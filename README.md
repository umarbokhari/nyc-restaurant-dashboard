# NYC Restaurant Inspection Dashboard

## Project Overview

This project is an interactive Exploratory Data Analysis (EDA) dashboard developed using Python, Pandas, Matplotlib, Seaborn, Plotly, and Streamlit.

The dashboard analyzes the New York City Restaurant Inspection dataset and presents meaningful insights through interactive visualizations, KPI cards, dynamic filters, and business intelligence features.

The primary objective of this project is to transform raw restaurant inspection data into an organized, user-friendly, and professional analytics platform that enables users to explore inspection trends, restaurant performance, borough-wise analysis, cuisine distributions, and critical violations.

---

## Live Dashboard Deployment

The dashboard has been successfully deployed online using Streamlit Cloud.

🔗 **Live Dashboard Link:**  
(https://nyc-restaurant-dashboard-f9vzbijssiwqgcjfvzwbky.streamlit.app/)

---

## Features

### Interactive Dashboard Features

- Dynamic sidebar filters connected to all charts
- Multi-select borough filtering
- Numerical score range filtering
- Date range filtering
- Search functionality for restaurants
- Reset / Clear Filters option
- Download filtered dataset functionality

### Dashboard Components

- KPI Summary Cards
- Responsive Tab-Based Layout
- Business Intelligence Section
- Interactive Plotly Visualizations
- Professional Dark Theme UI
- Dynamic Ranking Tables

### Data Analysis Features

- Data cleaning and preprocessing using Pandas
- Missing value handling
- Duplicate record removal
- Date conversion and transformation
- Statistical and categorical analysis

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Git & GitHub
- Streamlit Cloud

---

## Required Chart Types Included

The dashboard successfully implements all required chart types:

- Pie Chart
- Histogram
- Line Chart
- Bar Chart
- Scatter Plot
- Box Plot
- Heatmap
- Area Chart
- Count Plot
- Violin Plot

Additional advanced analytical sections were also implemented to improve dashboard usability and professionalism.

---

## Project Structure

```plaintext
dashboard_project/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   ├── DOHMH_New_York_City_Restaurant_Inspection_Results.csv
│   └── sample_restaurant_data.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── app.py
├── charts.py
├── filters.py
├── sample_creator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/nyc-restaurant-dashboard.git
```

### Step 2: Open Project Folder

Open the project folder using VS Code or any Python IDE.

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Dashboard

```bash
streamlit run app.py
```

---

## Dataset Note

The original NYC Restaurant Inspection dataset exceeded GitHub's upload size limitations.

For deployment optimization and improved cloud performance, a representative sampled dataset (`sample_restaurant_data.csv`) was used in the deployed dashboard version, while the complete dataset was used during local development and exploratory analysis.

This approach improves:

- Deployment compatibility
- Dashboard loading speed
- Cloud performance
- GitHub integration

---

## Dashboard Functionalities

### Filtering Features

- Borough Filtering
- Cuisine Filtering
- Numerical Range Filtering
- Date Range Filtering
- Search-Based Filtering
- Dynamic Linked Filters

### Business Intelligence Features

- Top 10 Restaurants with Highest Inspection Scores
- Most Common Cuisine Analysis
- KPI Monitoring
- Statistical Distribution Insights

### Interactive Features

- Interactive Plotly Charts
- Hover-Based Visualizations
- Dynamic Chart Updates
- Downloadable Filtered Dataset

---

## Key Insights

Some major insights obtained from the dataset include:

- Manhattan contains the highest number of restaurant inspections.
- Certain cuisine categories show consistently higher inspection scores.
- Critical violations are concentrated within specific boroughs.
- Inspection score distributions reveal multiple outliers.
- Restaurant inspection trends vary significantly over time.
- Certain restaurant categories repeatedly appear among high-risk establishments.

---

## Dashboard Tabs

### Overview

Contains general distribution and categorical analysis visualizations.

### Trends

Displays temporal inspection trends and cumulative score patterns.

### Correlations

Highlights relationships between numerical variables using scatter plots and heatmaps.

### Advanced Insights

Includes advanced statistical charts such as box plots and violin plots.

### Business Intelligence

Provides ranking-based analytical insights including top restaurants and cuisine distributions.

---

## Cloud Deployment

The dashboard was deployed using Streamlit Cloud with GitHub integration for continuous deployment and online accessibility.

Deployment Workflow:

1. Local Development
2. GitHub Repository Integration
3. Streamlit Cloud Deployment
4. Live Dashboard Hosting

---

## Future Improvements

Potential future enhancements include:

- Machine Learning prediction models
- Real-time API integration
- Database connectivity
- Geographical map visualizations
- User authentication system
- Advanced analytics and forecasting
- Automated reporting functionality
- Power BI style advanced KPI tracking

---

## Author

### Umar Bokhari

Exploratory Data Analysis Project

Instructor: **Ali Hassan Sherazi**

University Course: **Exploratory Data Analysis**

Year: **2026**

---

## Acknowledgements

Special thanks to:

- NYC Open Data
- Streamlit
- Plotly
- Pandas & Seaborn libraries
- Course Instructor and Teaching Staff
