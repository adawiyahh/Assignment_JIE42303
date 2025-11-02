import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page configuration
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Select Page",
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

# Run the selected page
if page == "Student Performance":
    StudentPerformance.app()
elif page == "Socioeconomic Factors":
    socioeconomic_factors.app()
elif page == "Behavior Lifestyle":
    behavior_lifestyle.app()


# Run the navigation
pages.run()


