# StudentPerformance.py
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("Student Performance")
    st.header("Assignment JIE42303 Scientific Visualization")
    st.subheader("Dataset: Student Performance Metrics")
    st.markdown("---")
    
    # Load Dataset
    csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3_cleaned.csv"
    try:
        df = pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    avg_cgpa = df['Overall'].mean() if 'Overall' in df else 0
    avg_attendance = df['Attendance'].mean() if 'Attendance' in df else 0
    avg_prep = df['Preparation'].mean() if 'Preparation' in df else 0
    avg_gaming = df['Gaming'].mean() if 'Gaming' in df else 0
    col1.metric("🎓 Average CGPA", f"{avg_cgpa:.2f}")
    col2.metric("📚 Average Attendance", f"{avg_attendance:.1f}")
    col3.metric("📝 Average Study Preparation", f"{avg_prep:.1f}")
    col4.metric("🎮 Average Gaming Time", f"{avg_gaming:.1f}")
    
    # Dataset
    st.subheader("Student Dataset")
    st.dataframe(df)

