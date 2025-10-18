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
st.markdown("Displaying key profitability indicators from the **Financial Dashboard Dataset**.")

# ───────────────────────────────────────────────
# Financial dataset
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
# Profit calculations
# ───────────────────────────────────────────────
df["Gross Profit"] = df["Revenue"] - df["COGS"]
df["Operating Profit"] = df["Gross Profit"] - df["Operating Expenses"]
df["Net Profit"] = df["Operating Profit"] - df["Interest"] - df["Taxes"]

# ───────────────────────────────────────────────
# Margin calculations (%)
# ───────────────────────────────────────────────
df["Gross Margin %"] = (df["Gross Profit"] / df["Revenue"]) * 100
df["Operating Margin %"] = (df["Operating Profit"] / df["Revenue"]) * 100
df["Net Margin %"] = (df["Net Profit"] / df["Revenue"]) * 100

# Latest year for KPIs
latest = df.iloc[-1]
previous = df.iloc[-2]

# ───────────────────────────────────────────────
# KPI Section – Large Metrics
# ───────────────────────────────────────────────
st.markdown("### 📊 Profit Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="💰 Gross Profit (2024)",
    value=f"£{latest['Gross Profit']:,}",
    delta=f"£{latest['Gross Profit'] - previous['Gross Profit']:,}"
)

col2.metric(
    label="🏢 Operating Profit (2024)",
    value=f"£{latest['Operating Profit']:,}",
    delta=f"£{latest['Operating Profit'] - previous['Operating Profit']:,}"
)

col3.metric(
    label="📈 Net Profit (2024)",
    value=f"£{latest['Net Profit']:,}",
    delta=f"£{latest['Net Profit'] - previous['Net Profit']:,}"
)

st.markdown("---")

# ───────────────────────────────────────────────
# Margin Section – Enlarged Layout
# ───────────────────────────────────────────────
st.markdown("### 📐 Profit Margin Ratios")

col4, col5, col6 = st.columns(3)

col4.metric(
    label="Gross Margin %",
    value=f"{latest['Gross Margin %']:.1f}%",
    delta=f"{latest['Gross Margin %'] - previous['Gross Margin %']:.1f} pp"
)

col5.metric(
    label="Operating Margin %",
    value=f"{latest['Operating Margin %']:.1f}%",
    delta=f"{latest['Operating Margin %'] - previous['Operating Margin %']:.1f} pp"
)

col6.metric(
    label="Net Margin %",
    value=f"{latest['Net Margin %']:.1f}%",
    delta=f"{latest['Net Margin %'] - previous['Net Margin %']:.1f} pp"
)

st.markdown("---")

# ───────────────────────────────────────────────
# Data Table
# ───────────────────────────────────────────────
st.markdown("### 📋 Detailed Financial Data")
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

# ───────────────────────────────────────────────
# Footer
# ───────────────────────────────────────────────
st.caption("Generated with 🧠 AI + Streamlit | Dataset: mohazone/financial-dashboard (Kaggle)")


