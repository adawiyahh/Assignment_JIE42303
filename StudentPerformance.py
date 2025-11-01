import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page configuration
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Add Material Symbols font
st.markdown("""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" />
""", unsafe_allow_html=True)

# Initialize session state for page
if "page" not in st.session_state:
    st.session_state.page = "Student Performance"

# Sidebar menu title
st.sidebar.title("Menu")

# Function to create a menu item with Material icon
def menu_item(label, icon, key):
    if st.sidebar.button(
        f'<span class="material-symbols-outlined" style="vertical-align:middle;">{icon}</span>  {label}',
        key=key,
        unsafe_allow_html=True
    ):
        st.session_state.page = label

# Sidebar menu items
menu_item("Student Performance", "analytics", "menu1")
menu_item("Socioeconomic Factors", "finance_mode", "menu2")
menu_item("Behavior Lifestyle", "psychology", "menu3")

# Load the selected page
if st.session_state.page == "Student Performance":
    StudentPerformance.app()
elif st.session_state.page == "Socioeconomic Factors":
    socioeconomic_factors.app()
elif st.session_state.page == "Behavior Lifestyle":
    behavior_lifestyle.app()

