# feature_importance_R.R
# Portfolio-safe template for computing XGBoost feature importance in R.

library(xgboost)
library(ggplot2)

# Load training data
train <- read.csv("training_set.csv")

# Prepare matrices
X <- as.matrix(train[, !(names(train) %in% c("Accession_ID", "plant_height"))])
y <- train$plant_height

# Train model
model <- xgboost(
  data = X,
  label = y,
  objective = "reg:squarederror",
  nrounds = 600,
  max_depth = 5,
  eta = 0.01,
  subsample = 0.6,
  colsample_bytree = 0.8,
  min_child_weight = 1.5,
  gamma = 1,
  verbose = 0
)

# Compute importance
importance <- xgb.importance(model = model)

# Save importance table (without SNP IDs)
write.csv(importance, "feature_importance_summary.csv", row.names = FALSE)

# Plot gain (no SNP IDs shown)
ggplot(importance[1:15, ], aes(x = reorder(Feature, Gain), y = Gain)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(title = "Top Features by Gain (IDs omitted)",
       x = "Feature",
       y = "Gain")
