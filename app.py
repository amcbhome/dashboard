import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ───────────────────────────────────────────────
# Page setup
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="Financial Dashboard",
    layout="centered",
    page_icon="💹"
)

st.title("💹 Financial Performance Dashboard (2021–2024)")
st.markdown("Visualising key profit metrics and trends using the **Financial Dashboard Dataset**.")

# ───────────────────────────────────────────────
# Data preparation
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
# Metric calculations
# ───────────────────────────────────────────────
df["Gross Profit"] = df["Revenue"] - df["COGS"]
df["Operating Profit"] = df["Gross Profit"] - df["Operating Expenses"]
df["Net Profit"] = df["Operating Profit"] - df["Interest"] - df["Taxes"]

latest = df.iloc[-1]  # most recent year (2024)

# ───────────────────────────────────────────────
# KPI Section
# ───────────────────────────────────────────────
st.markdown("### 📊 Key Financial Metrics")
col1, col2, col3 = st.columns(3)

col1.metric(
    label="Gross Profit (2024)",
    value=f"£{latest['Gross Profit']:,}",
    delta=f"£{df['Gross Profit'].iloc[-1] - df['Gross Profit'].iloc[-2]:,}"
)
col2.metric(
    label="Operating Profit (2024)",
    value=f"£{latest['Operating Profit']:,}",
    delta=f"£{df['Operating Profit'].iloc[-1] - df['Operating Profit'].iloc[-2]:,}"
)
col3.metric(
    label="Net Profit (2024)",
    value=f"£{latest['Net Profit']:,}",
    delta=f"£{df['Net Profit'].iloc[-1] - df['Net Profit'].iloc[-2]:,}"
)

# ───────────────────────────────────────────────
# Line Chart (Profit Trends)
# ───────────────────────────────────────────────
sns.set_theme(style="darkgrid", palette="crest")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["Year"], df["Gross Profit"], marker='o', linewidth=3, label="Gross Profit")
ax.plot(df["Year"], df["Operating Profit"], marker='o', linewidth=3, label="Operating Profit")
ax.plot(df["Year"], df["Net Profit"], marker='o', linewidth=3, label="Net Profit")
ax.fill_between(df["Year"], df["Net Profit"], color="green", alpha=0.1)
ax.set_title("📈 Profit Trends Over Time", fontsize=16, weight='bold')
ax.set_xlabel("Year")
ax.set_ylabel("£ Amount")
ax.legend(title="Metrics")
ax.grid(alpha=0.3)
st.pyplot(fig)

# ───────────────────────────────────────────────
# Data Table
# ───────────────────────────────────────────────
st.markdown("### 📋 Detailed Financial Data")
st.dataframe(df.style.format("{:,.0f}"))

# ───────────────────────────────────────────────
# Footer
# ───────────────────────────────────────────────
st.caption("Generated with 🧠 AI + Streamlit | Dataset: mohazone/financial-dashboard (Kaggle)")

