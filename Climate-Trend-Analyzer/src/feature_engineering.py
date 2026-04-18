# src/feature_engineering.py

import pandas as pd


def create_features(df):
    """
    Create additional climate features.
    """

    df["year"] = df["date"].dt.year

    df["month"] = df["date"].dt.month

    df["day"] = df["date"].dt.day

    # Season mapping
    def get_season(month):

        if month in [12, 1, 2]:
            return "Winter"

        elif month in [3, 4, 5]:
            return "Summer"

        elif month in [6, 7, 8, 9]:
            return "Monsoon"

        else:
            return "Post-Monsoon"

    df["season"] = df["month"].apply(get_season)

    return df


if __name__ == "__main__":

    from data_loader import load_data
    from preprocessing import preprocess_data

    df = load_data()

    df = preprocess_data(df)

    df = create_features(df)

    print(df.head())