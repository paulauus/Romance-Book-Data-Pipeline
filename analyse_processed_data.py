"""A script to analyse book data."""

import os
import pandas as pd
import altair as alt


pastel_colors = [
    '#FFDAC1',  # Pastel Orange
    '#A3C1DA',  # Pastel Blue
    '#F9EFAF',  # Pastel Yellow
    '#B7E0B0',  # Pastel Green
    '#D1A6E2',  # Pastel Purple
    '#FFB2B2',  # Pastel Coral
    '#D3C6E5',  # Pastel Lilac
    '#d68ba5',  # Pastel Red
    '#E0B0FF',  # Mauve
    '#B2F7EF',  # Pastel Mint
]

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
        color=alt.Color(field="decade", type="nominal",
                        scale=alt.Scale(range=pastel_colors)),
        tooltip=['decade', 'count']
    ).properties(
        title='Proportion of Books Released in Each Decade'
    )

    chart.save('data/decade_releases.png')


def plot_top_authors(df):
    """Create a bar chart showing the top 10 most-rated authors."""
    top_authors = df.groupby('author_name')['ratings'].sum().reset_index()
    top_authors = top_authors.nlargest(10, 'ratings')

    chart = alt.Chart(top_authors).mark_bar(color='#E0B0FF').encode(
        x=alt.X('ratings:Q', title='Total Ratings'),
        y=alt.Y('author_name:N', sort='-x', title='Author'),
        tooltip=['author_name', 'ratings']
    ).properties(
        title='Top 10 Most-Rated Authors'
    )

    chart.save('data/top_authors.png')


if __name__ == "__main__":
    data = load_processed_data("data/PROCESSED_DATA.csv")

    plot_decade_releases(data)
    plot_top_authors(data)
