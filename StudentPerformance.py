import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Assignment JIE42303 Scientific Visualization")

st.header("Assignment JIE42303 Scientific Visualization", divider="gray")

st.subheader("Dataset: Student Performance Metrics")

# Load dataset from GitHub 
# Replace this URL with your actual raw CSV file link
csv_url = "https://raw.githubusercontent.com/adawiyahh/sciviz2025/refs/heads/main/law_faculty_survey.csv"
col1, col2, col3, col4 = st.columns(4)
    
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)

# Read dataset directly from GitHub
law_df = pd.read_csv(csv_url)
st.dataframe(law_df)

