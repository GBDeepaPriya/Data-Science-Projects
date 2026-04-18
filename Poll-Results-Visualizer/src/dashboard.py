# src/dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Poll Results Dashboard",
    layout="wide"
)

st.title("📊 Poll Results Visualizer Dashboard")

# -----------------------------
# Load Data
# -----------------------------

@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/processed/cleaned_poll_data.csv"
    )
    return df


df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("🔍 Filter Data")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

age_filter = st.sidebar.multiselect(
    "Select Age Group",
    options=df["Age_Group"].unique(),
    default=df["Age_Group"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Apply Filters
filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Age_Group"].isin(age_filter)) &
    (df["Gender"].isin(gender_filter))
]

# -----------------------------
# KPI Metrics
# -----------------------------

st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

total_responses = len(filtered_df)

top_product = (
    filtered_df["Preferred_Product"]
    .value_counts()
    .idxmax()
)

avg_rating = (
    filtered_df["Satisfaction_Rating"]
    .mean()
)

col1.metric(
    "Total Responses",
    total_responses
)

col2.metric(
    "Top Product",
    top_product
)

col3.metric(
    "Average Rating",
    round(avg_rating, 2)
)

# -----------------------------
# Product Preference Chart
# -----------------------------

st.subheader("📊 Product Preference")

product_counts = (
    filtered_df["Preferred_Product"]
    .value_counts()
    .reset_index()
)

product_counts.columns = [
    "Product",
    "Votes"
]

fig_bar = px.bar(
    product_counts,
    x="Product",
    y="Votes",
    color="Product",
    title="Product Preference Distribution"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# -----------------------------
# Region-wise Chart
# -----------------------------

st.subheader("🌍 Region-wise Product Preference")

fig_region = px.histogram(
    filtered_df,
    x="Region",
    color="Preferred_Product",
    barmode="group",
    title="Region-wise Preferences"
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# -----------------------------
# Satisfaction Rating Chart
# -----------------------------

st.subheader("⭐ Satisfaction Rating Distribution")

fig_rating = px.histogram(
    filtered_df,
    x="Satisfaction_Rating",
    nbins=5,
    title="Rating Distribution"
)

st.plotly_chart(
    fig_rating,
    use_container_width=True
)

# -----------------------------
# Pie Chart
# -----------------------------

st.subheader("🥧 Product Share")

fig_pie = px.pie(
    product_counts,
    names="Product",
    values="Votes",
    title="Product Market Share"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# -----------------------------
# Feedback Sample Table
# -----------------------------

st.subheader("💬 Sample Feedback")

sample_feedback = filtered_df[
    ["Preferred_Product", "Feedback"]
].sample(
    min(10, len(filtered_df))
)

st.dataframe(sample_feedback)

# -----------------------------
# Download Filtered Data
# -----------------------------

st.subheader("⬇ Download Filtered Data")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_poll_data.csv",
    mime="text/csv"
)

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.markdown(
    "Built using **Python, Pandas, Plotly, and Streamlit** 🚀"
)