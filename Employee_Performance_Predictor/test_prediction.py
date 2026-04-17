from src.prediction import predict_employee

label_map = {
    0: "High",
    1: "Low",
    2: "Medium"
}

# HIGH performer
employee_high = {
    "Employee_ID": 5001,
    "Age": 29,
    "Gender": "Male",
    "Department": "IT",
    "Education_Level": "Masters",
    "Experience_Years": 6,
    "Salary": 65000,
    "Training_Hours": 80,
    "Projects_Completed": 15,
    "Overtime_Hours": 8,
    "Absenteeism_Days": 2,
    "Last_Performance_Score": 5
}

# MEDIUM performer
employee_medium = {
    "Employee_ID": 5002,
    "Age": 34,
    "Gender": "Female",
    "Department": "Sales",
    "Education_Level": "Bachelors",
    "Experience_Years": 8,
    "Salary": 48000,
    "Training_Hours": 35,
    "Projects_Completed": 7,
    "Overtime_Hours": 12,
    "Absenteeism_Days": 6,
    "Last_Performance_Score": 3
}

# LOW performer
employee_low = {
    "Employee_ID": 5003,
    "Age": 41,
    "Gender": "Male",
    "Department": "Finance",
    "Education_Level": "Bachelors",
    "Experience_Years": 2,
    "Salary": 30000,
    "Training_Hours": 10,
    "Projects_Completed": 2,
    "Overtime_Hours": 2,
    "Absenteeism_Days": 15,
    "Last_Performance_Score": 1
}

employees = [
    ("HIGH CASE", employee_high),
    ("MEDIUM CASE", employee_medium),
    ("LOW CASE", employee_low)
]

for case_name, emp in employees:

    pred = predict_employee(emp)

    result = label_map[pred[0]]

    print(f"\n{case_name}")
    print("Prediction:", result)