import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop missing customers
    df = df.dropna(subset=["CustomerID"])

    # Remove returns / cancellations
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Parse datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Total transaction value
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df
