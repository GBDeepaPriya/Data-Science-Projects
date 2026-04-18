import pandas as pd
import numpy as np
import os


def calculate_inventory():

    print("Calculating Inventory Optimization...")

    df = pd.read_csv(
        "outputs/forecasts/forecast_results.csv"
    )

    # Realistic parameters
    lead_time = 5      # days
    z = 1.28           # 90% service level

    results = []

    for product, group in df.groupby("product"):

        # Average predicted demand
        avg = group["predicted_sales"].mean()

        # Demand variability
        std = group["predicted_sales"].std()

        # Safety Stock Formula
        safety_stock = z * std * np.sqrt(lead_time)

        # Reorder Point Formula
        reorder_point = (
            (avg * lead_time)
            + safety_stock
        )

        # Create realistic stock levels
        current_stock = np.random.randint(
            int(avg * 3),
            int(avg * 8)
        )

        # Reorder decision
        reorder_required = (
            current_stock <= reorder_point
        )

        results.append([

            product,
            round(avg, 2),
            round(safety_stock, 2),
            round(reorder_point, 2),
            current_stock,
            reorder_required

        ])

    inventory_df = pd.DataFrame(

        results,

        columns=[

            "product",
            "avg_demand",
            "safety_stock",
            "reorder_point",
            "current_stock",
            "reorder_required"

        ]

    )

    os.makedirs(
        "outputs/inventory",
        exist_ok=True
    )

    inventory_df.to_csv(

        "outputs/inventory/reorder_recommendations.csv",
        index=False

    )

    print("Inventory recommendations saved.")

    return inventory_df