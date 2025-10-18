import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ───────────────────────────────────────────────
# Page Setup
# ───────────────────────────────────────────────
st.set_page_config(page_title="Executive KPI Dashboard", page_icon="📊", layout="wide")

# Global dark style
st.markdown(
    """
    <style>
        body {background-color: #0e1117; color: white;}
        .block-container {padding-top: 1rem;}
        div[data-testid="stMetricValue"] {font-size: 2rem;}
        div[data-testid="stMetricLabel"] {color: #bbb;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📊 Executive Performance Dashboard")
st.caption("Dark theme KPI view for revenue, partners, and hiring metrics.")

# ───────────────────────────────────────────────
# Fake Data (Demo)
# ───────────────────────────────────────────────
weeks = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [1000000, 1600000, 1900000, 2200000, 2400000]
restaurants = [120, 220, 360, 520, 606]
new_hires = [5, 14, 21, 30, 36]

# ───────────────────────────────────────────────
# KPI 1 — Revenue Card
# ───────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💰 Earn 5M in new revenue")
    st.metric(label="This Year", value="2.4 M SGD", delta="+450 K SGD")
    st.progress(int(2400000 / 5000000 * 100))

    # Revenue by week bar chart
    fig, ax = plt.subplots(figsize=(3.5, 2))
    ax.bar(weeks, revenue, color="#33C3F0")
    ax.set_facecolor("#0e1117")
    ax.tick_params(colors="white")
    ax.set_title("by month", color="white", fontsize=10)
    st.pyplot(fig)

    # Gauge: average revenue per restaurant
    fig, ax = plt.subplots(figsize=(3, 1.5), subplot_kw={'projection': 'polar'})
    value = 789
    max_val = 1000
    theta = np.pi * (1 - value / max_val)
    ax.barh(0, np.pi - theta, color="#33C3F0")
    ax.set_theta_zero_location('W')
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_facecolor("#0e1117")
    plt.text(0, 0, f"{value} SGD", color="white", ha="center", va="center", fontsize=12)
    st.pyplot(fig)

# ───────────────────────────────────────────────
# KPI 2 — Restaurants Card
# ───────────────────────────────────────────────
with col2:
    st.subheader("🏪 Acquire 1000 partner restaurants")
    st.metric(label="New restaurants", value="606", delta="+86")
    st.progress(int(606 / 1000 * 100))

    region_data = {
        "Central Region": 245,
        "North-East Region": 123,
        "North Region": 102,
        "East Region": 88,
        "West Region": 48,
    }
    st.markdown("**by region**")
    for region, val in region_data.items():
        st.text(f"{region}: {val}")

    # Gauge for setup time
    fig, ax = plt.subplots(figsize=(3, 1.5), subplot_kw={'projection': 'polar'})
    value = 8.7
    max_val = 20
    theta = np.pi * (1 - value / max_val)
    ax.barh(0, np.pi - theta, color="#00FA9A")
    ax.set_facecolor("#0e1117")
    plt.text(0, 0, f"{value:.1f} d", color="white", ha="center", va="center", fontsize=12)
    st.pyplot(fig)

# ───────────────────────────────────────────────
# KPI 3 — Hiring Card
# ───────────────────────────────────────────────
with col3:
    st.subheader("👥 Hire 50 new team members")
    st.metric(label="New hires", value="36", delta="+6")
    st.progress(int(36 / 50 * 100))

    dept_data = {
        "Account": 12,
        "CS": 10,
        "Dev": 8,
        "Marketing": 4,
        "Exec": 2,
    }
    st.markdown("**by department**")
    for dept, val in dept_data.items():
        st.text(f"{dept}: {val}")

    # Gauge for time-to-fill
    fig, ax = plt.subplots(figsize=(3, 1.5), subplot_kw={'projection': 'polar'})
    value = 24
    max_val = 30
    theta = np.pi * (1 - value / max_val)
    ax.barh(0, np.pi - theta, color="#FFD54F")
    ax.set_facecolor("#0e1117")
    plt.text(0, 0, f"{value} d", color="white", ha="center", va="center", fontsize=12)
    st.pyplot(fig)

st.caption("Dashboard generated using Streamlit + Matplotlib gauges.")

