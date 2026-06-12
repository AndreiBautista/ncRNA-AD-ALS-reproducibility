# Reproducibility Stress-Testing of an AD-ALS ncRNA Biomarker Signature

This repository contains the manuscript-supporting data, figure files, and pipeline archives for the study:

**Reproducibility Stress-Testing Reveals Fragility of an Alzheimer Disease-ALS ncRNA Biomarker Signature**

## Purpose

The project reconstructs and stress-tests a previously reported five-ncRNA Alzheimer disease (AD) / amyotrophic lateral sclerosis (ALS) overlap:

- MEG9
- ZMIZ1-AS1
- SLC12A5-AS1
- GUSBP1
- STRCP1

The manuscript evaluates dataset provenance, gene-identifier harmonization, overlap definition, direction-of-effect consistency, independent AD validation, and cross-disease model transportability. The main conclusion is that the nominal five-gene overlap can be reconstructed under a specific GSE203206 + GSE124439 symbol-level analysis path, but the stronger claim of a validated cross-disease biomarker panel is not supported.

## Repository structure

```text
data/
  manuscript_tables/        Tables used directly in the manuscript.
  figure_source_data/       Larger derived source outputs used for figure/table reconstruction.
figures/
  final/                    Main figure files available as PNG/PDF exports.
scripts/
  manuscript_reproduction/  Lightweight scripts to regenerate manuscript-facing summary tables.
pipeline_archive/
  current_pipeline_scripts_and_docs.zip
  legacy_pipeline_scripts_and_docs.zip
manuscript/
  Current manuscript draft.
docs/
  Repository notes and data/code availability text.
```

## Public source datasets

Raw/public source data are available from GEO under the following accessions:

- GSE203206
- GSE48350
- GSE124439
- GSE153960
- GSE33000

This repository contains derived tables and project artifacts needed to support the manuscript tables, figures, and reproducibility audit. It does not redistribute full raw GEO datasets.

## Pipeline archives

The `pipeline_archive/` folder contains compressed script/documentation archives extracted from the previously provided project zip files. These archives intentionally exclude virtual environments, large raw data folders, and large result directories.

- `current_pipeline_scripts_and_docs.zip`: current pipeline code and documentation.
- `legacy_pipeline_scripts_and_docs.zip`: earlier science-fair/legacy pipeline scripts and documentation.

## Reproducing manuscript tables

```bash
python scripts/manuscript_reproduction/reproduce_tables.py
```

The script reads the derived project outputs in `data/manuscript_tables/` and writes clean manuscript-facing CSV summaries to `outputs/reproduced_tables/`.

## Reproducing figures

The main figure exports are included in `figures/final/`. Some figures were generated during manuscript development from the project outputs and figure source tables. A lightweight helper script is included:

```bash
python scripts/manuscript_reproduction/make_figures.py
```

This helper regenerates simple audit summary visualizations from the included source tables. Journal-ready figure exports may have been manually polished after generation.

## Data availability statement draft

All derived data tables, figure source data, and scripts required to support the manuscript tables and figures are available in this repository. Raw transcriptomic data are publicly available from GEO under accessions GSE203206, GSE48350, GSE124439, GSE153960, and GSE33000.

## License

Code is released under the MIT License. Derived tables are provided for scholarly reproducibility with attribution to the manuscript authors. Raw GEO datasets remain governed by their source repository terms.
