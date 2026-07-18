"""
02_merge_traits_genotypes.py
Portfolio-safe template for merging phenotype and genotype data.
"""

import pandas as pd

# Load encoded genotype matrix
geno = pd.read_csv("genotype_encoded.csv")

# Load phenotype file
traits = pd.read_csv("path/to/phenotype.csv")

# Select relevant columns
traits_subset = traits[["Accession_ID", "plant_height"]]

# Merge on Accession_ID
merged = pd.merge(traits_subset, geno, on="Accession_ID")

# Remove sample with missing genotype (placeholder)
merged_clean = merged[merged["Accession_ID"] != "MISSING_SAMPLE"]

# Save cleaned dataset
merged_clean.to_csv("merged_traits_genotype_cleaned.csv", index=False)
