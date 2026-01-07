import pandas as pd

df = pd.read_csv("outputs/customer_clv_predictions.csv")

top_10 = df.sort_values("Predicted_CLV", ascending=False).head(10)
top_10.to_csv("outputs/top_10_customers.csv", index=False)

print(top_10[["CustomerID", "Segment", "Predicted_CLV"]])
