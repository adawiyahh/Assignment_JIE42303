# StudentPerformance.py
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.markdown("""
        <h2 style='text-decoration: underline;'>
            Assignment JIE42303: Scientific Visualization
        </h2>
    """, unsafe_allow_html=True)
    st.title("Student Performance")
    st.markdown("---")

    # Objective statement
    st.markdown(
        "**Objective Statement:** To analyze the relationship between academic background and student performance. "
    )

    st.markdown("---")
    
    # Load Dataset
    csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3_selected_columns1.csv"
    try:
        df = pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return

    # Summary metrics related to academic background
    col1, col2, col3, col4 = st.columns(4)

    avg_cgpa = df['Overall'].mean() if 'Overall' in df else 0
    avg_last_sem = df['Last'].mean() if 'Last' in df else 0
    avg_hsc = df['HSC'].mean() if 'HSC' in df else 0
    avg_ssc = df['SSC'].mean() if 'SSC' in df else 0

    col1.metric(label="🎓 Average CGPA", value=f"{avg_cgpa:.2f}",
                help="Average cumulative CGPA of students", border=True)
    col2.metric(label="📝 Last Semester Performance", value=f"{avg_last_sem:.2f}",
                help="Average grade in the last semester", border=True)
    col3.metric(label="📚 Average HSC Score", value=f"{avg_hsc:.2f}",
                help="Average HSC (Higher Secondary Certificate) score", border=True)
    col4.metric(label="📖 Average SSC Score", value=f"{avg_ssc:.2f}",
                help="Average SSC (Secondary School Certificate) score", border=True)

    st.markdown("---")
    # Display cleaned dataset
    st.subheader("Dataset: Student Performance Metrics")
    st.dataframe(df)

    
