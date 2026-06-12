#!/usr/bin/env python3
"""Generate lightweight reproducibility-audit summary figures.

The manuscript's journal-ready figure exports are stored in figures/final. This script
creates simple reproducible audit plots from the included source tables, useful for
checking the quantitative story behind the manuscript.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "reproduced_figures"
OUT.mkdir(parents=True, exist_ok=True)

# AUC transportability bar plot.
auc_rows = [
    ("Phase 1 AD internal", 0.949),
    ("Phase 1 ALS internal", 0.918),
    ("Phase 2 pooled/internal", 0.879),
    ("Train AD -> test ALS", 0.5007),
    ("Train ALS -> test AD", 0.4540),
]
auc = pd.DataFrame(auc_rows, columns=["Evaluation", "AUC"])
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.bar(auc["Evaluation"], auc["AUC"])
ax.axhline(0.5, linestyle="--", linewidth=1)
ax.set_ylim(0, 1.05)
ax.set_ylabel("AUC")
ax.set_title("Internal discrimination versus cross-disease transportability")
for i, v in enumerate(auc["AUC"]):
    ax.text(i, v + 0.025, f"{v:.3f}", ha="center", va="bottom", fontsize=8)
ax.tick_params(axis="x", rotation=30)
fig.tight_layout()
fig.savefig(OUT / "auc_transportability_summary.png", dpi=300)
plt.close(fig)

# Direction consistency summary.
direction = pd.DataFrame([
    ("MEG9", "Same down"),
    ("STRCP1", "Same down"),
    ("ZMIZ1-AS1", "Same down"),
    ("SLC12A5-AS1", "Opposite"),
    ("GUSBP1", "Opposite"),
], columns=["Gene", "Direction"])
counts = direction["Direction"].value_counts().rename_axis("Direction").reset_index(name="Count")
fig, ax = plt.subplots(figsize=(5, 4))
ax.bar(counts["Direction"], counts["Count"])
ax.set_ylabel("Number of genes")
ax.set_title("Original AD/ALS direction consistency")
for i, v in enumerate(counts["Count"]):
    ax.text(i, v + 0.05, str(v), ha="center")
fig.tight_layout()
fig.savefig(OUT / "direction_consistency_summary.png", dpi=300)
plt.close(fig)

print(f"Wrote reproducible figure checks to {OUT}")
