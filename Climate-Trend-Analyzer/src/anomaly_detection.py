# src/anomaly_detection.py

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt


def zscore_anomaly_detection(
    df,
    column,
    threshold=3
):
    """
    Detect anomalies using Z-score.
    """

    mean = df[column].mean()

    std = df[column].std()

    df["zscore"] = (
        df[column] - mean
    ) / std

    df["anomaly"] = (
        df["zscore"].abs() > threshold
    )

    return df


def plot_anomalies(
    df,
    column
):
    """
    Plot anomalies on graph.
    """

    plt.figure(figsize=(12, 6))

    plt.plot(
        df["date"],
        df[column],
        label="Data"
    )

    anomalies = df[df["anomaly"]]

    plt.scatter(
        anomalies["date"],
        anomalies[column],
        color="red",
        label="Anomalies"
    )

    plt.legend()

    plt.title(
        f"{column} Anomaly Detection"
    )

    plt.savefig(
        f"outputs/plots/{column}_anomalies.png"
    )

    plt.show()


def isolation_forest_detection(
    df,
    column
):
    """
    Detect anomalies using Isolation Forest.
    """

    model = IsolationForest(
        contamination=0.01,
        random_state=42
    )

    df["anomaly_if"] = model.fit_predict(
        df[[column]]
    )

    df["anomaly_if"] = df["anomaly_if"] == -1

    return df