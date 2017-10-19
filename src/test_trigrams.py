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


DICT_TEST = [(['any', 'thing', 'else'], {'any thing': ['else']}),
(['I','wish','I','may','I','wish','I','might'],
{'I wish': ['I', 'I'], 'wish I':['may', 'might'], 'may I':['wish'], 'I may':['I']
})]


@pytest.mark.parametrize('words_list,result', DICT_TEST)
def test_make_dict(words_list, result):
    """Make a test with list of words and making a dictionary for two consecutive words as key and third as value"""

    from trigrams import list_to_dict
    assert list_to_dict(words_list) == result

