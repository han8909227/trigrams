"""Tests for the trigrams module."""
import pytest


def test_open_text_file():
    """Test that main function can open a file."""
    from trigrams import main
    main('test_book.txt', 1)


def test_invalid_text_file():
    """Test that main function raises exception on non-existant file."""
    from trigrams import main
    with pytest.raises(FileNotFoundError):
        main('test_text.txt', 1)


def test_zero_words_from_main():
    """Test that main funciton returns empty string for 0 words."""
    from trigrams import main
    assert main('test_book.txt', 0) == ''


SPLIT_STR = [('a', ['a']), ('a d', ['a', 'd']), ('a\nd', ['a', 'd'])]


@pytest.mark.parametrize('text, result', SPLIT_STR)
def test_text_to_list(text, result):
    """Test that book_to_list splits text into list."""
    from trigrams import book_to_list
    assert book_to_list(text) == result


DICT_TEST = [(['any', 'thing', 'else'], {'any thing': ['else']}),
             (['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might'],
             {'I wish': ['I', 'I'], 'wish I':['may', 'might'],
              'may I':['wish'], 'I may':['I']
              }
              )]


@pytest.mark.parametrize('words_list,result', DICT_TEST)
def test_make_dict(words_list, result):
    """Test with list_to_dict for first two words as key and third as value."""
    from trigrams import list_to_dict
    assert list_to_dict(words_list) == result


STR_LENGTH = [({'any thing': ['else']}, 0),
              ({'any thing': ['else']}, 1),
              ({'I wish': ['I', 'I'], 'wish I':['may', 'might'],
                'may I':['wish'], 'I may':['I']}, 10)]


@pytest.mark.parametrize('words_dict, num_word', STR_LENGTH)
def test_dictionary_to_string(words_dict, num_word):
    """Test for length of string from dictionary."""
    from trigrams import dictionary_to_string
    assert len(dictionary_to_string(words_dict, num_word).split()) == num_word


def test_empty_dictionary_for_words():
    """Test for empty string from empty dictionary."""
    from trigrams import dictionary_to_string
    assert dictionary_to_string({}, 10) == ''
