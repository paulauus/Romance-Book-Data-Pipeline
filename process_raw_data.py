"""A script to process book data."""

import argparse
import os
import sqlite3
import re
import pandas as pd


def clean_title(title):
    """Remove any text in brackets from the title."""
    if pd.isna(title) or not isinstance(title, str):
        return ""
    return re.sub(r'\s*\[.*?\]\s*|\s*\(.*?\)\s*', '', title).strip()


def get_author_name(author_id):
    """Retrieve the author name from the SQLite database."""
    connection = sqlite3.connect('data/authors.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM author WHERE id=?", (author_id,))
    result = cursor.fetchone()
    connection.close()
    return result[0] if result else None

if __name__ == "__main__":
    print(clean_title("Five Feet Apart(ebook)"))
    print(get_author_name(10))
