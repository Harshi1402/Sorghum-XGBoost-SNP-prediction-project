"""
xgboost_training.py
Portfolio-safe template for training an XGBoost regression model.
"""

import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load training data
train_df = pd.read_csv("training_set.csv")

# Separate features and target
X_train = train_df.drop(columns=["Accession_ID", "plant_height"])
y_train = train_df["plant_height"]

# Define model
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

# Train model
model.fit(X_train, y_train)

# Evaluate on training set
train_preds = model.predict(X_train)
rmse = np.sqrt(mean_squared_error(y_train, train_preds))
r2 = r2_score(y_train, train_preds)

print("Training RMSE:", rmse)
print("Training R²:", r2)
