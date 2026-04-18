# src/data_cleaner.py

import pandas as pd


def clean_data(df):

    print("Cleaning data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Standardize text
    df["Preferred_Product"] = (
        df["Preferred_Product"]
        .str.strip()
        .str.title()
    )

    # Convert timestamp
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"]
    )

    # Extract date
    df["Date"] = df["Timestamp"].dt.date

    return df


def save_cleaned_data(df):

    output_path = "data/processed/cleaned_poll_data.csv"

    df.to_csv(output_path, index=False)

    print("Cleaned data saved")