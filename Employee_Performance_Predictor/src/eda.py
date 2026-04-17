"""
eda.py
"""

import matplotlib.pyplot as plt
import seaborn as sns


def perform_eda(df):

    sns.set()

    # Performance Distribution

    plt.figure(figsize=(8, 6))

    sns.countplot(
        x="Performance_Level",
        data=df
    )

    plt.title("Performance Distribution")

    plt.savefig(
        "images/performance_distribution.png"
    )

    plt.close()

    # Correlation Heatmap

    plt.figure(figsize=(10, 8))

    corr = df.corr(
        numeric_only=True
    )

    sns.heatmap(
        corr,
        annot=False,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.savefig(
        "images/correlation_heatmap.png"
    )

    plt.close()

    print("EDA completed!")