#!/usr/bin/env python3
"""Check each predicted encoding with clingo and write parsability stats per experiment folder."""
import json
import os
import sys
from contextlib import contextmanager
from pathlib import Path

try:
    import clingo
except ImportError:
    print("clingo not installed. Run: pip install clingo")
    sys.exit(1)

BASE = Path(__file__).parent
INPUTS = Path(__file__).parent.parent / "FewShot" / "inputs"

# Map experiment folder → input file → example SIDs to exclude
EXAMPLE_SIDS = {
    "zeroshot_v1":                  (None, []),
    "fewshot_5_random_v1":          ("5_random_input.json", [1, 59, 78, 93, 98]),
    "fewshot_5_random_v2":          ("5_random_input.json", [1, 59, 78, 93, 98]),
    "fewshot_5_v1":                 ("fewshot_5_input.json", [0, 17, 26, 45, 71]),
    "fewshot_10_random_v1":         ("10_random_input.json", [5, 6, 7, 15, 35, 43, 50, 59, 74, 92]),
    "fewshot_10_random_v2":         ("10_random_input.json", [5, 6, 7, 15, 35, 43, 50, 59, 74, 92]),
    "fewshot_10_random_v3":         ("10_random_input.json", [5, 6, 7, 15, 35, 43, 50, 59, 74, 92]),
    "manual_prompting":             ("10_random_input.json", [5, 6, 7, 15, 35, 43, 50, 59, 74, 92]),
}

def get_target_sids(folder_name):
    cfg = EXAMPLE_SIDS.get(folder_name, (None, []))
    if cfg[0] is None:
        return None  # all stories are targets
    input_path = INPUTS / cfg[0]
    if not input_path.exists():
        return None
    with open(input_path) as f:
        raw = json.load(f)
    items = raw.get("data", raw) if isinstance(raw, dict) else raw
    all_sids = sorted(set(e["sid"] for e in items))
    example_sids = set(cfg[1])
    return [s for s in all_sids if s not in example_sids]

@contextmanager
def suppress_stderr():
    sys.stderr.flush()
    devnull = os.open(os.devnull, os.O_WRONLY)
    old = os.dup(2)
    os.dup2(devnull, 2)
    os.close(devnull)
    try:
        yield
    finally:
        sys.stderr.flush()
        os.dup2(old, 2)
        os.close(old)

def is_valid_clingo(text):
    ctrl = clingo.Control()
    try:
        with suppress_stderr():
            ctrl.add("base", [], text)
            ctrl.ground([("base", [])])
        return True
    except Exception:
        return False

def process_json(json_path, target_sids):
    with open(json_path) as f:
        data = json.load(f)

    model_name = json_path.stem

    # Collect all predicted entries by SID
    predicted = {}  # sid → predicted text
    null_predicted_sids = set()  # SIDs with null predicted text (missing output)
    for key in ["partial_matches", "mismatches", "exact_matches"]:
        for e in data.get(key, []) or []:
            sid = e.get("sid")
            text = e.get("predicted")
            if sid is not None and text is not None:
                predicted[sid] = text
            elif sid is not None and text is None:
                null_predicted_sids.add(sid)

    # Also check predicted_entries_missing_sid (predicted entries with no valid SID)
    missing_sid_count = 0
    for e in data.get("predicted_entries_missing_sid", []) or []:
        # These have predicted text but no valid SID — can still check syntax
        # Count them separately since we can't attribute them to a target
        if isinstance(e, dict) and e.get("predicted"):
            missing_sid_count += 1

    # Determine which SIDs to evaluate
    if target_sids is None:
        # No target list — use all entries from the JSON (original behavior)
        entries = data.get("exact_matches", []) + data.get("partial_matches", [])
        total = len(entries)
        if total == 0:
            return model_name, total, 0, 0, [], 0
        valid = []
        invalid = []
        for e in entries:
            sid = e["sid"]
            text = e["predicted"]
            if is_valid_clingo(text):
                valid.append(sid)
            else:
                invalid.append(sid)
        return model_name, total, len(valid), len(invalid), invalid, missing_sid_count

    # Evaluate each target SID
    total = len(target_sids)
    valid = []
    invalid = []
    missing = []

    for sid in target_sids:
        if sid in predicted:
            text = predicted[sid]
            if is_valid_clingo(text):
                valid.append(sid)
            else:
                invalid.append(sid)
        else:
            missing.append(sid)

    # "Missing" target SIDs: check ground_truth_only_sids and null_predicted_sids
    # to distinguish genuinely missing outputs from exact-match entries not stored
    gt_only = set(data.get("ground_truth_only_sids", []) or [])
    actual_missing = [s for s in missing if s in gt_only or s in null_predicted_sids]
    exact_match_targets = [s for s in missing if s not in gt_only and s not in null_predicted_sids]
    if exact_match_targets:
        valid += exact_match_targets

    not_parsable = len(invalid) + len(actual_missing) + missing_sid_count
    return model_name, total, len(valid), not_parsable, invalid + actual_missing, missing_sid_count

def main():
    folders = sorted(BASE.iterdir())
    for folder in folders:
        if not folder.is_dir() or folder.name.endswith("_backup"):
            continue
        json_files = sorted(folder.glob("*_evaluated.json"))
        if not json_files:
            continue

        target_sids = get_target_sids(folder.name)

        results = []
        for jf in json_files:
            results.append(process_json(jf, target_sids))

        out_path = folder / "parsability_stats.md"
        with open(out_path, "w") as f:
            f.write(f"# Parsability Stats — {folder.name}\n\n")
            f.write("| Model | Total | Parsable | Not Parsable | Invalid SIDs |\n")
            f.write("|-------|-------|----------|--------------|--------------|\n")
            for name, total, pcount, npcount, invalid_sids, msid_count in results:
                sid_str = ", ".join(str(s) for s in invalid_sids[:20])
                if len(invalid_sids) > 20:
                    sid_str += f", ... ({len(invalid_sids)} total)"
                if msid_count:
                    if sid_str:
                        sid_str += f", +{msid_count} missing-SID entries"
                    else:
                        sid_str += f"{msid_count} missing-SID entries"
                f.write(f"| {name} | {total} | {pcount} | {npcount} | {sid_str} |\n")
        print(f"  → {out_path}")

if __name__ == "__main__":
    main()
