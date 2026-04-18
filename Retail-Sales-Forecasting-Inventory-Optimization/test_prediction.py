import pandas as pd
import joblib

print("\n==============================")
print(" RETAIL SALES PREDICTION TEST ")
print("==============================\n")

# Load model
model = joblib.load(
    "models/trained_model.pkl"
)

print("✅ Model Loaded Successfully\n")

# Sample Business Scenario
test_data = pd.DataFrame({

    "price": [120.5],
    "stock": [350],
    "day_of_week": [2],   # Wednesday
    "month": [6],         # June
    "week_of_year": [24],
    "is_weekend": [0],
    "lag_7": [65],
    "rolling_mean_7": [70]

})

print("📦 BUSINESS SCENARIO")
print("--------------------")

print("Product Price      : ₹120.5")
print("Current Stock      : 350 units")
print("Day                : Wednesday")
print("Month              : June")
print("Sales Last Week    : 65 units")
print("7-Day Avg Sales    : 70 units")

print("\n🔍 Running Prediction...\n")

# Predict
prediction = model.predict(test_data)

predicted_sales = round(prediction[0], 2)

print("📈 PREDICTION RESULT")
print("--------------------")

print(
    f"Expected Sales Tomorrow: {predicted_sales} units"
)

# Business Interpretation
print("\n🧠 BUSINESS INTERPRETATION")
print("---------------------------")

if predicted_sales < 50:

    print(
        "Low demand expected."
    )
    print(
        "No urgent restocking required."
    )

elif predicted_sales < 80:

    print(
        "Moderate demand expected."
    )
    print(
        "Maintain regular inventory level."
    )

else:

    print(
        "High demand expected!"
    )
    print(
        "Consider increasing stock levels."
    )

# Stock Safety Check
print("\n📦 STOCK CHECK")
print("----------------")

current_stock = 350

if current_stock < predicted_sales:

    print(
        "⚠ WARNING: Stock may run out soon!"
    )

else:

    print(
        "✅ Stock level is sufficient."
    )

print("\n✅ Test Prediction Completed Successfully\n")