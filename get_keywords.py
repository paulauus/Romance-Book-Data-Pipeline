"""A script to get the most common keywords from book titles."""

import pandas as pd
import altair as alt
import re


def extract_keywords(title):
    """Extract keywords from a title."""
    # Convert title to lowercase and split into words, removing punctuation
    words = re.findall(r'\b\w+\b', title.lower())
    return words


def get_top_keywords(df):
    """Get the top keywords from the book titles."""
    all_keywords = []
    for title in df['title'].dropna():
        all_keywords.extend(extract_keywords(title))

    keyword_counts = pd.Series(all_keywords).value_counts()
    return keyword_counts.head(20)


if __name__ == "__main__":
    df = pd.read_csv('data/PROCESSED_DATA.csv')

    # Get the top keywords
    top_keywords = get_top_keywords(df)

    # Create a DataFrame for plotting
    keywords_df = top_keywords.reset_index()
    keywords_df.columns = ['keyword', 'count']

    # Create a bar chart using Altair
    chart = alt.Chart(keywords_df).mark_bar(color='#E0B0FF').encode(
        x=alt.X('keyword', sort='-y', title='Keyword'),
        y=alt.Y('count', title='Count'),
        tooltip=['keyword', 'count']
    ).properties(
        title='Top 20 Keywords from Book Titles',
        width=800,
        height=400
    )

    chart.save('data/top_keywords.png')
