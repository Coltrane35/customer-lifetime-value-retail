import pandas as pd

def assign_segment(rfm: pd.DataFrame) -> pd.DataFrame:
    rfm = rfm.copy()

    def segment(row):
        if row["R"] >= 4 and row["F"] >= 4:
            return "Champions"
        if row["R"] >= 3 and row["F"] >= 3:
            return "Loyal Customers"
        if row["R"] >= 4 and row["F"] <= 2:
            return "New Customers"
        if row["R"] <= 2 and row["F"] >= 3:
            return "At Risk"
        if row["R"] <= 2 and row["F"] <= 2:
            return "Lost"
        return "Others"

    rfm["Segment"] = rfm.apply(segment, axis=1)
    return rfm
