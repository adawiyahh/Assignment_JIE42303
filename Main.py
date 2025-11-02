import streamlit as st
import StudentPerformance
import socioeconomic_factors
import behavior_lifestyle

# Page config
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Define pages using Material Icons
student_perf = st.Page(
    "StudentPerformance.py", 
    title="Student Performance", 
    icon=":material/school:"
)

socio_factors = st.Page(
    "socioeconomic_factors.py", 
    title="Socioeconomic Factors", 
    icon=":material/finance_chip:"
)

behavior_life = st.Page(
    "behavior_lifestyle.py", 
    title="Behavior Lifestyle", 
    icon=":material/psychology:"
)

# Create the navigation menu
pages = st.navigation(
    {
        "Menu": [student_perf, socio_factors, behavior_life]
    }
)

# Run the navigation
pages.run()

