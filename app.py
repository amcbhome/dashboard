import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ───────────────────────────────────────────────
# Page Setup
# ───────────────────────────────────────────────
st.set_page_config(page_title="Example Financial Dashboard", page_icon="💹", layout="wide")

st.title("💹 Example Financial Dashboard")
st.markdown("""
This dashboard demonstrates a **Streamlit financial overview**  
showing revenue, expenses, and profit trends from 2021–2024.
""")

# ───────────────────────────────────────────────
# Example Data
# ───────────────────────────────────────────────
data = {
    "Year": [2021, 2022, 2023, 2024],
    "Revenue": [200000, 250000, 300000, 340000],
    "Expenses": [120000, 150000, 180000, 200000]
}

df = pd.DataFrame(data)
df["Profit"] = df["Revenue"] - df["Expenses"]
df["Profit Margin %"] = (df["Profit"] / df["Revenue"]) * 100

# Latest year for KPIs
latest = df.iloc[-1]
previous = df.iloc[-2]

# ───────────────────────────────────────────────
# KPI Section
# ───────────────────────────────────────────────
st.markdown("### 📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Revenue (2024)",
    value=f"£{latest['Revenue']:,}",
    delta=f"£{latest['Revenue'] - previous['Revenue']:,}"
)

col2.metric(
    label="Profit (2024)",
    value=f"£{latest['Profit']:,}",
    delta=f"£{latest['Profit'] - previous['Profit']:,}"
)

col3.metric(
    label="Profit Margin (2024)",
    value=f"{latest['Profit Margin %']:.1f}%",
    delta=f"{latest['Profit Margin %'] - previous['Profit Margin %']:.1f} pp"
)

st.divider()

# ───────────────────────────────────────────────
# Visualization
# ───────────────────────────────────────────────
st.markdown("### 📈 Revenue, Expenses, and Profit Trends")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Year"], df["Revenue"], marker='o', label="Revenue")
ax.plot(df["Year"], df["Expenses"], marker='o', label="Expenses")
ax.plot(df["Year"], df["Profit"], marker='o', label="Profit")

ax.set_xlabel("Year")
ax.set_ylabel("£ Amount")
ax.set_title("Financial Trends (2021–2024)", weight='bold')
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

# ───────────────────────────────────────────────
# Data Table
# ───────────────────────────────────────────────
st.markdown("### 📋 Detailed Data Table")
st.dataframe(
    df.style.format({
        "Revenue": "£{:,.0f}",
        "Expenses": "£{:,.0f}",
        "Profit": "£{:,.0f}",
        "Profit Margin %": "{:.1f}%"
    })
)

# ───────────────────────────────────────────────
# Footer
# ───────────────────────────────────────────────
st.caption("Demo Financial Dashboard • Created with Streamlit 💻")

