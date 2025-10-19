import streamlit as st
import altair as alt
from vega_datasets import data

# ────────────────────────────────────────────────
# Streamlit Page Setup
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Linked Brushing Demo",
    layout="centered"
)

st.title("🎯 Altair Linked Brushing Example")
st.markdown("""
This Streamlit app demonstrates **linked brushing** using  
the built-in **Cars dataset** from `vega_datasets`.  
Drag over the scatter plot to filter the bar chart by car origin.
""")

# ────────────────────────────────────────────────
# Load Dataset
# ────────────────────────────────────────────────
source = data.cars()

# ────────────────────────────────────────────────
# Create Altair Charts
# ────────────────────────────────────────────────
brush = alt.selection_interval()

points = (
    alt.Chart(source)
    .mark_point()
    .encode(
        x=alt.X('Horsepower:Q', title='Horsepower'),
        y=alt.Y('Miles_per_Gallon:Q', title='Miles per Gallon'),
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray')),
        tooltip=['Name:N', 'Origin:N', 'Horsepower:Q', 'Miles_per_Gallon:Q']
    )
    .add_params(brush)
    .properties(width=500, height=300)
)

bars = (
    alt.Chart(source)
    .mark_bar()
    .encode(
        y=alt.Y('Origin:N', title='Origin'),
        color='Origin:N',
        x=alt.X('count(Origin):Q', title='Count')
    )
    .transform_filter(brush)
    .properties(width=500, height=150)
)

chart = points & bars

# ────────────────────────────────────────────────
# Display Chart
# ────────────────────────────────────────────────
st.altair_chart(chart, use_container_width=True)

st.caption("📊 Data source: vega_datasets.cars() | Built with Altair + Streamlit")

