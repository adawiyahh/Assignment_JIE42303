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

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Student Performance"

# Sidebar menu
st.sidebar.title("Menu")

# Function to create a clickable menu item
def menu_item(label, icon, page_name):
    if st.sidebar.markdown(
        f"""
        <div style="padding:5px 0;">
            <a href="#" onclick="window.location.href='#{page_name}'" style="text-decoration:none; color:black; font-size:16px;">
                <span class="material-symbols-outlined" style="vertical-align:middle;">{icon}</span> {label}
            </a>
        </div>
        """,
        unsafe_allow_html=True
    ):
        st.session_state.page = page_name

# Sidebar menu items (we track clicks via session_state)
if st.sidebar.button("Student Performance"):
    st.session_state.page = "Student Performance"
if st.sidebar.button("Socioeconomic Factors"):
    st.session_state.page = "Socioeconomic Factors"
if st.sidebar.button("Behavior Lifestyle"):
    st.session_state.page = "Behavior Lifestyle"

# Load the selected page
if st.session_state.page == "Student Performance":
    StudentPerformance.app()
elif st.session_state.page == "Socioeconomic Factors":
    socioeconomic_factors.app()
elif st.session_state.page == "Behavior Lifestyle":
    behavior_lifestyle.app()

