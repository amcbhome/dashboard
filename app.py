import streamlit as st
import pandas as pd
import altair as alt

# ────────────────────────────────────────────────
# Streamlit Page Setup
# ────────────────────────────────────────────────
st.set_page_config(page_title="Income vs Investments Dashboard", layout="centered")

st.title("💰 Income Survey Dashboard")
st.markdown("""
Explore **Income After Tax** vs **Investments**  
with linked brushing and demographic filters.
""")

# ────────────────────────────────────────────────
# Load Dataset
# ────────────────────────────────────────────────
uploaded_file = st.file_uploader("Upload the Income Survey CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Ensure the columns exist
    expected_columns = ["Income_After_Tax", "Investments", "Age", "Gender", "Marital_Status"]
    if not all(col in df.columns for col in expected_columns):
        st.error(f"❌ Expected columns not found. Please ensure these columns exist: {expected_columns}")
    else:
        # ────────────────────────────────────────────────
        # Linked Brushing with Altair
        # ────────────────────────────────────────────────
        brush = alt.selection_interval()

        points = (
            alt.Chart(df)
            .mark_point()
            .encode(
                x=alt.X("Income_After_Tax:Q", title="Income After Tax"),
                y=alt.Y("Investments:Q", title="Investments"),
                color=alt.condition(brush, "Gender:N", alt.value("lightgray")),
                tooltip=["Age", "Gender", "Marital_Status", "Income_After_Tax", "Investments"]
            )
            .add_params(brush)
            .properties(width=500, height=350)
        )

        bars = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y=alt.Y("Gender:N", title="Gender"),
                x=alt.X("count():Q", title="Count"),
                color="Gender:N"
            )
            .transform_filter(brush)
            .properties(width=500, height=120)
        )

        chart = points & bars

        st.altair_chart(chart, use_container_width=True)

        # ────────────────────────────────────────────────
        # Interactive Table based on selection
        # ────────────────────────────────────────────────
        st.markdown("### Interactive Table (Age, Gender, Marital Status)")
        st.dataframe(df[["Age", "Gender", "Marital_Status", "Income_After_Tax", "Investments"]].head(50))

else:
    st.info("⬆️ Upload your Income Survey CSV to begin.")
