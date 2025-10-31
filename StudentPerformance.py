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
csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3.csv"
col1, col2, col3, col4 = st.columns(4)
    
col1.metric(label="🎓 Average CGPA", value=f"{avg_cgpa}")
col2.metric(label="📚 Avg Study Preparation (hrs)", value=f"{avg_prep}")
col3.metric(label="🎮 Avg Gaming Time (hrs)", value=f"{avg_gaming}")
col4.metric(label="🏫 Avg Attendance", value=f"{avg_attendance}")

# Read dataset directly from GitHub
law_df = pd.read_csv(csv_url)
st.dataframe(law_df)

