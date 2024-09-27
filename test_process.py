"""Tests for process_raw_data.py."""

import pytest
from process_raw_data import clean_title, clean_numeric_float, clean_numeric_int


def test_clean_title():
    """Tests standard title."""
    assert clean_title("Five Feet Apart(ebook)") == "Five Feet Apart"


def test_clean_title_2():
    """Tests empty title."""
    assert clean_title("") == None


def test_clean_title_3():
    """Tests non-string titles."""
    assert(clean_title(3)) == None


def test_clean_numeric_int_valid():
    """Test clean_numeric_int with a valid integer string containing commas and backticks."""
    assert clean_numeric_int("1,234`567") == 1234567


def test_clean_numeric_int_empty_string():
    """Test clean_numeric_int with an empty string."""
    assert clean_numeric_int("") is None


def test_clean_numeric_float_valid():
    """Test clean_numeric_float with a valid string containing a comma."""
    assert clean_numeric_float("3,14") == 3.14


def test_clean_numeric_float_dot():
    """Test clean_numeric_float with a valid string containing a dot."""
    assert clean_numeric_float("2.718") == 2.718


def test_clean_numeric_float_empty_string():
    """Test clean_numeric_float with an empty string."""
    with pytest.raises(ValueError):
        clean_numeric_float("")
