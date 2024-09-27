"""A script to analyse book data."""

import pandas as pd
import altair as alt
import os


def load_processed_data(file_path):
    """Load the processed data from the given CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    return pd.read_csv(file_path)

if __name__ == "__main__":
    
    print(load_processed_data("data/PROCESSED_DATA.csv"))