#!/usr/bin/env python3
"""Create clean manuscript-facing tables from included derived project outputs.

This script is intentionally lightweight. It reproduces the fixed tables used in the
reproducibility stress-testing manuscript from the repository's derived CSV files.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "manuscript_tables"
OUT = ROOT / "outputs" / "reproduced_tables"
OUT.mkdir(parents=True, exist_ok=True)

# Table 1: original reconstruction evidence, fixed manuscript-facing values.
table1 = pd.DataFrame([
    {"Gene": "MEG9", "AD log2FC": -1.051, "AD FDR": "9.94e-05", "ALS log2FC": -0.756, "ALS FDR": "0.03992", "Direction consistency": "Same down", "Conservative interpretation": "Strongest exploratory candidate; not clinically validated"},
    {"Gene": "GUSBP1", "AD log2FC": -0.7144, "AD FDR": "1.96e-04", "ALS log2FC": 0.3135, "ALS FDR": "0.04759", "Direction consistency": "Opposite", "Conservative interpretation": "Remove or heavily qualify"},
    {"Gene": "STRCP1", "AD log2FC": -0.5727, "AD FDR": "0.009168", "ALS log2FC": -0.8831, "ALS FDR": "0.02638", "Direction consistency": "Same down", "Conservative interpretation": "Strong exploratory candidate; coverage-limited"},
    {"Gene": "ZMIZ1-AS1", "AD log2FC": -0.5806, "AD FDR": "0.01575", "ALS log2FC": -0.6245, "ALS FDR": "0.01655", "Direction consistency": "Same down", "Conservative interpretation": "Secondary exploratory candidate"},
    {"Gene": "SLC12A5-AS1", "AD log2FC": 0.2848, "AD FDR": "0.04934", "ALS log2FC": -0.5327, "ALS FDR": "0.03208", "Direction consistency": "Opposite", "Conservative interpretation": "Remove from strict convergence claim"},
])
table1.to_csv(OUT / "table1_original_reconstruction_evidence.csv", index=False)

# Table 2: fixed-panel validation summary.
table2 = pd.DataFrame([
    {"Dataset": "GSE203206", "Disease": "AD", "Genes present": "5/5", "FDR-significant genes": "5/5", "Direction summary": "MEG9, STRCP1, and ZMIZ1-AS1 directionally consistent with ALS; SLC12A5-AS1 and GUSBP1 opposite relative to ALS", "Main interpretation": "Original AD path retained the panel but included opposite-direction genes relative to ALS."},
    {"Dataset": "GSE48350", "Disease": "AD", "Genes present": "3/5", "FDR-significant genes": "0/5 at FDR < 0.05", "Direction summary": "MEG9 down but not significant; ZMIZ1-AS1 up and not significant; GUSBP1 borderline; SLC12A5-AS1 and STRCP1 missing", "Main interpretation": "Independent AD validation was incomplete and did not validate the full panel."},
    {"Dataset": "GSE124439", "Disease": "ALS", "Genes present": "5/5", "FDR-significant genes": "5/5", "Direction summary": "MEG9, STRCP1, and ZMIZ1-AS1 down; SLC12A5-AS1 down and GUSBP1 up, opposite relative to original AD evidence", "Main interpretation": "Statistical support present, but strict convergence was not rescued for all five genes."},
])
table2.to_csv(OUT / "table2_phase2_fixed_panel_validation_summary.csv", index=False)

# Table 3: final gene classification.
table3 = pd.DataFrame([
    {"Gene": "MEG9", "Validation behavior": "Down in original AD and ALS paths; not significant in GSE48350", "Final classification": "Strongest exploratory candidate", "Manuscript recommendation": "Prioritize for follow-up; avoid biomarker validity language"},
    {"Gene": "STRCP1", "Validation behavior": "Down where present; absent from GSE48350", "Final classification": "Strong exploratory candidate, coverage-limited", "Manuscript recommendation": "Retain as exploratory; require better coverage and orthogonal validation"},
    {"Gene": "ZMIZ1-AS1", "Validation behavior": "Supported in GSE203206 and GSE124439; up and non-significant in GSE48350", "Final classification": "Secondary exploratory candidate", "Manuscript recommendation": "Qualify convergence claim"},
    {"Gene": "SLC12A5-AS1", "Validation behavior": "Opposite original AD/ALS direction; missing in GSE48350", "Final classification": "Remove from strict convergence claim", "Manuscript recommendation": "Discuss as sensitivity failure, not convergent marker"},
    {"Gene": "GUSBP1", "Validation behavior": "Opposite original AD/ALS direction; borderline in GSE48350", "Final classification": "Remove or heavily qualify", "Manuscript recommendation": "Do not use as evidence of shared dysregulation"},
])
table3.to_csv(OUT / "table3_final_gene_classification.csv", index=False)

print(f"Wrote reproduced tables to {OUT}")
