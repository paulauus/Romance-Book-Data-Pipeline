"""A script to get the most common keywords from book titles using spaCy."""

import pandas as pd
import altair as alt
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_keywords(title):
    """Extract keywords from a title using spaCy."""
    doc = nlp(title)
    # Extract words that are not stop words or punctuation
    keywords = [token.text.lower()
                for token in doc if not token.is_stop and not token.is_punct]
    return keywords


def get_top_keywords(df, title_column):
    """Get the top keywords from the specified book title column."""
    all_keywords = []
    for title in df[title_column].dropna():
        all_keywords.extend(extract_keywords(title))

    keyword_counts = pd.Series(all_keywords).value_counts()
    return keyword_counts.head(20)


if __name__ == "__main__":
    df = pd.read_csv('data/PROCESSED_DATA.csv')

    # Specify the correct title column name
    title_column = 'title'

    # Get the top keywords
    top_keywords = get_top_keywords(df, title_column)

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
