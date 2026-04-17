"""
prediction.py
"""

import joblib
import pandas as pd


def load_objects():

    model = joblib.load(
        "models/performance_model.pkl"
    )

    encoders = joblib.load(
        "models/encoders.pkl"
    )

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    feature_columns = joblib.load(
        "models/feature_columns.pkl"
    )

    return model, encoders, scaler, feature_columns


def predict_employee(data):

    model, encoders, scaler, feature_columns = load_objects()

    df = pd.DataFrame([data])

    # Encode categorical

    categorical_cols = [
        "Gender",
        "Department",
        "Education_Level"
    ]

    for col in categorical_cols:

        df[col] = encoders[col].transform(
            df[col]
        )

    # Scale numerical

    numerical_cols = [
        "Age",
        "Experience_Years",
        "Salary",
        "Training_Hours",
        "Projects_Completed",
        "Overtime_Hours",
        "Absenteeism_Days",
        "Last_Performance_Score"
    ]

    df[numerical_cols] = scaler.transform(
        df[numerical_cols]
    )

   

    df = df[feature_columns]

    prediction = model.predict(df)

    return prediction