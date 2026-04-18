# 🌍 Climate Trend Analyzer

## 📌 Project Overview

Climate Trend Analyzer is a data science project designed to analyze historical climate data and uncover meaningful environmental trends. The system performs trend detection, anomaly identification, and climate forecasting using statistical and machine learning techniques.

This project simulates real-world climate analytics workflows used by environmental agencies, researchers, and policy makers.

---

## 🎯 Problem Statement

Climate datasets contain valuable information about temperature, rainfall, CO₂ levels, and sea level changes. However, identifying long-term trends and anomalies manually is difficult.

This project automates:

- Climate trend analysis
- Seasonal pattern detection
- Anomaly detection
- Future forecasting

---

## 🌎 Industry Relevance

Climate analytics is used by:

- Environmental agencies
- Smart city planners
- Agriculture sector
- Disaster management teams
- Climate-tech companies

---

## 🧰 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Streamlit

---

## 🏗️ Project Architecture

Raw Data
↓
Data Cleaning
↓
EDA
↓
Feature Engineering
↓
Trend Analysis
↓
Anomaly Detection
↓
Forecasting
↓
Visualization Dashboard

---

## 📂 Folder Structure

```text
Climate-Trend-Analyzer/

├── data/
│   ├── raw/
│   │   └── climate_data.csv
│   
│
├── src/
│   ├── data_generator.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── trend_analysis.py
│   ├── anomaly_detection.py
│   ├── forecasting.py
│   ├── insight_generation.py
│   ├── report_generator.py
│   ├── seasonal_analysis.py
│   ├── visualization.py
|
├── app/
│   └── streamlit_app.py
│
├── outputs/
│   ├── plots/
│   └── reports/
│
│
├── main.py
├── requirements.txt
├── README.md

```

# ⚙️ Installation Guide

pip install -r requirements.txt

## Dataset Generation

python src/data_generator.py

## Run Main Pipeline

python main.py

## Run Streamlit Dashboard

streamlit run app/streamlit_app.py

# 📊 Sample Outputs
<img width="1802" height="792" alt="Dashboard 1" src="https://github.com/user-attachments/assets/e502c0e1-a9ff-4a13-a55a-0b8ed0761e80" />
<img width="1842" height="748" alt="Dashboard 2" src="https://github.com/user-attachments/assets/7bf451e3-e1c4-43be-a8eb-75566547ebb5" />
<img width="1297" height="850" alt="output" src="https://github.com/user-attachments/assets/77cd6c7e-e1ed-4717-ab8f-50450151126d" />
<img width="1200" height="600" alt="temperature_forecast" src="https://github.com/user-attachments/assets/0669dee9-3462-47a0-bdc3-a3cf39c2fc06" />
<img width="1200" height="600" alt="temperature_anomalies" src="https://github.com/user-attachments/assets/0847c3fc-5929-42ad-b447-e3bc8f729b3f" />
<img width="1200" height="600" alt="temperature_moving_average" src="https://github.com/user-attachments/assets/3bab532e-91b1-4ec6-90d5-f3f2d5fb6980" />

