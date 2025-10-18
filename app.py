import streamlit as st
import altair as alt
from vega_datasets import data

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Car Performance Dashboard",
    layout="centered"
)

st.title("🚗 Car Performance Dashboard")
st.markdown("""
Explore relationships between **horsepower**, **fuel efficiency**, and **car origin**  
using an interactive linked-brushing chart.
""")

# ──────────────────────────────────────────────
# Load Data
# ──────────────────────────────────────────────
source = data.cars()

# ──────────────────────────────────────────────
# Define an Interval Selection (Brush)
# ──────────────────────────────────────────────
brush = alt.selection_interval()

# ──────────────────────────────────────────────
# Scatter Plot
# ──────────────────────────────────────────────
points = (
    alt.Chart(source, title="Horsepower vs. Miles per Gallon")
    .mark_point(filled=True, size=80)
    .encode(
        x=alt.X("Horsepower:Q", title="Horsepower"),
        y=alt.Y("Miles_per_Gallon:Q", title="Miles per Gallon (MPG)"),
        color=alt.condition(brush, "Origin:N", alt.value("lightgray")),
        tooltip=[
            alt.Tooltip("Name:N", title="Car"),
            alt.Tooltip("Origin:N", title="Origin"),
            alt.Tooltip("Horsepower:Q", title="Horsepower"),
            alt.Tooltip("Miles_per_Gallon:Q", title="MPG"),
            alt.Tooltip("Cylinders:Q", title="Cylinders"),
        ],
    )
    .add_params(brush)
    .interactive()
    .properties(width=600, height=400)
)

# ──────────────────────────────────────────────
# Bar Chart Filtered by Brush
# ──────────────────────────────────────────────
bars = (
    alt.Chart(source, title="Count by Origin (filtered by selection)")
    .mark_bar()
    .encode(
        y=alt.Y("Origin:N", title="Origin"),
        x=alt.X("count(Origin):Q", title="Number of Cars"),
        color="Origin:N",
        tooltip=["Origin:N", "count(Origin):Q"],
    )
    .transform_filter(brush)
    .properties(width=600)
)

# ──────────────────────────────────────────────
# Combine and Display
# ──────────────────────────────────────────────
chart = points & bars
st.altair_chart(chart, use_container_width=True)

# Optional note
st.caption("Data source: Vega Datasets – 'cars.csv'")

