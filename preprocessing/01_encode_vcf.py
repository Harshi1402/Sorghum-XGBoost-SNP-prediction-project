"""
01_encode_vcf.py
Portfolio-safe template for encoding VCF genotype data for XGBoost.
This script demonstrates the workflow used in the SCIE5003 project.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load VCF file (placeholder path)
df = pd.read_csv("path/to/combined.vcf", sep="\t")

# Separate metadata and genotype columns
metadata = df.iloc[:, :9]
genotypes = df.iloc[:, 9:]

# Encoding function
def encode(gt):
    if gt in ["0/0", "0|0"]:
        return 0
    elif gt in ["1/1", "1|1"]:
        return 1
    else:
        return np.nan

# Apply encoding
encoded = genotypes.apply(lambda col: col.map(encode))

# Fill missing values with column mode
encoded = encoded.fillna(encoded.mode().iloc[0])

# Optional scaling
scaler = MinMaxScaler()
scaled = pd.DataFrame(scaler.fit_transform(encoded), columns=encoded.columns)

# Convert to integers
scaled = scaled.astype(int)

# Combine metadata + encoded genotypes
vcf_encoded = pd.concat([metadata, scaled], axis=1)

# Save output (placeholder)
vcf_encoded.to_csv("genotype_encoded.csv", index=False)
