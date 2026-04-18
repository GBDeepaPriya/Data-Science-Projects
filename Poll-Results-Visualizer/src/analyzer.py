# src/analyzer.py

import pandas as pd


def calculate_vote_counts(df):

    counts = df["Preferred_Product"].value_counts()

    return counts


def calculate_percentages(df):

    counts = calculate_vote_counts(df)

    percentages = (
        counts / counts.sum()
    ) * 100

    summary_df = pd.DataFrame({

        "Votes": counts,
        "Percentage": percentages.round(2)

    })

    return summary_df


def region_analysis(df):

    region_df = pd.crosstab(

        df["Region"],
        df["Preferred_Product"]

    )

    return region_df


def satisfaction_analysis(df):

    rating_avg = df.groupby(
        "Preferred_Product"
    )["Satisfaction_Rating"].mean()

    return rating_avg