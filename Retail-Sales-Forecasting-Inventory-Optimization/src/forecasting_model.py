"""
File: forecasting_model.py

Purpose:
Train forecasting model
and generate demand predictions.
"""

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def train_forecasting_model():

    file_path = "data/processed/featured_sales.csv"

    df = pd.read_csv(file_path)

    print("Dataset Loaded:", df.shape)

    # Select features
    features = [
        "price",
        "stock",
        "day_of_week",
        "month",
        "week_of_year",
        "is_weekend",
        "lag_7",
        "rolling_mean_7"
    ]

    target = "sales"

    X = df[features]
    y = df[target]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training Model...")

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    print("Model MAE:", mae)

    # Save model
    os.makedirs("models", exist_ok=True)

    model_path = "models/trained_model.pkl"

    joblib.dump(
        model,
        model_path
    )

    print("Model saved:", model_path)

    return model


def generate_forecast():

    model_path = "models/trained_model.pkl"

    model = joblib.load(model_path)

    df = pd.read_csv(
        "data/processed/featured_sales.csv"
    )

    features = [
        "price",
        "stock",
        "day_of_week",
        "month",
        "week_of_year",
        "is_weekend",
        "lag_7",
        "rolling_mean_7"
    ]

    X = df[features]

    print("Generating Forecast...")

    df["predicted_sales"] = model.predict(X)

    os.makedirs(
        "outputs/forecasts",
        exist_ok=True
    )

    output_path = "outputs/forecasts/forecast_results.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("Forecast saved:", output_path)

    return df


if __name__ == "__main__":

    train_forecasting_model()

    generate_forecast()