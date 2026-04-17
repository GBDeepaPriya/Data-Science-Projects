"""
data_preprocessing.py
"""

import pandas as pd


def clean_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = df[col].fillna(
                df[col].mode()[0]
            )

        else:

            df[col] = df[col].fillna(
                df[col].mean()
            )

    print("Data cleaned!")

    return df


def save_cleaned_data(df):

    path = "data/processed/cleaned_data.csv"

    df.to_csv(
        path,
        index=False
    )

    print("Cleaned data saved!")

    return path