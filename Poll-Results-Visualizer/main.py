# main.py

from src.data_generator import save_poll_data
from src.data_loader import load_data
from src.data_cleaner import (
    clean_data,
    save_cleaned_data
)

from src.analyzer import (
    calculate_vote_counts,
    calculate_percentages,
    region_analysis
)

from src.visualizer import (
    bar_chart,
    pie_chart,
    region_chart,
    wordcloud_chart
)

from src.insights import generate_insights


def run_pipeline():

    print("Generating dataset...")

    save_poll_data()

    df = load_data(
        "data/raw/poll_data.csv"
    )

    df = clean_data(df)

    save_cleaned_data(df)

    summary_df = calculate_percentages(df)

    counts = calculate_vote_counts(df)

    region_df = region_analysis(df)

    bar_chart(counts)

    pie_chart(counts)

    region_chart(region_df)

    wordcloud_chart(df)

    generate_insights(summary_df)

    print("Pipeline completed successfully!")


if __name__ == "__main__":

    run_pipeline()