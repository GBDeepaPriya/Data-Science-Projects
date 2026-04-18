# src/preprocessing.py

import pandas as pd


def preprocess_data(df):
    """
    Clean climate dataset.
    """

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Sort data
    df = df.sort_values("date")

    # Handle missing values
    df = df.ffill()

    return df


if __name__ == "__main__":

    from data_loader import load_data

    df = load_data()

    df_clean = preprocess_data(df)

    print("Preprocessing Completed!")

    print(df_clean.head())