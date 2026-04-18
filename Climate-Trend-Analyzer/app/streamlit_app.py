# app/streamlit_app.py

import sys
import os

# Fix import path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features

from src.trend_analysis import moving_average_trend
from src.anomaly_detection import zscore_anomaly_detection
from src.forecasting import arima_forecast

# Page Config
st.set_page_config(
    page_title="Climate Trend Analyzer",
    layout="wide"
)

st.title("🌍 Climate Trend Analyzer Dashboard")

st.markdown(
    "Interactive Climate Analytics Dashboard "
    "for Trend, Anomaly Detection, and Forecasting"
)


# Load Data
@st.cache_data
def load_pipeline():

    df = load_data()

    df = preprocess_data(df)

    df = create_features(df)

    return df


df = load_pipeline()


# Sidebar Controls
st.sidebar.header("⚙️ Dashboard Controls")

parameter = st.sidebar.selectbox(
    "Select Climate Parameter",
    [
        "temperature",
        "rainfall",
        "humidity",
        "co2",
        "sea_level"
    ]
)

analysis_type = st.sidebar.selectbox(
    "Select Analysis Type",
    [
        "Trend",
        "Anomaly",
        "Forecast"
    ]
)


# Date Filter
st.sidebar.subheader("📅 Date Filter")

start_date = st.sidebar.date_input(
    "Start Date",
    df["date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["date"].max()
)

# Apply Filter
filtered_df = df[
    (df["date"] >= pd.to_datetime(start_date)) &
    (df["date"] <= pd.to_datetime(end_date))
]


# Dataset Preview
st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df.head(10),
    use_container_width=True
)


# Summary Metrics
st.subheader("📊 Climate Summary Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Temperature",
    round(filtered_df["temperature"].mean(), 2)
)

col2.metric(
    "Total Rainfall",
    round(filtered_df["rainfall"].sum(), 2)
)

col3.metric(
    "Avg CO₂",
    round(filtered_df["co2"].mean(), 2)
)

col4.metric(
    "Max Sea Level",
    round(filtered_df["sea_level"].max(), 2)
)


# TREND ANALYSIS
if analysis_type == "Trend":

    st.subheader(f"📈 {parameter.capitalize()} Trend Analysis")

    filtered_df = moving_average_trend(
        filtered_df,
        parameter
    )

    fig = px.line(
        filtered_df,
        x="date",
        y=[parameter, f"{parameter}_ma"],
        title=f"{parameter.capitalize()} Trend with Moving Average"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ANOMALY DETECTION
elif analysis_type == "Anomaly":

    st.subheader(f"🚨 {parameter.capitalize()} Anomaly Detection")

    filtered_df = zscore_anomaly_detection(
        filtered_df,
        parameter
    )

    anomalies = filtered_df[
        filtered_df["anomaly"]
    ]

    fig = px.line(
        filtered_df,
        x="date",
        y=parameter,
        title=f"{parameter.capitalize()} Anomaly Detection"
    )

    fig.add_scatter(
        x=anomalies["date"],
        y=anomalies[parameter],
        mode="markers",
        name="Anomalies"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.write("### Detected Anomalies")

    st.dataframe(
        anomalies.head(20),
        use_container_width=True
    )


# FORECASTING
elif analysis_type == "Forecast":

    st.subheader(f"🔮 {parameter.capitalize()} Forecast")

    forecast_df = arima_forecast(
        filtered_df,
        parameter
    )

    fig = px.line(
        forecast_df,
        x="date",
        y="forecast",
        title=f"{parameter.capitalize()} Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Download Forecast
    csv = forecast_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Forecast CSV",
        data=csv,
        file_name=f"{parameter}_forecast.csv",
        mime="text/csv"
    )


# Seasonal Analysis
st.subheader("🌦️ Seasonal Distribution")

fig = px.box(
    filtered_df,
    x="season",
    y=parameter,
    title=f"{parameter.capitalize()} Seasonal Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# Multi-Variable Comparison
st.subheader("📊 Multi-Parameter Comparison")

multi_fig = px.line(
    filtered_df,
    x="date",
    y=[
        "temperature",
        "rainfall",
        "co2"
    ],
    title="Temperature vs Rainfall vs CO₂"
)

st.plotly_chart(
    multi_fig,
    use_container_width=True
)


