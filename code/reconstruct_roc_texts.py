"""Restore redacted ROCStories texts from the official ROCStories corpus.

The public release replaces raw ROCStories text with placeholders of the form
``[REDACTED — original ROCStories text; storyid=<uuid>]`` (see
RECONSTRUCTION.md). This script fills those placeholders back in using a
user-supplied copy of the official ``ROCStories.csv`` (obtained from
https://www.cs.rochester.edu/nlp/rocstories/).

Usage:
    python code/reconstruct_roc_texts.py --csv other_data/ROCStories.csv
    python code/reconstruct_roc_texts.py --csv other_data/ROCStories.csv --check
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest_roc.json"
SKIP_PARTS = {".git", "__pycache__", ".ipynb_checkpoints"}

PLACEHOLDER_RE = re.compile(
    r"\[REDACTED — original ROCStories text; storyid="
    r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\]"
)


def load_manifest():
    with open(MANIFEST, encoding="utf-8") as f:
        return json.load(f)


def load_story_texts(csv_path):
    """Index storyid -> 'sentence1 sentence2 sentence3 sentence4 sentence5'."""
    story_texts = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sid = (row.get("storyid") or "").strip()
            if not sid:
                continue
            sentences = " ".join(
                (row.get("sentence%d" % i) or "").strip() for i in range(1, 6)
            ).strip()
            if sentences:
                story_texts[sid] = sentences
    return story_texts


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
    ap.add_argument("--csv", required=True,
                    help="Path to the official ROCStories.csv")
    ap.add_argument("--check", action="store_true",
                    help="Validate that every placeholder resolves in the CSV "
                         "without modifying any file")
    args = ap.parse_args()

    manifest = load_manifest()
    manifest_ids = {rec["storyid"] for rec in manifest["records"]}

    story_texts = load_story_texts(args.csv)
    missing = manifest_ids - set(story_texts)
    if missing:
        print("ERROR: %d manifest storyid(s) not found in %s:" % (len(missing), args.csv))
        for sid in sorted(missing):
            print("   ", sid)
        sys.exit(1)

    total_tokens = 0
    per_file = []
    for p in iter_files():
        text = p.read_text(encoding="utf-8")
        tokens = PLACEHOLDER_RE.findall(text)
        if not tokens:
            continue
        unresolved = sorted({t for t in tokens if t not in story_texts})
        if unresolved:
            print("ERROR: %s references storyid(s) missing from the CSV:" % p.relative_to(ROOT))
            for t in unresolved:
                print("   ", t)
            sys.exit(1)
        total_tokens += len(tokens)
        per_file.append((str(p.relative_to(ROOT)), len(tokens)))
        if not args.check:
            p.write_text(
                PLACEHOLDER_RE.sub(lambda m: story_texts[m.group(1)], text),
                encoding="utf-8",
            )

    if args.check:
        print("--check: %d placeholder(s) across %d file(s) resolve in the CSV."
              % (total_tokens, len(per_file)))
        for rel, n in per_file:
            print("   %4d  %s" % (n, rel))
        return

    print("Restored %d placeholder(s) across %d file(s):" % (total_tokens, len(per_file)))
    for rel, n in per_file:
        print("   %4d  %s" % (n, rel))

    remaining = sum(len(PLACEHOLDER_RE.findall(p.read_text(encoding="utf-8")))
                    for p in iter_files())
    if remaining:
        print("ERROR: %d placeholder(s) remain — check the list above." % remaining)
        sys.exit(1)
    print("Done: no placeholders remain.")


if __name__ == "__main__":
    main()
