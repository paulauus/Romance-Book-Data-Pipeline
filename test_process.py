"""Tests for process_raw_data.py."""

from process_raw_data import clean_title


def test_clean_title():
    """Tests standard title."""
    assert clean_title("Five Feet Apart(ebook)") == "Five Feet Apart"


def test_clean_title_2():
    """Tests empty title."""
    assert clean_title("") == ""


def test_clean_title_3():
    """Tests non-string titles."""
    assert(clean_title(3)) == ""
