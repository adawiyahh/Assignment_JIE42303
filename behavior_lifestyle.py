# behavior_lifestyle.py
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
    st.title("Behavior Lifestyle")
    st.markdown("---")

    # Objective statement
    st.markdown(
        "**Objective Statement:** To Determine how study habits, gaming, attendance, extracurriculars, and job status affect student academic performance."
    )

    st.markdown("---")
    
    # Load Dataset
    csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3_behavior.csv"
    try:
        df = pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return
    
    # Summary metrics related to student lifestyle and activities
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Calculate numeric metrics (if they exist in the dataframe)
    avg_cgpa = df['Overall'].mean() if 'Overall' in df else 0
    avg_attendance = df['Attendance'].mean() if 'Attendance' in df else 0
    avg_study_hours = df['Preparation'].mean() if 'Preparation' in df else 0
    avg_gaming = df['Gaming'].mean() if 'Gaming' in df else 0
    avg_extra = df['Extra'].mean() if 'Extra' in df else 0
    
    # Display metrics
    col1.metric(label="🎓 Average CGPA", value=f"{avg_cgpa:.2f}",
                help="Average cumulative CGPA of students", border=True)
    col2.metric(label="📚 Average Attendance", value=f"{avg_attendance:.1f}",
                help="Average class attendance of students", border=True)
    col3.metric(label="⏰ Average Study Hours", value=f"{avg_study_hours:.1f}",
                help="Average weekly preparation/study hours of students", border=True)
    col4.metric(label="🎮 Average Gaming Hours", value=f"{avg_gaming:.1f}",
                help="Average weekly gaming hours of students", border=True)
    col5.metric(label="⭐ Average Extracurricular Hours", value=f"{avg_extra:.1f}",
                help="Average weekly extracurricular activity hours of students", border=True)
    
    st.markdown("---")
    # Display cleaned dataset
    st.subheader("Dataset: Study Habits, Lifestyle, and Academic Performance")
    st.dataframe(df)
    
    st.markdown("---")


    # First visualization
    st.markdown("### Visualization 1: Gaming Time vs Overall CGPA")
    
    st.subheader("Box Plot")
    
    # Ensure columns exist and drop missing values
if 'Gaming' in df.columns and 'Overall' in df.columns:
    plot_df = df[['Gaming', 'Overall']].dropna()

    # Convert Gaming to string if needed for categorical plotting
    plot_df['Gaming'] = plot_df['Gaming'].astype(str)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=plot_df, x='Gaming', y='Overall', color='#FF69B4', ax=ax)
    ax.set_title('Boxplot of Gaming Time vs Overall CGPA')
    ax.set_xlabel('Gaming Time')
    ax.set_ylabel('Overall CGPA')
    ax.grid(True)

    # Replace encoded labels if label_encoders exist
    if 'label_encoders' in locals() and 'Gaming' in label_encoders:
        gaming_categories = label_encoders['Gaming'].classes_
        ax.set_xticks(range(len(gaming_categories)))
        ax.set_xticklabels(gaming_categories, rotation=45, ha='right')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # Descriptive statistics
    gaming_overall_stats = plot_df.groupby('Gaming')['Overall'].agg(
        ['mean', 'median', 'std', lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]
    ).rename(columns={'<lambda_0>': '25th_percentile', '<lambda_1>': '75th_percentile'})

    st.markdown("### Descriptive Statistics for Overall CGPA by Gaming Time")
    st.dataframe(gaming_overall_stats.style.format("{:.2f}"))
    
    st.markdown("### Interpretation")
    st.write("""
    Higher **gaming time** is associated with **lower median Overall CGPA** and **greater inconsistency** in performance, showing a clear **negative trend**.  Students who play video games for **0-1 Hours** do the best, while those who play for **More than 3 Hours** do the worst.
    """)
    st.markdown("---")
    
    
    # Second visualization
    st.markdown("### Visualization 2: Overall CGPA by Preparation Level")
    
    st.subheader("Bar Chart")
    
    preparation_overall_mean = df.groupby('Preparation')['Overall'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=preparation_overall_mean, x='Preparation', y='Overall', color='purple', ax=ax)
    ax.set_title('Overall CGPA by Preparation Level')
    ax.set_xlabel('Preparation Level')
    ax.set_ylabel('Overall CGPA')
    
    # Replace encoded labels with actual preparation categories if available
    if 'label_encoders' in locals() and 'Preparation' in label_encoders:
        preparation_categories = label_encoders['Preparation'].classes_
        ax.set_xticks(range(len(preparation_categories)))
        ax.set_xticklabels(preparation_categories, rotation=45, ha='right')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    
    # Descriptive statistics
    preparation_overall_stats = df.groupby('Preparation')['Overall'].agg(['mean', 'median', 'std'])
    st.markdown("### Descriptive Statistics for Overall CGPA by Preparation Level")
    st.dataframe(preparation_overall_stats.style.format("{:.2f}"))
    
    st.markdown("### Interpretation")
    st.write("""
    The **mean Overall CGPA steadily increases** with more study time, showing a clear **positive relationship** between **Preparation Level** and academic achievement.  Students studying for **"0-1 Hour"** have the lowest average CGPA about 2.95, while those preparing for **"More than 3 Hours"** have the greatest average CGPA about 3.45.
    """)
    st.markdown("---")
    
    
    # Third visualization
    st.markdown("### Visualization 3: Overall CGPA by Attendance")
    
    st.subheader("Bar Chart")
    
    attendance_overall_mean = df.groupby('Attendance')['Overall'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=attendance_overall_mean, x='Attendance', y='Overall', color='#FF69B4', ax=ax)
    ax.set_title('Overall CGPA by Attendance Category')
    ax.set_xlabel('Attendance')
    ax.set_ylabel('Overall CGPA')
    
    # Replace encoded labels with actual attendance categories if available
    if 'label_encoders' in locals() and 'Attendance' in label_encoders:
        attendance_categories = label_encoders['Attendance'].classes_
        ax.set_xticks(range(len(attendance_categories)))
        ax.set_xticklabels(attendance_categories, rotation=45, ha='right')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    
    # Descriptive statistics
    attendance_overall_stats = df.groupby('Attendance')['Overall'].agg(['mean', 'median', 'std'])
    st.markdown("### Descriptive Statistics for Overall CGPA by Attendance Category")
    st.dataframe(attendance_overall_stats.style.format("{:.2f}"))
    
    st.markdown("### Interpretation")
    st.write("""
    The **mean Overall CGPA continually rises** as attendance percentages increase, showing a strong **positive correlation** between academic performance and **Attendance Category** in this bar chart.  The greatest average CGPA (about 3.55) is attained by students in the **80%-100%** group, while the lowest average (approximately 1.80) is obtained by those with **Below 40** attendance.
    """)
    st.markdown("---")
