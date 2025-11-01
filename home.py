import streamlit as st
import pandas as pd

# Set page config (only once)
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["Student Performance", "Socioeconomic Insights", "Behavioral Patterns"]
)

# --- Page 1: Student Performance ---
if page == "Student Performance":
    st.title("Student Performance")
    st.header("Assignment JIE42303 Scientific Visualization")
    st.subheader("Dataset: Student Performance Metrics")

    # Load dataset
    csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3_cleaned.csv"
    df = pd.read_csv(csv_url)

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    avg_cgpa = df['Overall'].mean() if 'Overall' in df else 0
    avg_attendance = df['Attendance'].mean() if 'Attendance' in df else 0
    avg_prep = df['Preparation'].mean() if 'Preparation' in df else 0
    avg_gaming = df['Gaming'].mean() if 'Gaming' in df else 0

    col1.metric("🎓 Average CGPA", f"{avg_cgpa:.2f}")
    col2.metric("📚 Average Attendance", f"{avg_attendance:.1f}")
    col3.metric("📝 Average Study Preparation", f"{avg_prep:.1f}")
    col4.metric("🎮 Average Gaming Time", f"{avg_gaming:.1f}")

    # Display dataframe
    st.subheader("Student Dataset")
    st.dataframe(df)

# --- Page 2: Socioeconomic Insights ---
elif page == "Socioeconomic Insights":
    st.title("Socioeconomic Insights")
    st.write("Here you can add your socioeconomic visualizations and insights.")

# --- Page 3: Behavioral Patterns ---
elif page == "Behavioral Patterns":
    st.title("Behavioral Patterns")
    st.write("Here you can add your behavioral and lifestyle visualizations.")

