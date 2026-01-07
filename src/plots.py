import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/customer_clv_predictions.csv")

avg_clv = df.groupby("Segment")["Predicted_CLV"].mean().sort_values()

plt.figure(figsize=(8,5))
avg_clv.plot(kind="barh")
plt.title("Average Predicted CLV by Customer Segment")
plt.xlabel("Predicted CLV")
plt.tight_layout()
plt.savefig("outputs/clv_by_segment.png")
plt.show()
