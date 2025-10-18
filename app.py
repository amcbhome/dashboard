import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ───────────────────────────────────────────────
# Page Setup
# ───────────────────────────────────────────────
st.set_page_config(page_title="Modern Financial Dashboard", page_icon="💼", layout="wide")

st.title("💼 Modern Financial Dashboard")
st.caption("A monthly breakdown of revenue, expenses, and cost of goods sold (COGS).")

# ───────────────────────────────────────────────
# Simulated Monthly Data
# ───────────────────────────────────────────────
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data = {
    "Month": months,
    "Revenue": [310000, 450000, 380000, 270000, 320000, 250000, 340000, 410000, 430000, 470000, 420000, 390000],
    "Expenses": [290000, 410000, 370000, 260000, 300000, 240000, 330000, 400000, 420000, 460000, 410000, 380000],
    "COGS": [120000, 160000, 150000, 100000, 120000, 90000, 140000, 160000, 150000, 170000, 155000, 140000]
}
df = pd.DataFrame(data)

# Summary
total_revenue = df["Revenue"].sum()
total_expenses = df["Expenses"].sum()
total_cogs = df["COGS"].sum()
net_profit = total_revenue - total_expenses

# ───────────────────────────────────────────────
# Layout: 3 Columns (KPI | Chart | Breakdown)
# ───────────────────────────────────────────────
left, center, right = st.columns([1, 2, 1])

# LEFT PANEL – KPIs
with left:
    st.markdown("### 📊 This Year")
    st.markdown(f"### 💰 **${total_revenue/1_000_000:.1f}M**  \n**Revenue**")
    st.markdown(f"### 💸 **${total_expenses/1_000_000:.1f}M**  \n**Expenses**")
    st.markdown(f"### 🏭 **${total_cogs/1_000_000:.1f}M**  \n**COGS**")
    st.markdown(f"### 📈 **${net_profit/1_000_000:.1f}M**  \n**Net Profit**")

# CENTER PANEL – Chart
with center:
    st.markdown("### 📆 Monthly Performance")
    fig, ax = plt.subplots(figsize=(8, 4))
    width = 0.35
    ax.bar(df["Month"], df["Revenue"], width, label="Revenue", color="#4CAFEB")
    ax.bar(df["Month"], df["Expenses"], width, label="Expenses", color="#FFD54F", alpha=0.8, bottom=None)
    ax.plot(df["Month"], df["COGS"], color="red", linewidth=2, marker="o", label="COGS")

    ax.set_ylabel("USD ($)")
    ax.set_title("Monthly Revenue vs Expenses with COGS Trend")
    ax.legend()
    st.pyplot(fig)

# RIGHT PANEL – Breakdown
with right:
    st.markdown("### 🧾 Expense Breakdown")
    expense_breakdown = {
        "Salary": 315000,
        "Office costs": 21000,
        "Marketing": 25000,
        "Agency & consultancy": 10400,
        "Equipment": 7600,
        "Travel": 8500,
        "Other": 1500
    }

    for category, value in expense_breakdown.items():
        st.write(f"**{category}**")
        st.progress(int(value / max(expense_breakdown.values()) * 100))
        st.markdown(f"${value/1000:.1f}K")

# ───────────────────────────────────────────────
# Data Table (Optional)
# ───────────────────────────────────────────────
st.markdown("---")
st.markdown("### 📋 Detailed Data Table")
st.dataframe(df.style.format({"Revenue": "${:,.0f}", "Expenses": "${:,.0f}", "COGS": "${:,.0f}"}))
