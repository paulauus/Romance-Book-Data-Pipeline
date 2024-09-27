"""Tests for get_keywords.py."""

from get_keywords import extract_keywords


def test_extract_keywords():
    """Tests extraction process for a title."""
    assert extract_keywords("The Great Gatsby") == ["great", "gatsby"]
    assert extract_keywords("The Lord of the Rings") == ["lord", "rings"]
    assert extract_keywords("42 is the Answer") == ["42", "answer"]