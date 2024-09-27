"""A script to process book data."""

import argparse
import os
import sqlite3
import re
import pandas as pd


def clean_title(title):
    """Remove any text in brackets from the title."""
    if pd.isna(title):
        return ''
    return re.sub(r'\s*\[.*?\]\s*|\s*\(.*?\)\s*', '', title).strip()

if __name__ == "__main__":
    print(clean_title("Five Feet Apart(ebook)"))
