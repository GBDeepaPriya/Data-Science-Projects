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

# 📂 Project Folder Structure

Retail-Sales-Forecasting-Inventory-Optimization/

# 📂 Project Folder Structure

Retail-Sales-Forecasting-Inventory-Optimization/

├── data/  
│   ├── simulated/  
│   │   └── synthetic_sales.csv        # Generated synthetic retail dataset  
│   ├── processed/  
│   │   └── cleaned_sales.csv          # Cleaned and preprocessed dataset  
│
├── src/  
│   ├── data_generation.py             # Synthetic data creation  
│   ├── data_preprocessing.py          # Data cleaning and formatting  
│   ├── feature_engineering.py         # Feature creation for model  
│   ├── forecasting_model.py           # Machine learning model training  
│   ├── inventory_optimizer.py         # Inventory optimization logic  
│   ├── visualization.py               # Graph generation  
│   ├── model_evaluation.py            # Model performance evaluation  
│
├── app/  
│   └── streamlit_dashboard.py         # Interactive Streamlit dashboard  
│
├── outputs/  
│   ├── forecasts/  
│   │   └── forecast_results.csv       # Predicted sales output  
│   ├── inventory/  
│   │   └── reorder_recommendations.csv # Inventory decisions  
│   ├── plots/                         # Generated visualizations  
│
├── models/  
│   └── trained_model.pkl              # Saved trained model  
│
│
├── test_prediction.py                # Model testing script  
├── main.py                           # Main pipeline execution file  
├── requirements.txt                  # Project dependencies  
├── .gitignore                        # Ignore unnecessary files  
└── README.md                         # Project documentation                       
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
<img width="1842" height="822" alt="Dashboard1" src="https://github.com/user-attachments/assets/d23d2415-4541-4916-8e74-b030e6fc86c6" />
<img width="1821" height="837" alt="Dashboard2" src="https://github.com/user-attachments/assets/55282717-0b5a-4ce7-86c7-554eff9d51bd" />
<img width="640" height="480" alt="category_sales" src="https://github.com/user-attachments/assets/9572f2ae-4bf4-4661-949a-768908d9b853" />
<img width="640" height="480" alt="sales_trend" src="https://github.com/user-attachments/assets/67d426ff-0f8a-46cd-8558-abf805719859" />
<img width="1346" height="935" alt="output" src="https://github.com/user-attachments/assets/4b6edfc7-26dd-4ca4-9389-91ee048f80a4" />






