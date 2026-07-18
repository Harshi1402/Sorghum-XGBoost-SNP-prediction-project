# Results Overview

This project applied XGBoost to predict plant height in sorghum using high-dimensional SNP data.  
Key outcomes include:

## Model Performance

- **Training RMSE:** ~3.85  
- **Training R²:** ~0.99  
- **Validation RMSE:** ~22.49  
- **Validation R²:** ~0.51  

The model captured meaningful genomic signal but showed overfitting due to the large number of SNP features.

## Feature Importance

Feature importance was computed using XGBoost’s gain metric in R.  
High-impact genomic features were identified, but **specific SNP IDs are intentionally omitted** for ethical reasons.

Visual outputs include:

- Predicted vs actual height (training)
- Predicted vs actual height (validation)
- Gain-based feature importance barplot
- Gain vs frequency scatterplot

These plots help illustrate model behaviour and highlight genomic regions contributing to height variation.

## Interpretation

- The model generalises moderately well for a polygenic trait.
- Regularisation and tuning improved validation performance.
- High-ranking features are candidates for future biological validation.
