import pandas as pd
import numpy as np


def generate_climate_data(
    start_date="1995-01-01",
    end_date="2025-12-31",
    save_path="data/raw/climate_data.csv"
):

    # Create date range
    dates = pd.date_range(start=start_date, end=end_date)

    n = len(dates)

    np.random.seed(42)

    # Convert dayofyear to numpy array
    day_of_year = dates.dayofyear.values

    # Temperature
    temperature = (
        25
        + 10 * np.sin(2 * np.pi * day_of_year / 365)
        + np.linspace(0, 2, n)
        + np.random.normal(0, 2, n)
    )

    # Rainfall
    rainfall = (
        50
        + 40 * np.sin(2 * np.pi * day_of_year / 365)
        + np.random.normal(0, 10, n)
    )

    rainfall = np.clip(rainfall, 0, None)

    # Humidity
    humidity = (
        60
        + 20 * np.sin(2 * np.pi * day_of_year / 365)
        + np.random.normal(0, 5, n)
    )

    # CO2 trend
    co2 = (
        350
        + np.linspace(0, 80, n)
        + np.random.normal(0, 2, n)
    )

    # Sea level trend
    sea_level = (
        np.linspace(0, 120, n)
        + np.random.normal(0, 3, n)
    )

    # Add anomalies
    anomaly_indices = np.random.choice(n, size=50)

    temperature[anomaly_indices] += np.random.uniform(5, 10, size=50)

    rainfall[anomaly_indices] += np.random.uniform(50, 100, size=50)

    # Create DataFrame
    df = pd.DataFrame({
        "date": dates,
        "temperature": temperature,
        "rainfall": rainfall,
        "humidity": humidity,
        "co2": co2,
        "sea_level": sea_level
    })

    # Save dataset
    df.to_csv(save_path, index=False)

    print("Dataset Generated Successfully!")
    print("Saved to:", save_path)

    return df


if __name__ == "__main__":
    generate_climate_data()