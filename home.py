import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page config
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Navigate to:",
    ["Student Performance", "Socioeconomic Insights", "Behavioral Patterns"]
)

# Load selected page
if page == "Student Performance":
    StudentPerformance.app()
elif page == "Socioeconomic Insights":
    socioeconomic_factors.app()
elif page == "Behavioral Patterns":
    behavior_lifestyle.app()

