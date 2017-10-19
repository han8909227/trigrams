"""Tests for the trigrams module."""
import pytest


def test_open_text_file():
    """Test that main function can open a file."""
    from trigrams import main
    main('test_book.txt', 0)


SPLIT_STR = [('a', ['a']), ('a d', ['a', 'd']), ('a\nd', ['a', 'd'])]


@pytest.mark.parametrize('text, result', SPLIT_STR)
def test_text_to_list(text, result):
    """Test that book_to_list splits text into list."""
    from trigrams import book_to_list
    assert book_to_list(text) == result
