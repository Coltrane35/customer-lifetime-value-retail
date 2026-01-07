import pandas as pd
from preprocess import preprocess_data

def load_data(path="data/online_retail.csv"):
    df = pd.read_csv(path)
    df = preprocess_data(df)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print(df.shape)

if __name__ == "__main__":
    from rfm import build_rfm, score_rfm

    df = load_data()
    rfm = build_rfm(df)
    rfm = score_rfm(rfm)

    print(rfm.head())
    print(rfm.describe())

from segments import assign_segment

rfm = assign_segment(rfm)

print(rfm["Segment"].value_counts())

rfm.to_csv("outputs/rfm_segments.csv", index=False)
print("\nSaved: outputs/rfm_segments.csv")
