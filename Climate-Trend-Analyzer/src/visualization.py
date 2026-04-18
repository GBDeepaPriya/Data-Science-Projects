# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns


def plot_temperature_trend(df):

    plt.figure(figsize=(12, 6))

    plt.plot(df["date"], df["temperature"])

    plt.title("Temperature Trend Over Time")

    plt.xlabel("Date")

    plt.ylabel("Temperature")

    plt.savefig(
        "outputs/plots/temperature_trend.png"
    )

    plt.show()


def plot_rainfall_trend(df):

    plt.figure(figsize=(12, 6))

    plt.plot(df["date"], df["rainfall"])

    plt.title("Rainfall Trend Over Time")

    plt.xlabel("Date")

    plt.ylabel("Rainfall")

    plt.savefig(
        "outputs/plots/rainfall_trend.png"
    )

    plt.show()


def seasonal_temperature_plot(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        x="season",
        y="temperature",
        data=df
    )

    plt.title("Seasonal Temperature Distribution")

    plt.savefig(
        "outputs/plots/seasonal_temperature.png"
    )

    plt.show()