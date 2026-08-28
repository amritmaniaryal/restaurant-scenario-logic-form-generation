#!/usr/bin/env python3
"""Convert evaluated JSON files to Markdown for easy clingo copy-paste."""
import json
from pathlib import Path

BASE = Path(__file__).parent

def fmt_predicates(label, text):
    return f"### {label}\n```clingo\n{text}\n```\n"

def fmt_entry(entry, kind):
    sid = entry["sid"]
    sim = entry["similarity"]
    story = entry.get("story", "")
    pred = entry["predicted"]
    gt = entry["ground_truth"]
    lines = []
    lines.append(f"## Story #{sid} — {kind} (Similarity: {sim:.4f})\n")
    lines.append(f"**Story:** {story}\n")
    lines.append(fmt_predicates("Predicted", pred))
    lines.append(fmt_predicates("Ground Truth", gt))
    lines.append("---\n")
    return "\n".join(lines)

def convert_json_to_md(json_path):
    with open(json_path) as f:
        data = json.load(f)

    md_path = json_path.with_suffix(".md")
    summary = data["summary"]

    lines = []
    lines.append(f"# {json_path.stem}\n")
    lines.append("## Summary\n")
    lines.append(f"- Total common: {summary['total_common']}")
    lines.append(f"- Exact matches: {summary['exact_matches']}")
    lines.append(f"- Partial matches: {summary['partial_matches']}")
    if summary.get("predicted_only_count"):
        lines.append(f"- Predicted-only SIDs: {summary['predicted_only_count']}")
    if summary.get("ground_truth_only_count"):
        lines.append(f"- Ground-truth-only SIDs: {summary['ground_truth_only_count']}")
    lines.append(f"- Accuracy: {summary['accuracy']}")
    lines.append("")

    if data.get("predicted_only_sids"):
        lines.append(f"**Predicted-only SIDs:** {data['predicted_only_sids']}\n")
    if data.get("ground_truth_only_sids"):
        lines.append(f"**Ground-truth-only SIDs:** {data['ground_truth_only_sids']}\n")

    lines.append("---\n")

    for entry in data.get("exact_matches", []):
        lines.append(fmt_entry(entry, "Exact Match"))

    for entry in data.get("partial_matches", []):
        lines.append(fmt_entry(entry, "Partial Match"))

    with open(md_path, "w") as f:
        f.write("\n".join(lines))

    print(f"  → {md_path}")

def main():
    json_files = sorted(BASE.rglob("*.json"))
    if not json_files:
        print("No JSON files found.")
        return
    for jf in json_files:
        if jf.name == "convert_to_md.py":
            continue
        if any(part.endswith("_backup") for part in jf.parts):
            continue
        print(f"Converting: {jf.relative_to(BASE)}")
        convert_json_to_md(jf)

if __name__ == "__main__":
    main()
