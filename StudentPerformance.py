import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page config
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Sidebar menu
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Navigate to:",
    ["Student Performance", "Socioeconomic Factors", "Behavior Lifestyle"]
)

# Load the selected page
if page == "Student Performance":
    StudentPerformance.app()
elif page == "Socioeconomic Factors":
    socioeconomic_factors.app()
elif page == "Behavior Lifestyle":
    behavior_lifestyle.app()


