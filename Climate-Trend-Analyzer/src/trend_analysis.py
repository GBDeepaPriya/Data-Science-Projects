# src/trend_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def moving_average_trend(df, column, window=30):
    """
    Calculate moving average trend.
    """

    df[f"{column}_ma"] = df[column].rolling(
        window=window
    ).mean()

    return df


def plot_trend_with_moving_average(
    df,
    column
):
    """
    Plot actual vs moving average trend.
    """

    plt.figure(figsize=(12, 6))

    plt.plot(
        df["date"],
        df[column],
        label="Actual"
    )

    plt.plot(
        df["date"],
        df[f"{column}_ma"],
        label="Moving Average",
        linewidth=2
    )

    plt.title(f"{column} Trend Analysis")

    plt.xlabel("Date")

    plt.ylabel(column)

    plt.legend()

    plt.savefig(
        f"outputs/plots/{column}_moving_average.png"
    )

    plt.show()


def linear_trend_analysis(df, column):
    """
    Calculate linear trend line.
    """

    x = np.arange(len(df))

    y = df[column]

    slope, intercept = np.polyfit(x, y, 1)

    trend_line = slope * x + intercept

    df[f"{column}_trend"] = trend_line

    return df