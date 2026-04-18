import pandas as pd

def clean_data():

    df = pd.read_csv(
        "data/raw_expense_data.csv"
    )

    # Convert date
    df["date"] = pd.to_datetime(
        df["date"]
    )

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Feature Engineering
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["weekday"] = df["date"].dt.day_name()

    # Weekend flag
    df["is_weekend"] = df["weekday"].isin(
        ["Saturday", "Sunday"]
    )

    df.to_csv(
        "data/processed_expense_data.csv",
        index=False
    )

    print("Data Cleaned Successfully!")

if __name__ == "__main__":
    clean_data()