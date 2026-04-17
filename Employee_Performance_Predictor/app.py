# app.py

import streamlit as st
import joblib
import pandas as pd

from src.prediction import predict_employee


# Page Config
st.set_page_config(
    page_title="Employee Performance Predictor",
    layout="centered"
)

st.title("📊 Employee Performance Predictor")
st.markdown("Predict employee performance using Machine Learning.")


# ------------------------------
# INPUT SECTION
# ------------------------------

st.subheader("Enter Employee Details")


# Dropdown Inputs

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

department = st.selectbox(
    "Department",
    ["IT", "HR", "Finance", "Sales"]
)

education = st.selectbox(
    "Education Level",
    ["Bachelors", "Masters", "PhD"]
)


# Numeric Inputs

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30
)

experience = st.number_input(
    "Experience Years",
    min_value=0,
    max_value=40,
    value=5
)

salary = st.number_input(
    "Salary",
    min_value=20000,
    max_value=150000,
    value=50000
)

training_hours = st.number_input(
    "Training Hours",
    min_value=0,
    max_value=200,
    value=40
)

projects = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=50,
    value=8
)

overtime = st.number_input(
    "Overtime Hours",
    min_value=0,
    max_value=50,
    value=5
)

absenteeism = st.number_input(
    "Absenteeism Days",
    min_value=0,
    max_value=30,
    value=3
)

last_score = st.number_input(
    "Last Performance Score",
    min_value=1,
    max_value=5,
    value=3
)


# ------------------------------
# PREDICTION BUTTON
# ------------------------------

if st.button("Predict Performance"):

    employee = {
        "Employee_ID": 9999,
        "Age": age,
        "Gender": gender,
        "Department": department,
        "Education_Level": education,
        "Experience_Years": experience,
        "Salary": salary,
        "Training_Hours": training_hours,
        "Projects_Completed": projects,
        "Overtime_Hours": overtime,
        "Absenteeism_Days": absenteeism,
        "Last_Performance_Score": last_score
    }

    prediction = predict_employee(employee)

    # Load label mapping

    encoders = joblib.load("models/encoders.pkl")

    le = encoders["Performance_Level"]

    label_map = {
        i: label
        for i, label in enumerate(le.classes_)
    }

    result = label_map[prediction[0]]

    st.divider()

    st.subheader("Prediction Result")

    if result == "High":

        st.success("High Performer ⭐")

    elif result == "Medium":

        st.warning("Medium Performer ⚠️")

    else:

        st.error("Low Performer ❌")