import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load RFM with segments
rfm = pd.read_csv("outputs/rfm_segments.csv")

# Encode segment
rfm["Segment"] = rfm["Segment"].astype("category")

features = ["Recency", "Frequency", "R", "F", "Segment"]
target = "Monetary"

X = rfm[features]
y = np.log1p(rfm[target])  # log scale

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

cat_features = ["Segment"]

model = CatBoostRegressor(
    iterations=600,
    depth=6,
    learning_rate=0.05,
    loss_function="MAE",
    verbose=100,
    random_seed=42
)

model.fit(
    X_train,
    y_train,
    cat_features=cat_features,
    eval_set=(X_test, y_test)
)

# Evaluation
preds = model.predict(X_test)
mae = mean_absolute_error(np.expm1(y_test), np.expm1(preds))
print(f"CLV MAE: {mae:.2f}")

# Predict CLV for all customers
rfm["Predicted_CLV"] = np.expm1(model.predict(X))

rfm.to_csv("outputs/customer_clv_predictions.csv", index=False)
model.save_model("outputs/clv_catboost_model.cbm")

print("Saved:")
print("- outputs/customer_clv_predictions.csv")
print("- outputs/clv_catboost_model.cbm")
