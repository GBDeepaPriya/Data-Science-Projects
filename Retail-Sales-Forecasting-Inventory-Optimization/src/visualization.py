"""
File: visualization.py

Purpose:
Generate EDA visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_sales_trend():

    file_path = "data/processed/cleaned_sales.csv"

    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    # Aggregate sales
    daily_sales = df.groupby(
        "date"
    )["sales"].sum()

    os.makedirs(
        "outputs/plots",
        exist_ok=True
    )

    plt.figure()

    plt.plot(
        daily_sales.index,
        daily_sales.values
    )

    plt.title("Daily Sales Trend")

    plt.xlabel("Date")

    plt.ylabel("Sales")

    output_file = "outputs/plots/sales_trend.png"

    plt.savefig(output_file)

    plt.close()

    print("Sales trend plot saved.")


def plot_category_sales():

    file_path = "data/processed/cleaned_sales.csv"

    df = pd.read_csv(file_path)

    category_sales = df.groupby(
        "category"
    )["sales"].sum().reset_index()

    plt.figure()

    sns.barplot(
        x="category",
        y="sales",
        data=category_sales
    )

    plt.xticks(rotation=45)

    plt.title("Category-wise Sales")

    output_file = "outputs/plots/category_sales.png"

    plt.savefig(output_file)

    plt.close()

    print("Category sales plot saved.")


if __name__ == "__main__":
    plot_sales_trend()
    plot_category_sales()