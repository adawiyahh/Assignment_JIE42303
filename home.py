import streamlit as st
import importlib

st.set_page_config(page_title="Student Performance Dashboard")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["Student Performance", "Socioeconomic Insights", "Behavioral Patterns"]
)

def load_page(module_name, display_name):
    module = importlib.import_module(module_name)
    if hasattr(module, "app"):
        module.app()
    else:
        st.title(display_name)
        st.write("No content found. Please define an `app()` function in this module.")

if page == "Student Performance":
    load_page("StudentPerformance", "Student Performance")
elif page == "Socioeconomic Insights":
    load_page("socioeconomic_factors", "Socioeconomic Insights")
elif page == "Behavioral Patterns":
    load_page("behavior_lifestyle", "Behavioral Patterns")
