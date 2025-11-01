import streamlit as st

st.set_page_config(page_title="Student Performance Dashboard")

# Define Pages
academic = st.Page("StudentPerformance.py", title="Student Performance", icon=":material/school:")
socioeconomic = st.Page("socioeconomic_factors.py", title="Socioeconomic Insights", icon=":material/finance_chip:")
behavior = st.Page("behavior_lifestyle.py", title="Behavioral Patterns", icon=":material/psychology:")

# Navigation Menu
pg = st.navigation(
    {
        "Analysis Pages": [academic, socioeconomic, behavior]
    }
)

pg.run()
