"""
File: data_generation.py

Purpose:
Generate synthetic retail sales dataset
to simulate real retail store behavior.
"""

import pandas as pd
import numpy as np
import os

def generate_synthetic_data():

    np.random.seed(42)

    # Create date range
    dates = pd.date_range(
        start="2022-01-01",
        end="2023-12-31",
        freq="D"
    )

    # Products list
    products = [
        "Milk",
        "Bread",
        "Rice",
        "Eggs",
        "Soap",
        "Shampoo"
    ]

    # Categories
    categories = {
        "Milk": "Dairy",
        "Bread": "Bakery",
        "Rice": "Grocery",
        "Eggs": "Dairy",
        "Soap": "Personal Care",
        "Shampoo": "Personal Care"
    }

    data = []

    for date in dates:

        for product in products:

            # Weekly seasonality
            weekday = date.weekday()

            if weekday >= 5:
                base_sales = np.random.randint(80, 120)
            else:
                base_sales = np.random.randint(50, 80)

            # Monthly seasonality
            if date.month in [11, 12]:
                base_sales += np.random.randint(20, 40)

            # Random noise
            sales = max(
                0,
                base_sales + np.random.randint(-10, 10)
            )

            # Price simulation
            price = np.random.uniform(10, 200)

            # Stock level simulation
            stock = np.random.randint(200, 500)

            data.append([
                date,
                product,
                categories[product],
                sales,
                price,
                stock
            ])

    df = pd.DataFrame(
        data,
        columns=[
            "date",
            "product",
            "category",
            "sales",
            "price",
            "stock"
        ]
    )

    # Create directory
    os.makedirs(
        "data/simulated",
        exist_ok=True
    )

    file_path = "data/simulated/synthetic_sales.csv"

    df.to_csv(
        file_path,
        index=False
    )

    print("Synthetic dataset created:")
    print(file_path)

    return df


if __name__ == "__main__":
    generate_synthetic_data()