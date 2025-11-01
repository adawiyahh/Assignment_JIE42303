import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page config
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Sidebar menu title
st.sidebar.title("Menu")

# Sidebar buttons for navigation (no dropdown)
if st.sidebar.button("🏫  Student Performance"):
    StudentPerformance.app()
elif st.sidebar.button("📊  Socioeconomic Factors"):
    socioeconomic_factors.app()
elif st.sidebar.button("🗂  Behavior Lifestyle"):
    behavior_lifestyle.app()


