import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ───────────────────────────────────────────────
# Page setup
# ───────────────────────────────────────────────
st.set_page_config(page_title="Financial Dashboard", layout="centered")
st.title("📊 Financial Performance Dashboard (2021–2024)")

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
# Dashboard chart
# ───────────────────────────────────────────────
sns.set_theme(style="darkgrid", palette="crest")
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df["Year"], df["Gross Profit"], marker='o', linewidth=3, label="Gross Profit")
ax.plot(df["Year"], df["Operating Profit"], marker='o', linewidth=3, label="Operating Profit")
ax.plot(df["Year"], df["Net Profit"], marker='o', linewidth=3, label="Net Profit")

ax.fill_between(df["Year"], df["Net Profit"], color="green", alpha=0.1)
ax.set_title("📈 Profit Trends", fontsize=16, weight='bold')
ax.set_xlabel("Year")
ax.set_ylabel("£ Amount")
ax.legend(title="Profit Metrics")
ax.grid(alpha=0.3)

st.pyplot(fig)

# ───────────────────────────────────────────────
# Data table
# ───────────────────────────────────────────────
st.subheader("📋 Summary Data")
st.dataframe(df)
