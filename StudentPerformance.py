import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Assignment JIE42303 Scientific Visualization")

st.header("Assignment JIE42303 Scientific Visualization", divider="gray")
st.subheader("Dataset: Student Performance Metrics")

# --- Load Dataset from GitHub ---
csv_url = "https://raw.githubusercontent.com/adawiyahh/Assignment_JIE42303/refs/heads/main/ResearchInformation3.csv"
df = pd.read_csv(csv_url)

# --- Clean column names (just in case) ---
df.columns = df.columns.str.strip()

# --- Map text categories to numeric values for averaging ---
attendance_map = {'Poor': 1, 'Occasional': 2, 'Regular': 3}
prep_map = {'Low': 1, 'Medium': 2, 'High': 3}
gaming_map = {'Less than 1 hour': 1, '1-3 hours': 2, 'More than 3 hours': 3}

if 'Attendance' in df.columns:
    df['Attendance'] = df['Attendance'].map(attendance_map)

if 'Preparation' in df.columns:
    df['Preparation'] = df['Preparation'].map(prep_map)

if 'Gaming' in df.columns:
    df['Gaming'] = df['Gaming'].map(gaming_map)

# --- Safely convert numeric columns ---
for col in ['Overall', 'Attendance', 'Preparation', 'Gaming']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# --- Summary Metric Boxes ---
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Average CGPA",
    value=f"{df['Overall'].mean():.2f}" if 'Overall' in df.columns else "N/A",
    help="Represents the average cumulative grade point average (Overall) of students.",
    border=True
)

col2.metric(
    label="Average Attendance",
    value=f"{df['Attendance'].mean():.2f}" if 'Attendance' in df.columns else "N/A",
    help="Shows the average attendance level (1=Poor, 3=Regular).",
    border=True
)

col3.metric(
    label="Average Study Preparation",
    value=f"{df['Preparation'].mean():.2f}" if 'Preparation' in df.columns else "N/A",
    help="Average study preparation level (1=Low, 3=High).",
    border=True
)

col4.metric(
    label="Average Gaming Time",
    value=f"{df['Gaming'].mean():.2f}" if 'Gaming' in df.columns else "N/A",
    help="Average gaming frequency (1=Less than 1 hour, 3=More than 3 hours).",
    border=True
)

# --- Legend to help interpretation ---
st.caption("""
**Scale Legend:**
- Attendance → 1=Poor, 2=Occasional, 3=Regular  
- Study Preparation → 1=Low, 2=Medium, 3=High  
- Gaming Time → 1=Less than 1 hour, 2=1–3 hours, 3=More than 3 hours
""")

# --- Show dataset table ---
st.dataframe(df)
