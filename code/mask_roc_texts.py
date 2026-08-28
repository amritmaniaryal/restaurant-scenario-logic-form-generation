"""Mask (redact) ROCStories-derived story text in the release.

Replaces the raw story text of every ROCStories-derived record with the
placeholder ``[REDACTED — original ROCStories text; storyid=<uuid>]``. This is
the inverse of ``reconstruct_roc_texts.py`` — run it after re-running
experiments and before committing, so unmasked ROCStories text is never staged.

Run from the repository root:

    python code/mask_roc_texts.py
    python code/mask_roc_texts.py --check   # dry run, no changes

Records are identified from ``manifest_roc.json`` (sids 75-99). Only dataset
family files (those carrying a manifest ``storyid``, or located under
``experiments/FewShot/inputs/`` and ``experiments/FewShot/Results/``) and the
evaluated output files are touched; synthetic/generated corpora elsewhere are
left alone. This script does not contain any ROCStories text.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest_roc.json"
SKIP_PARTS = {".git", "__pycache__", ".ipynb_checkpoints"}
ROC_SIDS = set(range(75, 100))

# Locations that carry copies of the evaluation dataset (records mirror the
# fixed_dataset sid numbering). Synthetic/generated corpora live elsewhere and
# are never touched.
DATASET_FAMILY_PREFIXES = (
    ("experiments", "FewShot", "inputs"),
    ("experiments", "FewShot", "Results"),
)

PLACEHOLDER_RE = re.compile(
    r"\[REDACTED — original ROCStories text; storyid="
    r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\]"
)
MD_STORY_RE = re.compile(
    r"(## Story #(\d+) — [^\n]*\n\n\*\*Story:\*\* )([^\n]*)(\n)"
)


def is_placeholder(value):
    return isinstance(value, str) and bool(PLACEHOLDER_RE.fullmatch(value.strip()))


def placeholder_for(sid, storyid, sid_to_id):
    if storyid in sid_to_id.values() and storyid:
        return "[REDACTED — original ROCStories text; storyid=%s]" % storyid
    return "[REDACTED — original ROCStories text; storyid=%s]" % sid_to_id[sid]


def iter_files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in (".json", ".md"):
            continue
        rel = p.relative_to(ROOT)
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        yield p


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="Report what would be masked without modifying files")
    args = ap.parse_args()

    with open(MANIFEST, encoding="utf-8") as f:
        manifest = json.load(f)
    sid_to_id = {int(rec["sid"]): rec["storyid"] for rec in manifest["records"]}
    manifest_ids = set(sid_to_id.values())

    total = 0
    changed_files = []
    for p in iter_files():
        name = p.name
        changed = 0

        if p.suffix == ".md":
            if not name.endswith("_evaluated.md"):
                continue
            content = p.read_text(encoding="utf-8")

            def repl(m):
                nonlocal changed
                sid = int(m.group(2))
                if sid in ROC_SIDS and not is_placeholder(m.group(3)):
                    changed += 1
                    return m.group(1) + placeholder_for(sid, None, sid_to_id) + m.group(4)
                return m.group(0)

            new_content = MD_STORY_RE.sub(repl, content)
            if changed and not args.check:
                p.write_text(new_content, encoding="utf-8")
            if changed:
                changed_files.append(str(p.relative_to(ROOT)))

        else:  # .json
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue

            records = []
            is_eval_report = False
            if isinstance(data, dict) and isinstance(data.get("data"), list):
                records = data["data"]
            elif isinstance(data, dict):
                for key in ("exact_matches", "partial_matches", "mismatches"):
                    if data.get(key):
                        is_eval_report = True
                    records.extend(data.get(key, []) or [])

            if not records:
                continue

            # dataset-family files are those already carrying a manifest storyid
            # or living under the dataset-family locations; evaluation reports are
            # generated from the fixed dataset and are identified by sid directly.
            has_manifest_id = any(
                isinstance(r, dict) and r.get("storyid") in manifest_ids
                for r in records
            )
            rel_parts = p.relative_to(ROOT).parts
            is_dataset_family = has_manifest_id or rel_parts[:3] in DATASET_FAMILY_PREFIXES

            for rec in records:
                if not isinstance(rec, dict):
                    continue
                is_roc = (
                    rec.get("storyid") in manifest_ids
                    or (is_dataset_family and rec.get("sid") in ROC_SIDS)
                    or (is_eval_report and rec.get("sid") in ROC_SIDS)
                )
                if not is_roc:
                    continue
                sid = rec.get("sid")
                storyid = rec.get("storyid")
                for key in list(rec):
                    if key == "story" or "text" in key:
                        value = rec[key]
                        if isinstance(value, str) and not is_placeholder(value):
                            rec[key] = placeholder_for(sid, storyid, sid_to_id)
                            changed += 1
                if is_eval_report and is_roc and "story" not in rec:
                    rec["story"] = placeholder_for(sid, storyid, sid_to_id)
                    changed += 1

            if changed:
                if not args.check:
                    p.write_text(
                        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
                    )
                changed_files.append(str(p.relative_to(ROOT)))

        total += changed

    if args.check:
        print("--check: would mask %d value(s) in %d file(s)." % (total, len(changed_files)))
    else:
        print("Masked %d value(s) in %d file(s)." % (total, len(changed_files)))
    for rel in sorted(set(changed_files)):
        print("   %s" % rel)

    # Validation: every ROC record in the canonical dataset must be redacted.
    fixed = json.loads((ROOT / "encodedForm" / "fixed_all_combined.json")
                       .read_text(encoding="utf-8"))
    fixed_recs = {int(r["sid"]): r for r in fixed["data"]}
    missing = []
    for sid in sorted(ROC_SIDS):
        r = fixed_recs.get(sid, {})
        if not is_placeholder(r.get("text", "")):
            missing.append(sid)
    if missing:
        print("ERROR: fixed_all_combined.json is missing redaction for sids: %s" % missing)
        sys.exit(1)
    print("OK: all 25 ROCStories records in fixed_all_combined.json are redacted.")


if __name__ == "__main__":
    main()
