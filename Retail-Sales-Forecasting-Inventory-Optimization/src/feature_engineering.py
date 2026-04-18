"""
File: feature_engineering.py

Purpose:
Create time-based features
for forecasting models.
"""

import pandas as pd
import os


def create_features():

    file_path = "data/processed/cleaned_sales.csv"

    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    # Time features
    df["day_of_week"] = df["date"].dt.dayofweek

    df["month"] = df["date"].dt.month

    df["week_of_year"] = df["date"].dt.isocalendar().week

    df["is_weekend"] = df["day_of_week"].apply(
        lambda x: 1 if x >= 5 else 0
    )

    # Lag features
    df["lag_7"] = df.groupby("product")[
        "sales"
    ].shift(7)

    df["rolling_mean_7"] = df.groupby("product")[
        "sales"
    ].transform(
        lambda x: x.rolling(7).mean()
    )

    df = df.dropna()

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    output_path = "data/processed/featured_sales.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("Feature engineered dataset saved.")

    return df


if __name__ == "__main__":
    create_features()