"""
03_split_train_val.py
Portfolio-safe template for splitting dataset into training and validation sets.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("merged_traits_genotype_cleaned.csv")

train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

train_df.to_csv("training_set.csv", index=False)
val_df.to_csv("validation_set.csv", index=False)
