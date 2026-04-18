# src/data_loader.py

import pandas as pd


def load_data(file_path="data/raw/climate_data.csv"):
    """
    Load climate dataset.
    """

    df = pd.read_csv(file_path)

    print("Data Loaded Successfully!")

    return df


if __name__ == "__main__":

    df = load_data()

    print(df.head())