"""
File: data_preprocessing.py

Purpose:
Clean and preprocess retail sales data.
"""

import pandas as pd
import os


def preprocess_data():

    file_path = "data/simulated/synthetic_sales.csv"

    df = pd.read_csv(file_path)

    print("Original Shape:", df.shape)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Sort values
    df = df.sort_values(
        by=["date", "product"]
    )

    # Handle missing values
    df.ffill(inplace=True)

    # Remove duplicates
    df = df.drop_duplicates()

    print("Cleaned Shape:", df.shape)

    # Save processed data
    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    output_path = "data/processed/cleaned_sales.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("Processed data saved:")
    print(output_path)

    return df


if __name__ == "__main__":
    preprocess_data()