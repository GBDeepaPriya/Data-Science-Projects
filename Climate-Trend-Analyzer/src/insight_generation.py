# src/insight_generation.py

def generate_summary(df):
    """
    Generate climate summary insights.
    """

    summary = {}

    summary["avg_temperature"] = round(
        df["temperature"].mean(), 2
    )

    summary["max_temperature"] = round(
        df["temperature"].max(), 2
    )

    summary["total_rainfall"] = round(
        df["rainfall"].sum(), 2
    )

    summary["avg_co2"] = round(
        df["co2"].mean(), 2
    )

    return summary


def print_summary(summary):
    """
    Print readable insights.
    """

    print("\nClimate Summary\n")

    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )