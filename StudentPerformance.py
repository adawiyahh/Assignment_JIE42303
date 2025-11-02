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


    st.markdown("---")

    # Title for the first visualization
    st.markdown("### Visualization 1: HSC vs Overall CGPA")

    st.subheader("Scatter Plot")

    # Create Seaborn scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='HSC', y='Overall', color='purple', ax=ax)
    ax.set_title('Scatter Plot of HSC vs Overall CGPA')
    ax.set_xlabel('HSC Score')
    ax.set_ylabel('Overall CGPA')
    ax.grid(True)

    # Display plot in Streamlit
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # Interpretation Section
    st.markdown("### Interpretation")
    st.write("""
    According to the visualisation, there seems to be a slightly positive correlation between the HSC Score and the overall CGPA, indicating that students who have performed better academically in the past typically have higher university CGPAs.
    """)

    st.markdown("---")

    # Second visualization
    st.markdown("### Visualization 2: SSC vs Overall CGPA")

    st.subheader("Scatter Plot")

    # Create Seaborn scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='SSC', y='Overall', color='#FF69B4', ax=ax)
    ax.set_title('Scatter Plot of SSC vs Overall CGPA')
    ax.set_xlabel('SSC Score')
    ax.set_ylabel('Overall CGPA')
    ax.grid(True)

    # Display plot in Streamlit
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # Interpretation Section
    st.markdown("### Interpretation")
    st.write("""
    This scatter plot shows that the SSC score has little predictive power for academic success because there seems to be a weak positive association between the SSC score and the overall CGPA.
    """)

    # Third visualization
    st.markdown("### Visualization 3: Boxplot of Semester vs Overall CGPA")

    st.subheader("Scatter Plot")

    # Create Seaborn scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x='Semester', y='Overall', color='purple', ax=ax)
    ax.set_title('Boxplot of Semester vs Overall CGPA')
    ax.set_xlabel('Semester')
    ax.set_ylabel('Overall CGPA')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display plot in Streamlit
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # Calculate mean, median, and quartiles for Overall CGPA by Semester
    semester_stats = df.groupby('Semester')['Overall'].describe()

    # Display statistics in Streamlit
    st.markdown("### Overall CGPA Statistics by Semester")
    st.dataframe(semester_stats)

    # Interpretation Section
    st.markdown("### Interpretation")
    st.write("""
    Throughout the semesters, the students' **median Overall CGPA** stays high, but performance consistency often **decreases** after Semester 2 (highest median, smallest spread), with **greater variability** and more low-scoring outliers starting in **Semester 6**.
    """)
    
