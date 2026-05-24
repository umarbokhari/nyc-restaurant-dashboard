import streamlit as st
import pandas as pd
import charts  
import filters # This imports your custom modular filters.py engine!

#Adding CSS 
st.markdown("""
<style>

/* Entire App */
.stApp {
    background-color: #0F172A;
}

/* KPI Metric Cards */
[data-testid="metric-container"] {
    background: linear-gradient(145deg, #1E293B, #111827);
    border: 1px solid #00BFFF;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

/* Metric Labels */
[data-testid="metric-container"] label {
    color: white !important;
    font-size: 16px;
}

/* Metric Values */
[data-testid="metric-container"] div {
    color: #00BFFF !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
    padding: 10px 20px;
    border-radius: 10px;
}

/* Selected Tab */
button[aria-selected="true"] {
    background-color: #00BFFF !important;
    color: black !important;
}

/* Chart spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("data/sample_restaurant_data.csv")

# 1. Dashboard Layout & Standards Config
st.set_page_config(layout="wide", page_title="NYC Restaurant Inspection Insights")
st.title("🗽 NYC Restaurant Inspection Analytics Dashboard")
st.caption("Exploratory Data Analysis Final Project • Instructor: Ali Hassan Sherazi")
st.subheader("Dashboard Overview")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Average Score",
    round(df['SCORE'].mean(), 2)
)

col3.metric(
    "Total Boroughs",
    df['BORO'].nunique()
)

col4.metric(
    "Cuisine Types",
    df['CUISINE DESCRIPTION'].nunique()
)

st.markdown("---")

#tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Trends",
    "Correlations",
    "Advanced Insights",
    "Restaurant Rankings"
])

# 2. Optimized Data Loading 
@st.cache_data
def load_and_clean_dashboard_data():
    # Targets your exact dataset path inside the data folder
    df = pd.read_csv("data/sample_restaurant_data.csv")
    df.drop_duplicates(inplace=True)
    
    # Fill text columns with "Unknown" and handle types properly
    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].fillna("Unknown")
    df['SCORE'] = pd.to_numeric(df['SCORE'], errors='coerce').fillna(0)
    df['INSPECTION DATE'] = pd.to_datetime(df['INSPECTION DATE'], errors='coerce')
    df['Year'] = df['INSPECTION DATE'].dt.year
    return df

df = load_and_clean_dashboard_data()

# ==========================================
# 3. Sidebar UI Interactive Filters (All 6 Requirements Met)
# ==========================================
st.sidebar.header("🎛️ Dynamic Filter Suite")

# FILTER 6: Reset / Clear Filters
if st.sidebar.button("Reset / Clear Filters"):
    st.rerun()

st.sidebar.markdown("---")

# FILTER 1: Date / Time Range Filter
min_date = df['INSPECTION DATE'].min().date()
max_date = df['INSPECTION DATE'].max().date()
selected_date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# FILTER 2: Category Filter (Dropdown selection for single criteria)
all_flags = sorted(list(df['CRITICAL FLAG'].unique()))
selected_flag = st.sidebar.selectbox("Filter by Critical Status (Category):", options=["All"] + all_flags)

# FILTER 3: Numerical Range Slider
min_score, max_score = int(df['SCORE'].min()), int(df['SCORE'].max())
selected_score_range = st.sidebar.slider("Filter by Score Range (Numerical):", min_score, max_score, (min_score, max_score))

# FILTER 4: Multi-Select Filter (Multiple criteria selection matching)
all_boros = sorted([b for b in df['BORO'].unique() if b != "Unknown" and b != "0"])
selected_boros = st.sidebar.multiselect("Filter by Boroughs (Multi-Select):", options=all_boros, default=all_boros)

# FILTER 5: Search / Text Filter
search_keyword = st.sidebar.text_input("Search Restaurant by Name (Text Filter):", "").strip()

# ==========================================
# 4. Engine Connection: Passing data out to filters.py
# ==========================================
filtered_df = filters.apply_all_dashboard_filters(
    df, 
    selected_date_range, 
    selected_flag, 
    selected_score_range, 
    selected_boros, 
    search_keyword
)


# ==========================================
# Download Filtered Dataset
# ==========================================

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.sidebar.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name='filtered_restaurant_data.csv',
    mime='text/csv',
)

# ==========================================
# 5. Top-Level High-Impact KPI Cards
# ==========================================
st.markdown("### 📊 System Key Metrics")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Total Establishments Inspected", value=f"{len(filtered_df):,}")
kpi2.metric(label="Average Penalty Score", value=f"{filtered_df['SCORE'].mean():.1f}")
kpi3.metric(label="Critical Infractions Tracked", value=f"{len(filtered_df[filtered_df['CRITICAL FLAG'] == 'Critical']):,}")

st.markdown("---")

# ==========================================
# 6. Responsive Visual Display Grid
# ==========================================

# ======================================================
# TAB 1 — OVERVIEW
# ======================================================

with tab1:

    st.markdown("## 📌 General Overview")

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.plotly_chart(
    charts.plot_pie_chart(filtered_df),
    use_container_width=True
)
        st.info("Pie chart shows the proportional distribution of restaurant categories.")

    with row1_col2:
        st.pyplot(charts.plot_bar_chart(filtered_df))
        st.info("Bar chart visualization compares restaurant activity across boroughs.")

    st.markdown("---")

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.pyplot(charts.plot_count_plot(filtered_df))
        st.info("Count plot highlights categorical frequency distributions.")

    with row2_col2:
        st.pyplot(charts.plot_histogram(filtered_df))
        st.info("Histogram displays score distribution across inspections.")


# ======================================================
# TAB 2 — TRENDS
# ======================================================

with tab2:

    st.markdown("## 📈 Trend Analysis")

    row3_col1, row3_col2 = st.columns(2)

    with row3_col1:
        st.plotly_chart(
    charts.plot_line_chart(filtered_df),
    use_container_width=True
)
        st.info("Line chart visualizes inspection trends over time.")

    with row3_col2:
        st.pyplot(charts.plot_area_chart(filtered_df))
        st.info("Area chart emphasizes cumulative changes across years.")


# ======================================================
# TAB 3 — CORRELATIONS
# ======================================================

with tab3:

    st.markdown("## 🔗 Correlation & Relationships")

    row4_col1, row4_col2 = st.columns(2)

    with row4_col1:
        st.plotly_chart(
    charts.plot_scatter(filtered_df),
    use_container_width=True
)
        st.info("Scatter plot shows relationships between numerical variables.")

    with row4_col2:
        st.pyplot(charts.plot_correlation_heatmap(filtered_df))
        st.info("Heatmap highlights feature correlations and statistical relationships.")


# ======================================================
# TAB 4 — ADVANCED INSIGHTS
# ======================================================

with tab4:

    st.markdown("## 🧠 Advanced Statistical Insights")

    row5_col1, row5_col2 = st.columns(2)

    with row5_col1:
        st.pyplot(charts.plot_box_plot(filtered_df))
        st.info("Box plot identifies median values and potential outliers.")

    with row5_col2:
        st.pyplot(charts.plot_violin_plot(filtered_df))
        st.info("Violin plot visualizes probability density and distribution spread.")

        st.markdown("---")

st.caption(
    "Developed by Umar Bokhari • Exploratory Data Analysis Dashboard • 2026"
)

# ======================================================
# TAB 5 — TOP 10 RESTAURANTS
# ======================================================

with tab5:

    st.markdown("## 📋 Top Restaurants Rankings")

    st.info(
        "This section dynamically ranks restaurants based on filtered inspection scores."
    )

    st.subheader("🔎 Top 10 Restaurants with Highest Inspection Scores")

    top_restaurants = (
        filtered_df[['DBA', 'BORO', 'CUISINE DESCRIPTION', 'SCORE']]
        .sort_values(by='SCORE', ascending=False)
        .head(10)
    )

    st.dataframe(
        top_restaurants,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🍽️ Top 10 Most Common Cuisine Types")

    top_cuisines = (
        filtered_df['CUISINE DESCRIPTION']
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_cuisines.columns = ['Cuisine Type', 'Count']

    st.dataframe(
    top_restaurants,
    use_container_width=True
)