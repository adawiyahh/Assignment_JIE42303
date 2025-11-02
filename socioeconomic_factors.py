# sosioeconomic_factors.py
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
    st.title("Sosioeconomic Factors")
    st.markdown("---")

    # Objective statement
    st.markdown(
        "**Objective Statement:** To find patterns between CGPA, hometown (rural or urban), and family income in order to figure out whether student background affects performance. "
    )

    st.markdown("---")
    
    # Load Dataset
    csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3_socioeconomic.csv"
    try:
        df = pd.read_csv(csv_url)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return
    
    # Summary metrics related to socioeconomic background
    col1, col2, col3, col4 = st.columns(4)
    
    avg_cgpa = df['Overall'].mean() if 'Overall' in df else 0
    avg_attendance = df['Attendance'].mean() if 'Attendance' in df else 0
    avg_income = df['Income'].mean() if 'Income' in df else 0
    # For hometown, just use a placeholder value or skip calculation to prevent errors
    hometown_info = "Rural / Urban"  # replace with actual value if needed
    
    col1.metric(label="🎓 Average CGPA", value=f"{avg_cgpa:.2f}",
                help="Average cumulative CGPA of students", border=True)
    col2.metric(label="📚 Average Attendance", value=f"{avg_attendance:.1f}",
                help="Average class attendance of students", border=True)
    col3.metric(label="💰 Average Family Income", value=f"RM{avg_income:,.0f}",
                help="Average monthly family income of students", border=True)
    col4.metric(label="🏘 Hometown Distribution", value=hometown_info,
                help="Percentage of students from rural vs urban areas", border=True)
    
    st.markdown("---")
    # Display cleaned dataset
    st.subheader("Dataset: Socioeconomic and Overall Performance")
    st.dataframe(df)
    
    st.markdown("---")

    # First visualization 
    st.markdown("### Visualization 1: Income vs Overall CGPA")
    
    st.subheader("Box Plot")
    
    # Create the boxplot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='Income', y='Overall', color='#FF69B4', ax=ax)
    ax.set_title('Boxplot of Income vs Overall CGPA')
    ax.set_xlabel('Income Category')
    ax.set_ylabel('Overall CGPA')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    

    # Display plot in Streamlit
    st.pyplot(fig)
    plt.close(fig)
    
    # Calculate descriptive statistics for Overall CGPA by Income
    income_overall_stats = df.groupby('Income')['Overall'].agg(
        ['mean', 'median', lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]
    )
    income_overall_stats = income_overall_stats.rename(
        columns={'<lambda_0>': '25th_percentile', '<lambda_1>': '75th_percentile'}
    )
    
    # Display statistics in Streamlit
    st.markdown("### Descriptive Statistics for Overall CGPA by Income Level")
    st.dataframe(income_overall_stats.style.format("{:.2f}"))
    
    # Interpretation Section
    st.markdown("### Interpretation")
    st.write("""
    With a **consistent median Overall CGPA** (between 3.0 and 3.5 for the majority of income categories, **Income Category 6 (Low)** stands out as having a **significantly lower median** and a narrow performance range.
    """)


    st.markdown("---")

    # Second visualization 
    st.markdown("### Visualization 2: Average CGPA by Hometown")
    
    st.subheader("Box plot")

    # Create the boxplot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='Hometown', y='Overall', color='purple', ax=ax)
    ax.set_title('Box Plot of Overall CGPA by Hometown')
    ax.set_xlabel('Hometown')
    ax.set_ylabel('Overall CGPA')
    
    # Replace encoded labels with actual hometown names if available
    if 'label_encoders' in locals() and 'Hometown' in label_encoders:
        hometown_categories = label_encoders['Hometown'].classes_
        ax.set_xticks(range(len(hometown_categories)))
        ax.set_xticklabels(hometown_categories, rotation=45)
    
    ax.grid(True)
    plt.tight_layout()
    
    # Display plot in Streamlit
    st.pyplot(fig)
    plt.close(fig)
    
    # Calculate descriptive statistics for 'Overall' CGPA grouped by 'Hometown'
    hometown_overall_stats = df.groupby('Hometown')['Overall'].agg([
        'mean', 'median', 'std',
        lambda x: x.quantile(0.25),
        lambda x: x.quantile(0.75)
    ])
    
    # Rename the quartile columns for clarity
    hometown_overall_stats = hometown_overall_stats.rename(
        columns={'<lambda_0>': '25th_percentile', '<lambda_1>': '75th_percentile'}
    )
    
    # Display descriptive statistics in Streamlit
    st.markdown("### Descriptive Statistics for Overall CGPA by Hometown")
    st.dataframe(hometown_overall_stats.style.format("{:.2f}"))
    
    # Interpretation Section
    st.markdown("### Interpretation")
    st.write("""
    Both **City** and **Village** students have **almost identical** performance consistency and median CGPA, indicating that **hometown has no meaningful effect** on the distribution of academic outcomes.
    """)

    st.markdown("---")

    

    # Third visualization 
    st.markdown("### Visualization 3: Distribution of Income Levels")
    
    st.subheader("Histogram")
    
    # Get unique income levels from the dataframe
    income_levels = df['Income'].unique()
    
    # Create the histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(
        data=df,
        x='Income',
        bins=len(income_levels),  # use unique values count
        kde=False,
        color='#FF69B4',
        ax=ax
    )
    ax.set_title('Distribution of Income Levels')
    ax.set_xlabel('Income Level')
    ax.set_ylabel('Frequency')
    
    # Optional: add tick labels
    ax.set_xticks(range(len(income_levels)))
    ax.set_xticklabels(sorted(income_levels), rotation=30)
    
    plt.tight_layout()
    
    # Display the figure in Streamlit
    st.pyplot(fig)
    plt.close(fig)
    
    # Interpretation section
    st.markdown("### Interpretation")
    st.write("""
    The **majority of students** are found in just three income groups in the **uneven distribution** visualisation: **Level 5** (Lower Middle), **Level 8** (Upper Middle), and **Level 0** (High).
    """)

    st.markdown("---")


    

