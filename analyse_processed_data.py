"""A script to analyse book data."""

import pandas as pd
import altair as alt
import os


def load_processed_data(file_path):
    """Load the processed data from the given CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    return pd.read_csv(file_path)


def plot_decade_releases(df):
    """Create a pie chart showing the proportion of books released in each decade."""
    # Extract the decade from the 'year' column
    df['decade'] = (df['year'] // 10) * 10
    decade_counts = df['decade'].value_counts().reset_index()
    decade_counts.columns = ['decade', 'count']

    chart = alt.Chart(decade_counts).mark_arc().encode(
        theta=alt.Theta(field='count', type='quantitative'),
        color=alt.Color(field='decade', type='nominal'),
        tooltip=['decade', 'count']
    ).properties(
        title='Proportion of Books Released in Each Decade'
    )

    chart.save('data/decade_releases.png')

if __name__ == "__main__":
    
    data = load_processed_data("data/PROCESSED_DATA.csv")

    plot_decade_releases(data)