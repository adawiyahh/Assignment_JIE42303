import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

st.set_page_config(page_title="Student Dashboard", layout="wide")

# Sidebar menu title
st.sidebar.title("Menu")

# Use radio for navigation — all pages always visible
page = st.sidebar.radio(
    label="",
    options=[
        "🏫 Student Performance",
        "📊 Socioeconomic Factors",
        "🗂 Behavior Lifestyle"
    ]
)

# Load selected page
if page == "🏫 Student Performance":
    StudentPerformance.app()
elif page == "📊 Socioeconomic Factors":
    socioeconomic_factors.app()
elif page == "🗂 Behavior Lifestyle":
    behavior_lifestyle.app()



