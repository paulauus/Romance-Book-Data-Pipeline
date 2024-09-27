"""A script to process book data."""

import argparse
import sqlite3
import re
import pandas as pd


def clean_title(title):
    """Remove any text in brackets from the title."""
    if pd.isna(title) or not isinstance(title, str) or title.strip() == "":
        return None
    return re.sub(r'\s*\[.*?\]\s*|\s*\(.*?\)\s*', '', title).strip()


def get_author_name(author_id):
    """Retrieve the author name from the SQLite database."""
    connection = sqlite3.connect('data/authors.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM author WHERE id=?", (author_id,))
    result = cursor.fetchone()
    connection.close()
    # Remove extra spaces from names
    return " ".join(result[0].split()) if result else None


def clean_numeric_int(value):
    """Clean numeric values by removing commas, backticks, and other unwanted characters."""
    if pd.isna(value):
        return None
    # Remove backticks and commas, and convert to float
    value = re.sub(r'[`,]', '', str(value))
    try:
        return int(value)
    except ValueError:
        return None


def clean_numeric_float(value):
    """Turn a string into a float."""
    return float(value.replace(",", "."))


def process_raw_data(file_path):
    """Process the raw CSV file and output the cleaned data."""
    # Load the raw data
    df = pd.read_csv(file_path)

    # Clean the data
    df['book_title'] = df['book_title'].apply(clean_title)
    df['author_name'] = df['author_id'].apply(get_author_name)

    # Remove rows with missing title or author
    df = df.dropna(subset=['book_title', 'author_name'])

    # Clean and convert numeric columns
    df['ratings'] = df['ratings'].apply(clean_numeric_int)
    df['Rating'] = df['Rating'].apply(clean_numeric_float)

    # Select required columns and rename them
    df = df[['book_title', 'author_name', 'Year released', 'Rating', 'ratings']]
    df.columns = ['title', 'author_name', 'year', 'rating', 'ratings']

    # Sort by rating in descending order
    df = df.sort_values(by='rating', ascending=False).dropna()

    # Save the cleaned data to a new CSV file
    output_file = 'data/PROCESSED_DATA.csv'
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process raw book data CSV.")
    parser.add_argument('file_path', type=str,
                        help="Path to the raw data CSV file.")

    args = parser.parse_args()

    process_raw_data(args.file_path)
