import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="Expense Tracker Dashboard",
    layout="wide"
)

st.title("💰 Expense Tracker Dashboard")

# ------------------------------
# LOAD DATA
# ------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )
    return df

df = load_data()

# ------------------------------
# SIDEBAR FILTERS
# ------------------------------

st.sidebar.header("🔎 Filters")

# Year Filter
years = sorted(df["year"].unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

# Month Filter
months = sorted(df["month"].unique())

selected_month = st.sidebar.multiselect(
    "Select Month",
    months,
    default=months
)

# Category Filter
categories = df["category"].unique()

selected_category = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)

# ------------------------------
# APPLY FILTERS
# ------------------------------

filtered_df = df[
    (df["year"].isin(selected_year)) &
    (df["month"].isin(selected_month)) &
    (df["category"].isin(selected_category))
]

# ------------------------------
# KPI METRICS
# ------------------------------

total_spending = filtered_df["amount"].sum()
avg_spending = filtered_df["amount"].mean()

# Overspending Logic
overspending = filtered_df[
    filtered_df["amount"] >
    filtered_df["budget"]
]

overspending_count = len(overspending)

col1, col2, col3 = st.columns(3)

col1.metric(
    "💵 Total Spending",
    f"₹{total_spending:,.0f}"
)

col2.metric(
    "📊 Average Spending",
    f"₹{avg_spending:,.0f}"
)

col3.metric(
    "⚠ Overspending Instances",
    overspending_count
)

st.markdown("---")

# ------------------------------
# CATEGORY BAR CHART
# ------------------------------

category_total = (
    filtered_df
    .groupby("category")["amount"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_total,
    x="category",
    y="amount",
    color="category",
    title="📊 Category-wise Spending"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ------------------------------
# MONTHLY TREND LINE CHART
# ------------------------------

monthly_total = (
    filtered_df
    .groupby(["year", "month"])["amount"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    monthly_total,
    x="month",
    y="amount",
    color="year",
    markers=True,
    title="📈 Monthly Spending Trend"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------
# PIE CHART
# ------------------------------

fig3 = px.pie(
    category_total,
    names="category",
    values="amount",
    title="🥧 Expense Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ------------------------------
# WEEKDAY ANALYSIS
# ------------------------------

weekday_total = (
    filtered_df
    .groupby("weekday")["amount"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    weekday_total,
    x="weekday",
    y="amount",
    title="📅 Weekday Spending Pattern"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ------------------------------
# SHOW FILTERED DATA TABLE
# ------------------------------

st.markdown("### 📄 Filtered Expense Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ------------------------------
# DOWNLOAD BUTTON
# ------------------------------

csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="filtered_expense_data.csv",
    mime="text/csv"
)

# ------------------------------
# FOOTER
# ------------------------------

st.markdown("---")

st.caption(
    "Built using Streamlit | Expense Tracker Data Science Project"
)