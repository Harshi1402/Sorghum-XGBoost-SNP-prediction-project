"""
xgboost_evaluation.py
Portfolio-safe template for evaluating XGBoost model on validation data.
"""

import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load validation data
val_df = pd.read_csv("validation_set.csv")

X_val = val_df.drop(columns=["Accession_ID", "plant_height"])
y_val = val_df["plant_height"]

# Load or reinitialize model (same parameters)
model = XGBRegressor(
    objective="reg:squarederror",
    learning_rate=0.01,
    max_depth=5,
    subsample=0.6,
    colsample_bytree=0.8,
    reg_alpha=1,
    reg_lambda=1,
    min_child_weight=1.5,
    gamma=1,
    n_estimators=600,
    random_state=42
)

# Fit on training data again (portfolio-safe)
train_df = pd.read_csv("training_set.csv")
X_train = train_df.drop(columns=["Accession_ID", "plant_height"])
y_train = train_df["plant_height"]
model.fit(X_train, y_train)

# Predict on validation set
val_preds = model.predict(X_val)

rmse = np.sqrt(mean_squared_error(y_val, val_preds))
r2 = r2_score(y_val, val_preds)

print("Validation RMSE:", rmse)
print("Validation R²:", r2)
