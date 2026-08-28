#!/usr/bin/env python3
"""Build the ``evaluation_viz.ipynb`` notebook.

Generates ``experiments/Evaluation/evaluation_viz.ipynb`` with the analysis
function and per-experiment cells that compute pass rates and score
distributions from ``Manual_evaluation.xlsx`` and save figures to
``experiments/Evaluation/figures/``.
"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {"name": "python", "version": "3.13.0"}
}

cells = []

# ── Cell 1: Imports & config ──────────────────────────────────────────
cells.append(nbf.v4.new_code_cell(
    """import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings, os, sys
warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid", palette="Set2")

EXCEL_PATH = "Manual_evaluation.xlsx"
FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

EXPERIMENTS = {
    "ZeroShot-V1":          {"sheet": "zeroshot_v1",          "header": 0},
    "FewShot-5-Random-V1":  {"sheet": "fewshot_5_random_v1",  "header": 0},
    "FewShot-5-Random-V2":  {"sheet": "fewshot_5_random_v2",  "header": 0},
    "FewShot-10-Random-V1": {"sheet": "fewshot_10_random_v1", "header": 0},
    "FewShot-10-Random-V2": {"sheet": "fewshot_10_random_v2", "header": 0},
    "Manual-Prompting":     {"sheet": "manual_exp",           "header": 0},
}

MODEL_COLS = ["ChatGPT", "Gemini", "DeepSeek"]
SHEET_MODEL_MAP = {"ChatGPT": "ChatGPT", "Gemini": "Gemini", "DeepSeek": "Deepseek"}

# SIDs to exclude per sheet (e.g., SID 15 was an example in 10-shot experiments)
EXCLUDE_SIDS = {
    "fewshot_10_random_v1": [15],
    "fewshot_10_random_v1_old": [15],
}"""
))

# ── Cell 2: Analysis function ─────────────────────────────────────────
cells.append(nbf.v4.new_code_cell(
    """def analyze_experiment(sheet_name, title, header=0, save=True):
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name, header=header)
    df.columns = [str(c) for c in df.columns]

    # Exclude known example SIDs (stories that were used as examples, not targets)
    if sheet_name in EXCLUDE_SIDS:
        sid_col = [c for c in df.columns if "SID" in str(c).upper() or "sid" in str(c)]
        if sid_col:
            before = len(df)
            df = df[~df[sid_col[0]].isin(EXCLUDE_SIDS[sheet_name])]
            if len(df) < before:
                print(f"  (excluded {before - len(df)} row(s) for SID(s) {EXCLUDE_SIDS[sheet_name]})")

    # Identify score columns for each model
    score_cols = {}
    for mdl, sheet_mdl in SHEET_MODEL_MAP.items():
        candidates = [c for c in df.columns if sheet_mdl in str(c) and "Unnamed" not in str(c)]
        # Score col is the first non-SID, non-Evaluated, non-Remarks column for this model
        for c in candidates:
            if "emarks" not in str(c) and "ass?" not in str(c) and "valuated" not in str(c):
                score_cols[mdl] = c
                break

    stats = []
    for mdl in MODEL_COLS:
        col = score_cols.get(mdl)
        if col is None or col not in df.columns:
            continue
        scores = df[col].dropna()
        n = len(scores)
        if n == 0:
            stats.append({"Experiment": title, "Model": mdl, "N": 0,
                          "Pass Rate": None, "Pass": 0, "Fail": 0})
            continue
        passes = (scores >= 4).sum()
        fails = (scores < 4).sum()
        pass_rate = passes / n
        stats.append({"Experiment": title, "Model": mdl, "N": n,
                      "Pass Rate": round(pass_rate, 3),
                      "Pass": passes, "Fail": fails})

    result = pd.DataFrame(stats)

    # ── Print summary ──
    print(f"\\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(result[["Model", "N", "Pass Rate", "Pass", "Fail"]].to_string(index=False))
    print()

    # ── Pass rate bar chart ──
    fig, ax = plt.subplots(figsize=(7, 4.5))

    colors = ["#66c2a5", "#fc8d62", "#8da0cb"]
    bar_data = result.dropna(subset=["Pass Rate"])
    if len(bar_data) > 0:
        bars = ax.bar(bar_data["Model"], bar_data["Pass Rate"],
                      color=colors[:len(bar_data)], edgecolor="white", linewidth=0.8, width=0.55)
        ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=0.7, alpha=0.5)
        for bar, val in zip(bars, bar_data["Pass Rate"]):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                     f"{val:.0%}", ha="center", va="bottom", fontsize=10, fontweight="bold")
        ax.set_ylim(0, 1.15)
    ax.set_title(f"{title}: Pass Rate (score ≥ 4)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Pass Rate")
    ax.set_xlabel("")

    plt.tight_layout()

    safe_name = sheet_name.replace(" ", "_")
    path = f"{FIG_DIR}/{safe_name}_results.png"
    plt.savefig(path, dpi=300, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.show()

    return result"""
))

# ── Cell 3: Run all experiments ───────────────────────────────────────
cells.append(nbf.v4.new_code_cell(
    """all_results = []
for name, cfg in EXPERIMENTS.items():
    r = analyze_experiment(cfg["sheet"], name, cfg["header"])
    all_results.append(r)

summary = pd.concat(all_results, ignore_index=True)
print("\\nDone — all experiments analyzed.")"""
))

# ── Cell 4: Summary comparison ────────────────────────────────────────
cells.append(nbf.v4.new_code_cell(
    """# ── Grouped bar chart: pass rate across all experiments ──
fig, ax = plt.subplots(figsize=(12, 5))
pivot = summary.pivot_table(index="Experiment", columns="Model",
                             values="Pass Rate", aggfunc="first")
order = list(EXPERIMENTS.keys())
pivot = pivot.reindex(order)
pivot.plot(kind="bar", ax=ax, color=["#66c2a5", "#fc8d62", "#8da0cb"],
           edgecolor="white", linewidth=0.8, width=0.75)
ax.set_title("Pass Rate (score ≥ 4) Across All Experiments", fontsize=13, fontweight="bold")
ax.set_ylabel("Pass Rate")
ax.set_ylim(0, 1.1)
ax.set_xlabel("")
ax.legend(title="Model", fontsize=9)
ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=0.7, alpha=0.4)

