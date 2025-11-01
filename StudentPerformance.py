# home.py
import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Sidebar
page = st.sidebar.selectbox(
    "Select Page",
    ["Student Performance", "Socioeconomic Insights", "Behavioral Patterns"]
)

# Load the selected page
if page == "Student Performance":
    StudentPerformance.app()
elif page == "Socioeconomic Insights":
    socioeconomic_factors.app()
elif page == "Behavioral Patterns":
    behavior_lifestyle.app()

