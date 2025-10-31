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

# --- Clean column names ---
df.columns = df.columns.str.strip()

# --- Show unique values before cleaning ---
st.write("### 🧩 Unique Values Before Cleaning")
for col in ['Attendance', 'Preparation', 'Gaming']:
    if col in df.columns:
        st.write(f"**{col}** unique values →", df[col].unique())

# --- Function to map text responses flexibly ---
def map_fuzzy(series, mapping_dict):
    series = series.astype(str).str.lower().str.strip()
    mapped = series.copy()
    for key, val in mapping_dict.items():
        mapped = mapped.mask(mapped.str.contains(key.lower(), na=False), val)
    return pd.to_numeric(mapped, errors='coerce')

# --- Apply mapping for categorical text columns ---
if 'Attendance' in df.columns:
    df['Attendance'] = map_fuzzy(df['Attendance'], {
        'poor': 1,
        'occasional': 2,
        'regular': 3,
        'good': 3,
        'average': 2,
        'low': 1,
    })

if 'Preparation' in df.columns:
    df['Preparation'] = map_fuzzy(df['Preparation'], {
        'low': 1,
        'medium': 2,
        'moderate': 2,
        'high': 3,
        'good': 3,
    })

if 'Gaming' in df.columns:
    df['Gaming'] = map_fuzzy(df['Gaming'], {
        'less': 1,
        'low': 1,
        '1-3': 2,
        'moderate': 2,
        'more': 3,
        'high': 3,
    })

# --- Safely convert numeric columns ---
for col in ['Overall', 'Attendance', 'Preparation', 'Gaming']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# --- Summary Metric Boxes ---
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Average CGPA",
    value=f"{df['Overall'].mean():.2f}" if 'Overall' in df.columns else "N/A",
    help="Average cumulative grade point average (Overall).",
    border=True
)

col2.metric(
    label="Average Attendance",
    value=f"{df['Attendance'].mean():.2f}" if 'Attendance' in df.columns else "N/A",
    help="1 = Poor, 2 = Occasional, 3 = Regular.",
    border=True
)

col3.metric(
    label="Average Study Preparation",
    value=f"{df['Preparation'].mean():.2f}" if 'Preparation' in df.columns else "N/A",
    help="1 = Low, 2 = Medium, 3 = High.",
    border=True
)

col4.metric(
    label="Average Gaming Time",
    value=f"{df['Gaming'].mean():.2f}" if 'Gaming' in df.columns else "N/A",
    help="1 = <1 hour, 2 = 1–3 hours, 3 = >3 hours daily.",
    border=True
)

# --- Legend for user interpretation ---
st.caption("""
**Scale Legend:**  
- Attendance → 1=Poor, 2=Occasional, 3=Regular  
- Study Preparation → 1=Low, 2=Medium, 3=High  
- Gaming Time → 1=Less than 1 hour, 2=1–3 hours, 3=More than 3 hours
""")

# --- Display cleaned dataset ---
st.dataframe(df)