# Annotate bars
for container in ax.containers:
    for bar in container:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.02,
                    f"{h:.0%}", ha="center", va="bottom", fontsize=8, fontweight="bold")

plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/all_experiments_pass_rate.png", dpi=300, bbox_inches="tight")
plt.show()

# ── Heatmap: pass rates ──
fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(pivot.T, annot=True, fmt=".0%", cmap="YlGn", linewidths=1,
            cbar_kws={"label": "Pass Rate"}, ax=ax)
ax.set_title("Pass Rate (score ≥ 4) — Experiment × Model", fontsize=13, fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("Model")
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/all_experiments_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()"""
))

# ── Cell 5: Detailed score distribution (optional) ────────────────────
cells.append(nbf.v4.new_code_cell(
    """def score_distribution(sheet_name, title, header=0):
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name, header=header)
    df.columns = [str(c) for c in df.columns]

    # Identify score columns
    score_cols = {}
    for mdl, sheet_mdl in SHEET_MODEL_MAP.items():
        candidates = [c for c in df.columns if sheet_mdl in str(c) and "Unnamed" not in str(c)]
        for c in candidates:
            if "emarks" not in str(c) and "ass?" not in str(c) and "valuated" not in str(c):
                score_cols[mdl] = c
                break

    bins = [0, 1, 2, 3, 4, 4.5, 5]
    labels = ["0", "1", "2", "3", "4", "4.5/5"]

    fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
    for ax, mdl in zip(axes, MODEL_COLS):
        col = score_cols.get(mdl)
        if col is None or col not in df.columns:
            ax.set_title(f"{mdl}: no data")
            continue
        scores = df[col].dropna()
        # Bucket: put 4.5 and 5 together, 4 alone
        bucket = scores.copy()
        bucket = bucket.apply(lambda x: "4.5/5" if x >= 4.5 else (str(int(x)) if x == int(x) else str(x)))
        # Count by bucket
        order = ["0", "1", "2", "3", "4", "4.5/5"]
        counts = bucket.value_counts().reindex(order, fill_value=0)
        colors_dist = ["#d73027", "#fc8d59", "#fee08b", "#d9ef8b", "#91cf60", "#1a9850"]
        bars = ax.bar(order, counts.values, color=colors_dist, edgecolor="white", linewidth=0.8)
        for bar, val in zip(bars, counts.values):
            if val > 0:
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                        str(val), ha="center", va="bottom", fontsize=10, fontweight="bold")
        ax.set_title(f"{mdl}", fontsize=12, fontweight="bold")
        ax.set_xlabel("Score")
        ax.axvline(x=3.5, color="red", linestyle="--", linewidth=0.7, alpha=0.5,
                   label="Pass/fail boundary")
        if mdl == "ChatGPT":
            ax.set_ylabel("Count")
        # Mark pass/fail region
        ax.text(0.5, 0.95, "FAIL", transform=ax.get_xaxis_transform(),
                ha="center", fontsize=8, color="red", alpha=0.6, fontweight="bold")
        ax.text(4.5, 0.95, "PASS", transform=ax.get_xaxis_transform(),
                ha="center", fontsize=8, color="green", alpha=0.6, fontweight="bold")

    fig.suptitle(f"{title}: Score Distribution", fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    safe_name = sheet_name.replace(" ", "_")
    plt.savefig(f"{FIG_DIR}/{safe_name}_distribution.png", dpi=300, bbox_inches="tight")
    plt.show()

# Run for all experiments
for name, cfg in EXPERIMENTS.items():
    score_distribution(cfg["sheet"], name, cfg["header"])"""
))

# ── Cell 6: Score distribution summary table ──────────────────────────
cells.append(nbf.v4.new_code_cell(
    """# Print a clean summary table for the thesis
def print_summary_table(all_results_df):
    pivot = all_results_df.pivot_table(
        index="Experiment", columns="Model",
        values=["N", "Pass Rate", "Pass", "Fail"],
        aggfunc="first"
    )
    # Reorder columns for readability
    pivot = pivot.reorder_levels([1, 0], axis=1).sort_index(axis=1)
    print("Semantic Evaluation Summary (score ≥ 4 = pass)\\n")
    print(pivot.to_string())

print_summary_table(summary)"""
))

nb.cells = cells

import nbformat
nbformat.write(nb, "experiments/Evaluation/evaluation_viz.ipynb")
print("Done: experiments/Evaluation/evaluation_viz.ipynb")
