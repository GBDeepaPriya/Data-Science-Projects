"""
data_generation.py

Creates synthetic employee dataset.
"""

import pandas as pd
import numpy as np


def generate_employee_data(num_records=3000):

    np.random.seed(42)

    data = {
        "Employee_ID": np.arange(1, num_records + 1),

        "Age": np.random.randint(22, 60, num_records),

        "Gender": np.random.choice(
            ["Male", "Female"],
            num_records
        ),

        "Department": np.random.choice(
            ["HR", "Sales", "IT", "Finance", "Marketing"],
            num_records
        ),

        "Education_Level": np.random.choice(
            ["Bachelors", "Masters", "PhD"],
            num_records
        ),

        "Experience_Years": np.random.randint(
            0, 30, num_records
        ),

        "Salary": np.random.randint(
            20000, 200000, num_records
        ),

        "Training_Hours": np.random.randint(
            0, 100, num_records
        ),

        "Projects_Completed": np.random.randint(
            0, 20, num_records
        ),

        "Overtime_Hours": np.random.randint(
            0, 50, num_records
        ),

        "Absenteeism_Days": np.random.randint(
            0, 20, num_records
        ),

        "Last_Performance_Score": np.random.randint(
            1, 6, num_records
        )
    }

    df = pd.DataFrame(data)

    # Create Target Variable

    df["Performance_Level"] = np.where(
        (df["Training_Hours"] > 50)
        & (df["Projects_Completed"] > 10)
        & (df["Absenteeism_Days"] < 5),

        "High",

        np.where(
            df["Last_Performance_Score"] >= 3,
            "Medium",
            "Low"
        )
    )

    return df