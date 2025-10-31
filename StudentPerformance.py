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
df = pd.read_csv(csv_url)

# Convert numeric columns safely
for col in ['Overall', 'Attendance', 'Preparation', 'Gaming']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # convert text -> NaN for safety
col1, col2, col3, col4 = st.columns(4)

    
col1.metric(
    label="Average CGPA", 
    value=f"{df['Overall'].mean():.2f}", 
    help="Represents the average cumulative grade point average (Overall) of students.", 
    border=True
)

col2.metric(
    label="Average Attendance", 
    value=f"{df['Attendance'].mean():.2f}", 
    help="Shows the average attendance rate of students in class participation.", 
    border=True
)

col3.metric(
    label="Average Study Preparation", 
    value=f"{df['Preparation'].mean():.2f}", 
    help="Average hours students spend on study preparation outside class.", 
    border=True
)

col4.metric(
    label="Average Gaming Time", 
    value=f"{df['Gaming'].mean():.2f}", 
    help="Average time students spend on gaming activities daily.", 
    border=True
)

st.dataframe(df)

