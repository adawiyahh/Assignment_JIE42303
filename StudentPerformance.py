import streamlit as st
from streamlit_option_menu import option_menu
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

st.set_page_config(page_title="Student Dashboard", layout="wide")

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",  # Sidebar title
        options=["Student Performance", "Socioeconomic Factors", "Behavior Lifestyle"],
        icons=["school", "coin", "person-lines-fill"],  # Icons for each page
        menu_icon="cast",  # Optional menu icon
        default_index=0  # default page
    )

# Load selected page
if selected == "Student Performance":
    StudentPerformance.app()
elif selected == "Socioeconomic Factors":
    socioeconomic_factors.app()
elif selected == "Behavior Lifestyle":
    behavior_lifestyle.app()


