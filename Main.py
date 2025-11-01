import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page config
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Add Material Symbols font
st.markdown("""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" />
""", unsafe_allow_html=True)

# Sidebar title
st.sidebar.title("Menu")

# Sidebar menu using radio buttons
page = st.sidebar.radio(
    label="",  # No label above menu
    options=[
        "Student Performance",
        "Socioeconomic Factors",
        "Behavior Lifestyle"
    ],
    format_func=lambda x: {
        "Student Performance": "📊 Student Performance",
        "Socioeconomic Factors": "💹 Socioeconomic Factors",
        "Behavior Lifestyle": "🧠 Behavior Lifestyle"
    }[x]
)

# Load the selected page
if page == "Student Performance":
    StudentPerformance.app()
elif page == "Socioeconomic Factors":
    socioeconomic_factors.app()
elif page == "Behavior Lifestyle":
    behavior_lifestyle.app()


