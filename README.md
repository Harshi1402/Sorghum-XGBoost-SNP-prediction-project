# XGBoost-Based SNP Discovery for Plant Height in Sorghum

This repository documents a machine‑learning workflow for predicting plant height in sorghum using GBS‑derived SNP data and XGBoost. The project was completed as part of SCIE5003 at UWA and focuses on identifying high‑impact genomic markers associated with height variation.

> This is a portfolio‑safe reconstruction of the project.  
> No raw VCF, phenotype files, or proprietary datasets are included.  
> No SNP identifiers are shown for ethical reasons.

## Aim

To build an optimized XGBoost regression model that predicts plant height from SNP data and identifies the most influential genomic features contributing to height variation.

## Why Sorghum?

- Drought‑tolerant, globally important cereal  
- Height influences lodging resistance, biomass yield, and adaptability  
- SNP‑based genomic prediction supports modern breeding programs

## Dataset

- GBS‑derived SNPs from Yu et al. (2016)  
- 962 accessions genotyped  
- 299 phenotyped for height  
- Phenotypes normalized using GBLUP  
- Final cleaned dataset: **498 samples × 115,833 SNPs**

## Tools & Languages

### Python (JupyterLab)
- VCF encoding  
- Genotype–phenotype merging  
- Train/validation splitting  
- XGBoost model training  
- RMSE & R² evaluation  

### R
- XGBoost feature importance (gain, cover, frequency)  
- Visualisation of ranked genomic features  

## Workflow Summary

1. **VCF Encoding**  
   - Convert 0/0 → 0, 1/1 → 1  
   - Transpose matrix (samples as rows, SNPs as columns)

2. **Merging**  
   - Align genotype + phenotype by Accession_ID  
   - Remove missing sample  
   - Produce final merged dataset

3. **Train/Validation Split**  
   - 80/20 split  
   - Training used for hyperparameter tuning  
   - Validation used for final evaluation

4. **Model Training (XGBoost)**  
   - Objective: `reg:squarederror`  
   - Hyperparameters tuned across team members  
   - Final model: RMSE = 3.85 (train), 22.49 (validation)

5. **Feature Importance**  
   - Gain metric used to rank genomic features  
   - High‑impact SNPs identified without listing specific IDs

## Key Findings

- Validation R² ≈ **0.516** — strong for a polygenic trait  
- Model captured meaningful genomic signal despite high dimensionality  
- Overfitting observed due to 115k SNP features  
- Regularisation + tuning improved generalisation  
- High‑ranking genomic features are candidates for future biological validation

## Biological Insight

High‑ranking features are strong candidates for:

- functional validation  
- marker‑assisted selection  
- genomic prediction pipelines  
- future transcriptomic or gene‑level studies  

## Repository Structure
Sorghum-Height-XGBoost/
│
├── preprocessing/        # Python scripts for data handling
├── model/                # XGBoost training, evaluation, R importance
├── docs/                 # Workflow documentation
├── data/                 # Structure-only documentation
└── results/              # Plots and ranked feature lists


## My Contribution

- Encoded VCF genotype data in Python  
- Merged phenotype + genotype matrices  
- Performed train/validation split  
- Trained XGBoost models in JupyterLab  
- Evaluated RMSE & R²  
- Contributed to feature‑importance interpretation  
- Collaborated using both Python and R  
- Documented workflow and results in a reproducible format

## Ethical Notice

This repository contains **only** scripts, documentation, and summaries.  
No raw VCF, phenotype files, or SNP identifiers are included.

## Team Members

- Harshita Khot  
- Brian Kibet Kipkosgey  
- Maureen Natukunda  
Supervisor: **Monica Danilevicz**

