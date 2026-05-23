import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

# Set global professional layout and colors (Matches Assignment Guidelines)
sns.set_theme(style="whitegrid")
PALETTE = sns.color_palette("Set2")

def plot_pie_chart(df):

    borough_counts = df['BORO'].value_counts().reset_index()

    borough_counts.columns = ['BORO', 'Count']

    fig = px.pie(
        borough_counts,
        names='BORO',
        values='Count',
        title='Restaurant Distribution by Borough',
        hole=0.4
    )

    fig.update_layout(
        template='plotly_dark'
    )

    return fig

def plot_histogram(df):
    """Chart 2: Frequency distribution of violation scores"""
    fig, ax = plt.subplots(figsize=(6, 4))
    plot_df = df[df['SCORE'] > 0]
    
    sns.histplot(data=plot_df, x='SCORE', bins=30, kde=True, color='skyblue', ax=ax)
    ax.set_title("Distribution of Restaurant Inspection Scores", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("Violation Score")
    ax.set_ylabel("Frequency Count")
    return fig

def plot_bar_chart(df):
    """Chart 4: Compare top 10 cuisine types inspected"""
    fig, ax = plt.subplots(figsize=(6, 4))
    top_cuisines = df['CUISINE DESCRIPTION'].value_counts().head(10)
    
    sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette="viridis", ax=ax)
    ax.set_title("Top 10 Inspected Cuisine Types", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("Number of Inspections")
    return fig

def plot_scatter(df):

    fig = px.scatter(
        df,
        x='SCORE',
        y='CAMIS',
        color='BORO',
        hover_data=['DBA', 'CUISINE DESCRIPTION'],
        title='Inspection Score Relationships',
    )

    fig.update_layout(
        template='plotly_dark'
    )

    return fig

def plot_area_chart(df):
    """Chart 8: Cumulative trend timeline"""
    fig, ax = plt.subplots(figsize=(6, 4))
    timeline_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2026)].dropna(subset=['Year'])
    yearly_counts = timeline_df.groupby('Year').size()
    
    ax.plot(yearly_counts.index, yearly_counts.values, color="teal", alpha=0.8)
    ax.fill_between(yearly_counts.index, yearly_counts.values, color="teal", alpha=0.3)
    ax.set_title("Cumulative Inspection Volume Over Time", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("Year")
    return fig

def plot_line_chart(df):

    # Group data by year
    yearly_scores = df.groupby('Year')['SCORE'].mean().reset_index()

    fig = px.line(
        yearly_scores,
        x='Year',
        y='SCORE',
        markers=True,
        title='Average Inspection Scores Over Time'
    )

    fig.update_layout(
        template='plotly_dark',
        xaxis_title='Year',
        yaxis_title='Average Score'
    )

    return fig

def plot_box_plot(df):
    """Chart 6: Score distributions across boroughs with outliers"""
    fig, ax = plt.subplots(figsize=(6, 4))
    box_df = df[(df['BORO'] != "Unknown") & (df['SCORE'] > 0) & (df['SCORE'] <= 60)]
    
    sns.boxplot(data=box_df, x='BORO', y='SCORE', palette="Set3", ax=ax)
    ax.set_title("Violation Scores Spread by Borough", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("Borough")
    ax.set_ylabel("Score Scale")
    plt.xticks(rotation=15)
    return fig

def plot_correlation_heatmap(df):
    """Chart 7: Feature relationship metrics matrix"""
    fig, ax = plt.subplots(figsize=(6, 4))
    numeric_cols = df[['SCORE', 'Latitude', 'Longitude', 'ZIPCODE']].apply(pd.to_numeric, errors='coerce')
    corr_matrix = numeric_cols.corr()
    
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=False, ax=ax)
    ax.set_title("Numerical Feature Correlations", fontsize=11, fontweight='bold', pad=10)
    return fig

def plot_count_plot(df):
    """Chart 9: Volumetric count of critical item status flags"""
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='CRITICAL FLAG', palette="Set2", ax=ax)
    ax.set_title("Critical vs. Non-Critical Violations Count", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("Critical Flag Status")
    ax.set_ylabel("Inspection Entries Count")
    return fig

def plot_violin_plot(df):
    """Chart 10: Probability density distribution of score bands per grade"""
    fig, ax = plt.subplots(figsize=(6, 4))
    grade_df = df[df['GRADE'].isin(['A', 'B', 'C'])]
    
    sns.violinplot(data=grade_df, x='GRADE', y='SCORE', palette="Pastel1", order=['A', 'B', 'C'], ax=ax)
    ax.set_title("Violation Score Density by Letter Grade", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("Assigned Grade")
    ax.set_ylabel("Inspection Score Context")
    return fig