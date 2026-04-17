# Employee Performance Predictor using Data Analytics

## 📌 Project Overview

Employee Performance Predictor is a Machine Learning-based HR Analytics system designed to predict employee performance levels using structured employee data.

This project simulates a real-world HR analytics workflow using synthetic employee datasets and predictive modeling techniques.

The system helps organizations:

- Identify high-performing employees
- Detect low-performing employees early
- Support data-driven HR decisions
- Improve workforce productivity

---

## 🎯 Problem Statement

Organizations often rely on manual evaluations to assess employee performance. This approach may lead to:

- Subjective decision-making
- Delayed identification of weak performers
- Inefficient training allocation
- Unfair promotion decisions

This project builds a predictive analytics system that classifies employees into performance levels based on their attributes such as training hours, projects completed, experience, and absenteeism.

---

## 💼 Business Value

This system provides practical value for:

### HR Teams

- Identify top-performing employees
- Detect employees needing support
- Optimize training investments

### Managers

- Make promotion decisions using data
- Improve team productivity
- Allocate resources effectively

### Business Leaders

- Enhance workforce planning
- Reduce performance risk
- Improve organizational efficiency

---

## 🛠️ Tech Stack

Programming Language:

- Python

Libraries Used:

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

Machine Learning Model:

- Random Forest Classifier

Development Tools:

- VS Code / Jupyter Notebook
- GitHub

---

## 🧠 Machine Learning Approach

This project solves a:

**Supervised Machine Learning Classification Problem**

Target Variable:

```text
Performance_Level
```

Classes:

```text
High
Medium
Low
```

Model Used:

```text
Random Forest Classifier
```

Reason for Selection:

- Handles structured data effectively
- Reduces overfitting
- Provides feature importance insights

---

## 🏗️ Project Architecture

```text
Employee Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Performance Prediction
        │
        ▼
HR Insights Generation
```

---

## 📂 Project Structure

```text
Employee-Performance-Predictor/

├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│
├── src/
│   ├── data_generation.py
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   ├── prediction.py
│
├── models/
│
├── outputs/
│
├── images/
│
├── main.py
├── requirements.txt
├── README.md
```

---

## 📊 Dataset Description

Synthetic employee dataset includes:

| Feature                | Description          |
| ---------------------- | -------------------- |
| Age                    | Employee age         |
| Gender                 | Male/Female          |
| Department             | Employee department  |
| Education_Level        | Education background |
| Experience_Years       | Work experience      |
| Salary                 | Annual salary        |
| Training_Hours         | Training attended    |
| Projects_Completed     | Completed projects   |
| Overtime_Hours         | Overtime worked      |
| Absenteeism_Days       | Leave days           |
| Last_Performance_Score | Previous rating      |

Target:

```text
Performance_Level
```

---

## 🚀 How To Run This Project

### Navigate to Folder

```bash
cd Employee-Performance-Predictor-ML
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Project

```bash
python main.py
```
### Streamlit dashboard

```bash
streamlit run app.py
```
---

## 📈 Output Results

After execution, system generates:

```text
data/raw/employee_data.csv
data/processed/cleaned_data.csv

models/performance_model.pkl

images/
├── performance_distribution.png
├── correlation_heatmap.png
├── confusion_matrix.png
├── feature_importance.png

outputs/
├── metrics.txt
├── predictions.csv
```
<img width="748" height="888" alt="image" src="https://github.com/user-attachments/assets/b11e0519-a259-4d16-a033-4683de1318bf" />
<img width="748" height="888" alt="Output" src="https://github.com/user-attachments/assets/e106fdb3-c36f-410f-bda1-b20d3d40a7d6" />
<img width="800" height="600" alt="confusion_matrix" src="https://github.com/user-attachments/assets/018f1f8b-c3ac-4881-823c-2bd10d55d8ec" />
<img width="3553" height="2352" alt="feature_importance" src="https://github.com/user-attachments/assets/15898451-b0b4-481b-85f5-1d7c98e5c2cd" />
<img width="800" height="600" alt="performance_distribution" src="https://github.com/user-attachments/assets/46b5c08a-1896-46a4-b46a-577b0697d426" />
<img width="1000" height="800" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/d9baf51d-a256-49e9-8405-0fac7e5a8f71" />


---

## 📊 Sample Model Performance

Typical Accuracy:

```text
Accuracy: 0.88 – 0.99
```

Metrics Generated:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## 📸 Screenshots

Add these images here:

- Dataset Preview
- Performance Distribution
- Correlation Heatmap
- Confusion Matrix
- Feature Importance

---

## 📉 Business Insights Generated

Example insights:

- Employees with higher training hours perform better
- Higher absenteeism negatively affects performance
- Project completion strongly influences performance

These insights help organizations:

- Plan employee training
- Improve productivity
- Identify promotion candidates

---

## 👨‍💻 Author
G B Deepika
---
