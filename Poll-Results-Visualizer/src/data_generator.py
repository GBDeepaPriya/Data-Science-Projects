# src/data_generator.py

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def generate_poll_data(num_records=1000):

    np.random.seed(42)

    # Categories
    age_groups = ["18-24", "25-34", "35-44", "45+"]
    genders = ["Male", "Female", "Other"]
    regions = ["North", "South", "East", "West"]

    products = [
        "Product A",
        "Product B",
        "Product C",
        "Product D"
    ]

    feedback_options = [
        "Excellent product",
        "Very useful",
        "Needs improvement",
        "Good value",
        "Not satisfied",
        "Highly recommended",
        "Average experience"
    ]

    data = []

    start_date = datetime(2024, 1, 1)

    for i in range(num_records):

        timestamp = start_date + timedelta(
            days=random.randint(0, 90),
            minutes=random.randint(0, 1440)
        )

        record = {

            "Respondent_ID": i + 1,

            "Timestamp": timestamp,

            "Age_Group": random.choice(age_groups),

            "Gender": random.choice(genders),

            "Region": random.choice(regions),

            "Preferred_Product": random.choice(products),

            "Satisfaction_Rating": random.randint(1, 5),

            "Feedback": random.choice(feedback_options)
        }

        data.append(record)

    df = pd.DataFrame(data)

    return df


def save_poll_data():

    df = generate_poll_data()

    output_path = "data/raw/poll_data.csv"

    df.to_csv(output_path, index=False)

    print(f"Dataset saved at {output_path}")


if __name__ == "__main__":
    save_poll_data()