"""
File: model_evaluation.py

Purpose:
Visualize model performance.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_actual_vs_predicted():

    file_path = (
        "outputs/forecasts/"
        "forecast_results.csv"
    )

    df = pd.read_csv(file_path)

    plt.figure()

    plt.scatter(
        df["sales"],
        df["predicted_sales"]
    )

    plt.xlabel("Actual Sales")

    plt.ylabel("Predicted Sales")

    plt.title(
        "Actual vs Predicted Sales"
    )

    os.makedirs(
        "outputs/plots",
        exist_ok=True
    )

    output_file = (
        "outputs/plots/"
        "actual_vs_predicted.png"
    )

    plt.savefig(output_file)

    plt.close()

    print("Evaluation plot saved.")


if __name__ == "__main__":

    plot_actual_vs_predicted()