# 🛒 Retail Sales Forecasting & Inventory Optimization System

An end-to-end **Retail Analytics & Demand Forecasting Project** that predicts product sales and optimizes inventory levels using Machine Learning and Business Logic.

This project simulates a **real-world retail decision-support system** used by supermarkets, e-commerce companies, and warehouse operations to forecast demand and manage stock efficiently.

---

# 📌 Project Overview

Retail businesses need accurate demand forecasting to avoid:

- ❌ Stockouts (losing customers)
- ❌ Overstock (wasting storage cost)
- ❌ Revenue loss
- ❌ Poor inventory planning

This project builds a **complete pipeline** that:

✔ Generates retail sales data  
✔ Cleans and preprocesses data  
✔ Engineers time-series features  
✔ Trains a Machine Learning forecasting model  
✔ Predicts future demand  
✔ Calculates safety stock  
✔ Generates reorder alerts  
✔ Displays results in an interactive dashboard

---

# 🎯 Problem Statement

Retail stores face uncertainty in customer demand. Without proper forecasting:

- Popular products may run out of stock
- Slow-moving products may accumulate
- Storage costs increase
- Customer satisfaction decreases

This system solves that problem using:

📊 **Demand Forecasting**  
📦 **Inventory Optimization**  
📈 **Business Visualization**

---

# 🏢 Industry Relevance

This system simulates tools used in:

- Supermarkets
- Warehouses
- Retail chains
- E-commerce platforms

Examples:

- Amazon
- Flipkart
- Walmart
- Reliance Retail
- D-Mart

They use similar systems to:

✔ Forecast product demand  
✔ Plan inventory  
✔ Reduce stockouts  
✔ Optimize warehouse operations

---

# 💼 Business Value

This system helps businesses:

- Predict daily product demand
- Calculate safety stock
- Identify reorder points
- Prevent stock shortages
- Optimize storage cost
- Improve customer satisfaction

---

# 🧰 Tech Stack

| Component        | Tool          |
| ---------------- | ------------- |
| Language         | Python        |
| Data Handling    | Pandas, NumPy |
| Visualization    | Matplotlib    |
| Machine Learning | Scikit-learn  |
| Model Storage    | Joblib        |
| Dashboard        | Streamlit     |
| Version Control  | Git & GitHub  |

---

# 🏗️ Project Architecture

Synthetic Retail Data
↓
Data Preprocessing
↓
Feature Engineering
↓
Machine Learning Model
↓
Sales Forecast
↓
Inventory Optimization
↓
Dashboard Visualization

---

# 📂 Folder Structure

├── data/
│ ├── simulated/
│ │ └── synthetic_sales.csv
│ ├── processed/
│ │ └── cleaned_sales.csv
│
├── src/
│ ├── data_generation.py
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── forecasting_model.py
│ ├── inventory_optimizer.py
│ ├── visualization.py
│ ├── model_evaluation.py
│
├── app/
│ └── streamlit_dashboard.py
│
├── outputs/
│ ├── forecasts/
│ │ └── forecast_results.csv
│ ├── inventory/
│ │ └── reorder_recommendations.csv
│ ├── plots/
│
├── models/
│ └── trained_model.pkl
│
├── test_prediction.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

---

# ⚙️ Run the Project

cd Retail-Sales-Forecasting-Inventory-Optimization

pip install -r requirements.txt

python main.py

python test_prediction.py

streamlit run app/streamlit_dashboard.py

# 📊 Sample Outputs

Sales Forecast
Shows:
Actual Sales
Predicted Sales

Inventory Table Example
Product Avg Demand Safety Stock Reorder Point Current Stock Reorder Required
Bread 62 15 325 300 Yes
