
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Page Setup
st.set_page_config(
    page_title="Retail Dashboard",
    layout="wide"
)

st.title("🛒 Retail Sales Forecasting Dashboard")

# Load Data
forecast_df = pd.read_csv(
    "outputs/forecasts/forecast_results.csv"
)

inventory_df = pd.read_csv(
    "outputs/inventory/reorder_recommendations.csv"
)

model = joblib.load(
    "models/trained_model.pkl"
)

# Sidebar Product Selection
st.sidebar.header("🔎 Product Filter")

products = forecast_df["product"].unique()

selected_product = st.sidebar.selectbox(
    "Select Product",
    products
)

# Filter Data
product_data = forecast_df[
    forecast_df["product"] == selected_product
]

inventory_data = inventory_df[
    inventory_df["product"] == selected_product
]

# ==============================
# SECTION 1 — INVENTORY STATUS
# ==============================

st.subheader("📦 Inventory Status")

st.dataframe(inventory_data)

if not inventory_data.empty:

    reorder_flag = bool(
        inventory_data[
            "reorder_required"
        ].iloc[0]
    )

    if reorder_flag:

        st.error(
            "⚠ Reorder Required — Stock May Run Out Soon!"
        )

    else:

        st.success(
            "✅ Inventory Level is Safe"
        )

# ==============================
# SECTION 2 — BUSINESS SUMMARY
# ==============================

st.subheader("🧠 Business Summary")

if not product_data.empty:

    avg_sales = product_data[
        "predicted_sales"
    ].mean()

    current_stock = inventory_data[
        "current_stock"
    ].iloc[0]

    st.write(

        f"Expected demand for **{selected_product}** "
        f"is **{round(avg_sales,2)} units per day**."

    )

    # Dynamic demand levels
    if avg_sales < 60:

        st.warning(
            "📉 Low Demand Expected"
        )

    elif avg_sales < 70:

        st.info(
            "📊 Moderate Demand Expected"
        )

    else:

        st.success(
            "🔥 High Demand Expected"
        )

    # Stock comparison
    if current_stock < avg_sales:

        st.error(
            "⚠ Stock may be insufficient."
        )

    else:

        st.success(
            "✅ Stock level is sufficient."
        )

# ==============================
# SECTION 3 — CUSTOM PREDICTION
# ==============================

st.subheader(
    "🧪 Custom Sales Prediction"
)

col1, col2 = st.columns(2)

with col1:

    price = st.number_input(
        "Product Price",
        value=100.0
    )

    stock = st.number_input(
        "Stock Level",
        value=300
    )

    day_of_week = st.slider(
        "Day (0=Mon)",
        0, 6, 2
    )

    month = st.slider(
        "Month",
        1, 12, 6
    )

with col2:

    week_of_year = st.slider(
        "Week of Year",
        1, 52, 24
    )

    is_weekend = st.selectbox(
        "Weekend?",
        [0, 1]
    )

    lag_7 = st.number_input(
        "Sales Last Week",
        value=60
    )

    rolling_mean_7 = st.number_input(
        "7-Day Avg Sales",
        value=65
    )

# Predict Button
if st.button("Predict Sales"):

    input_data = pd.DataFrame({

        "price": [price],
        "stock": [stock],
        "day_of_week": [day_of_week],
        "month": [month],
        "week_of_year": [week_of_year],
        "is_weekend": [is_weekend],
        "lag_7": [lag_7],
        "rolling_mean_7": [rolling_mean_7]

    })

    prediction = model.predict(
        input_data
    )

    predicted_sales = round(
        prediction[0],
        2
    )

    st.success(
        f"📈 Expected Sales: {predicted_sales} units"
    )

    # Business interpretation

    if predicted_sales < 50:

        st.warning(
            "Low demand expected."
        )

    elif predicted_sales < 80:

        st.info(
            "Moderate demand expected."
        )

    else:

        st.success(
            "High demand expected."
        )

    if stock < predicted_sales:

        st.error(
            "⚠ Stock may run out soon!"
        )

    else:

        st.success(
            "✅ Stock level is sufficient."
        )

# ==============================
# SECTION 4 — RECENT DATA
# ==============================

st.subheader(
    "📊 Recent Forecast Data"
)

st.dataframe(
    product_data.tail(20)
)

# ==============================
# SECTION 5 — SALES TREND
# ==============================

st.subheader(
    f"📈 Sales Trend — {selected_product}"
)

fig, ax = plt.subplots()

ax.plot(
    product_data["date"],
    product_data["sales"],
    label="Actual"
)

ax.plot(
    product_data["date"],
    product_data["predicted_sales"],
    label="Predicted"
)

ax.legend()

st.pyplot(fig)
