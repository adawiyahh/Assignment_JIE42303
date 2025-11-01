import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit Page Setup 
st.set_page_config(page_title="Assignment JIE42303 Scientific Visualization")

st.header("Assignment JIE42303 Scientific Visualization", divider="gray")
st.subheader("Dataset: Student Performance Metrics")

# Load Dataset from GitHub
csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3_cleaned.csv"
df = pd.read_csv(csv_url)

col1, col2, col3, col4 = st.columns(4)

avg_cgpa = df['Overall CGPA'].mean() if 'Overall CGPA' in df else 0
avg_attendance = df['Attendance'].mean() if 'Attendance' in df else 0
avg_prep = df['Preparation'].mean() if 'Preparation' in df else 0
avg_gaming = df['GamingTime'].mean() if 'GamingTime' in df else 0

col1.metric(label="🎓 Average CGPA", value=f"{avg_cgpa:.2f}", help="Average of all students’ cumulative CGPA")
col2.metric(label="📚 Average Attendance", value=f"{avg_attendance:.1f}", help="Average attendance rate among students")
col3.metric(label="📝 Average Study Preparation", value=f"{avg_prep:.1f}", help="Average study preparation level")
col4.metric(label="🎮 Average Gaming Time", value=f"{avg_gaming:.1f}", help="Average daily gaming hours")

# Display cleaned dataset 
st.dataframe(df)
