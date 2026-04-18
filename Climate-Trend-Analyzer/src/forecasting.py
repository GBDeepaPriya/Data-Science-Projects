# src/forecasting.py

import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA


def arima_forecast(
    df,
    column,
    steps=365
):
    """
    Forecast future values using ARIMA.
    """

    # Make copy (safe practice)
    df_copy = df.copy()

    # Set index
    df_copy = df_copy.set_index("date")

    # IMPORTANT: Set frequency to Daily
    df_copy = df_copy.asfreq("D")

    # Fill any missing values
    df_copy[column] = df_copy[column].ffill()

    print(f"\nRunning ARIMA Forecast for {column}...")

    # Build model
    model = ARIMA(
        df_copy[column],
        order=(5, 1, 0)
    )

    model_fit = model.fit()

    # Forecast future values
    forecast = model_fit.forecast(
        steps=steps
    )

    # Create future dates
    forecast_index = pd.date_range(
        start=df_copy.index[-1] + pd.Timedelta(days=1),
        periods=steps,
        freq="D"
    )

    # Create forecast dataframe
    forecast_df = pd.DataFrame({
        "date": forecast_index,
        "forecast": forecast.values
    })

    print("Forecast completed successfully!")

    return forecast_df


def plot_forecast(
    df,
    forecast_df,
    column
):
    """
    Plot forecast results.
    """

    plt.figure(figsize=(12, 6))

    # Historical data
    plt.plot(
        df["date"],
        df[column],
        label="Historical Data"
    )

    # Forecast data
    plt.plot(
        forecast_df["date"],
        forecast_df["forecast"],
        label="Forecast",
        linewidth=2
    )

    plt.xlabel("Date")

    plt.ylabel(column)

    plt.title(
        f"{column.capitalize()} Forecast"
    )

    plt.legend()

    plt.grid(True)

    # Save plot
    file_path = f"outputs/plots/{column}_forecast.png"

    plt.savefig(file_path)

    print(f"Forecast plot saved to: {file_path}")

    plt.close()