"""
feature_engineering.py
"""

import joblib

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


def encode_features(df):

    encoders = {}

    categorical_cols = [
        "Gender",
        "Department",
        "Education_Level",
        "Performance_Level"
    ]

    for col in categorical_cols:

        le = LabelEncoder()

        df[col] = le.fit_transform(df[col])

        encoders[col] = le

    # Save encoders
    joblib.dump(
        encoders,
        "models/encoders.pkl"
    )

    return df


def scale_features(df):

    scaler = StandardScaler()

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

    df[numerical_cols] = scaler.fit_transform(
        df[numerical_cols]
    )

    # Save scaler
    joblib.dump(
        scaler,
        "models/scaler.pkl"
    )

    return df