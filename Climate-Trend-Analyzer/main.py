# main.py

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.report_generator import generate_report

from src.trend_analysis import (
    moving_average_trend,
    plot_trend_with_moving_average
)

from src.anomaly_detection import (
    zscore_anomaly_detection,
    plot_anomalies
)

from src.forecasting import (
    arima_forecast,
    plot_forecast
)

from src.insight_generation import (
    generate_summary,
    print_summary
)


def main():

    # Load Data
    df = load_data()

    # Preprocess
    df = preprocess_data(df)

    # Feature Engineering
    df = create_features(df)

    # Trend Analysis
    df = moving_average_trend(
        df,
        "temperature"
    )

    plot_trend_with_moving_average(
        df,
        "temperature"
    )

    # Anomaly Detection
    df = zscore_anomaly_detection(
        df,
        "temperature"
    )

    plot_anomalies(
        df,
        "temperature"
    )

    # Forecasting
    forecast_df = arima_forecast(
        df,
        "temperature"
    )

    plot_forecast(
        df,
        forecast_df,
        "temperature"
    )

    # Insights
    summary = generate_summary(df)

    print_summary(summary)
    generate_report(summary)

    
if __name__ == "__main__":

    main()