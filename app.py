import streamlit as st
import pandas as pd

# ───────────────────────────────────────────────
# Page setup
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="Financial KPI Dashboard",
    page_icon="💹",
    layout="wide"
)

st.title("💹 Financial KPI Dashboard (2021–2024)")
st.markdown("Displaying enlarged, key profitability indicators from the **Financial Dashboard Dataset**.")

# ───────────────────────────────────────────────
# Dataset
# ───────────────────────────────────────────────
data = {
    "Year": [2021, 2022, 2023, 2024],
    "Revenue": [120000, 150000, 180000, 210000],
    "COGS": [65000, 80000, 95000, 110000],
    "Operating Expenses": [15000, 20000, 25000, 30000],
    "Interest": [4000, 5000, 6000, 7000],
    "Taxes": [5000, 7000, 8000, 9000],
}
df = pd.DataFrame(data)

# ───────────────────────────────────────────────
# Calculations
# ───────────────────────────────────────────────
df["Gross Profit"] = df["Revenue"] - df["COGS"]
df["Operating Profit"] = df["Gross Profit"] - df["Operating Expenses"]
df["Net Profit"] = df["Operating Profit"] - df["Interest"] - df["Taxes"]

df["Gross Margin %"] = (df["Gross Profit"] / df["Revenue"]) * 100
df["Operating Margin %"] = (df["Operating Profit"] / df["Revenue"]) * 100
df["Net Margin %"] = (df["Net Profit"] / df["Revenue"]) * 100

latest = df.iloc[-1]
previous = df.iloc[-2]

# ───────────────────────────────────────────────
# Helper: Large KPI Card Function
# ───────────────────────────────────────────────
def kpi_card(title, value, delta=None, color="#2E8B57"):
    st.markdown(
        f"""
        <div style="
            background-color: {color};
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            ">
            <h2 style="font-size: 24px; margin-bottom: 10px;">{title}</h2>
            <h1 style="font-size: 46px; margin: 0;">{value}</h1>
            <p style="font-size: 18px; opacity: 0.85;">{delta}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ───────────────────────────────────────────────
# KPI Section – Profits
# ───────────────────────────────────────────────
st.markdown("### 💰 Profit Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    kpi_card(
        "Gross Profit (2024)",
        f"£{latest['Gross Profit']:,}",
        f"Δ £{latest['Gross Profit'] - previous['Gross Profit']:,}",
        color="#1E90FF"
    )

with col2:
    kpi_card(
        "Operating Profit (2024)",
        f"£{latest['Operating Profit']:,}",
        f"Δ £{latest['Operating Profit'] - previous['Operating Profit']:,}",
        color="#4682B4"
    )

with col3:
    kpi_card(
        "Net Profit (2024)",
        f"£{latest['Net Profit']:,}",
        f"Δ £{latest['Net Profit'] - previous['Net Profit']:,}",
        color="#2E8B57"
    )

# ───────────────────────────────────────────────
# KPI Section – Margins
# ───────────────────────────────────────────────
st.markdown("### 📐 Profit Margins")

col4, col5, col6 = st.columns(3)

with col4:
    kpi_card(
        "Gross Margin %",
        f"{latest['Gross Margin %']:.1f}%",
        f"Δ {latest['Gross Margin %'] - previous['Gross Margin %']:.1f} pp",
        color="#20B2AA"
    )

with col5:
    kpi_card(
        "Operating Margin %",
        f"{latest['Operating Margin %']:.1f}%",
        f"Δ {latest['Operating Margin %'] - previous['Operating Margin %']:.1f} pp",
        color="#00BFFF"
    )

with col6:
    kpi_card(
        "Net Margin %",
        f"{latest['Net Margin %']:.1f}%",
        f"Δ {latest['Net Margin %'] - previous['Net Margin %']:.1f} pp",
        color="#3CB371"
    )

# ───────────────────────────────────────────────
# Data Table
# ───────────────────────────────────────────────
st.markdown("### 📋 Full Financial Data")
st.dataframe(
    df.style.format({
        "Revenue": "£{:,.0f}",
        "COGS": "£{:,.0f}",
        "Operating Expenses": "£{:,.0f}",
        "Interest": "£{:,.0f}",
        "Taxes": "£{:,.0f}",
        "Gross Profit": "£{:,.0f}",
        "Operating Profit": "£{:,.0f}",
        "Net Profit": "£{:,.0f}",
        "Gross Margin %": "{:.1f}%",
        "Operating Margin %": "{:.1f}%",
        "Net Margin %": "{:.1f}%"
    })
)

st.caption("Generated with 🧠 AI + Streamlit | Dataset: mohazone/financial-dashboard (Kaggle)")


