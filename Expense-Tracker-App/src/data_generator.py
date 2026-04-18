import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Seed for reproducibility
np.random.seed(42)

# Categories
categories = {
    "Food": ["Groceries", "Restaurant", "Snacks"],
    "Transport": ["Fuel", "Bus", "Taxi"],
    "Shopping": ["Clothing", "Electronics", "Accessories"],
    "Bills": ["Electricity", "Water", "Internet"],
    "Entertainment": ["Movies", "Games", "Subscriptions"],
    "Health": ["Medicine", "Doctor"],
    "Education": ["Books", "Courses"],
    "Travel": ["Flights", "Hotel"],
    "Rent": ["House Rent"],
    "Others": ["Misc"]
}

payment_methods = ["Cash", "Card", "UPI"]
locations = ["Online", "Store", "Mall", "Restaurant"]

def random_dates(start, end, n):
    return [
        start + timedelta(
            seconds=random.randint(
                0,
                int((end - start).total_seconds()),
            )
        )
        for _ in range(n)
    ]

def generate_expense_data(n=5000):

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)

    dates = random_dates(start_date, end_date, n)

    data = []

    for i in range(n):

        category = random.choice(list(categories.keys()))
        sub_category = random.choice(categories[category])

        # Spending logic
        if category == "Rent":
            amount = np.random.uniform(5000, 20000)
        elif category == "Travel":
            amount = np.random.uniform(2000, 15000)
        else:
            amount = np.random.uniform(50, 5000)

        record = {

            "user_id":
                random.randint(1001, 1020),

            "date":
                dates[i],

            "category":
                category,

            "sub_category":
                sub_category,

            "amount":
                round(amount, 2),

            "payment_method":
                random.choice(payment_methods),

            "location":
                random.choice(locations),

            "income":
                random.choice(
                    [30000, 40000, 50000, 60000]
                ),

            "budget":
                random.choice(
                    [20000, 25000, 30000]
                )

        }

        data.append(record)

    df = pd.DataFrame(data)

    df.to_csv(
        "data/raw_expense_data.csv",
        index=False
    )

    print("Dataset Generated Successfully!")

if __name__ == "__main__":
    generate_expense_data()