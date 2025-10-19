import streamlit as st
import pandas as pd
import altair as alt

# ────────────────────────────────────────────────
# Streamlit Page Setup
# ────────────────────────────────────────────────
st.set_page_config(page_title="Income vs Investment Dashboard", layout="centered")

st.title("💰 Income vs Investment Dashboard")
st.markdown("""
Explore the relationship between **Income after Tax** and **Investment**  
across different **Marital Status** categories.  
You can brush over the scatter plot to filter the bar chart and table.
""")

# ────────────────────────────────────────────────
# Load Dataset
# ────────────────────────────────────────────────
uploaded_file = st.file_uploader("Upload your Income Survey CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Check for expected columns
    expected_cols = ["Income_after_tax", "Investment", "Marital_status", "Private_pension"]
    if not all(col in df.columns for col in expected_cols):
        st.error(f"❌ Missing columns. Please ensure these exist: {expected_cols}")
    else:
        # ────────────────────────────────────────────────
        # Linked Brushing Charts
        # ────────────────────────────────────────────────
        brush = alt.selection_interval()

        points = (
            alt.Chart(df)
            .mark_point(size=70, filled=True)
            .encode(
                x=alt.X("Income_after_tax:Q", title="Income After Tax"),
                y=alt.Y("Investment:Q", title="Investment"),
                color=alt.condition(brush, "Marital_status:N", alt.value("lightgray")),
                tooltip=["Marital_status", "Private_pension", "Income_after_tax", "Investment"]
            )
            .add_params(brush)
            .properties(width=520, height=360)
        )

        bars = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y=alt.Y("Marital_status:N", title="Marital Status"),
                x=alt.X("count():Q", title="Count"),
                color="Marital_status:N"
            )
            .transform_filter(brush)
            .properties(width=520, height=140)
        )

        chart = points & bars

        # Display chart
        st.altair_chart(chart, use_container_width=True)

        # ────────────────────────────────────────────────
        # Interactive Table
        # ────────────────────────────────────────────────
        st.markdown("### Interactive Table (Marital Status & Private Pension)")
        st.dataframe(df[["Marital_status", "Private_pension", "Income_after_tax", "Investment"]].head(50))

else:
    st.info("⬆️ Upload your Income Survey CSV file to begin.")
