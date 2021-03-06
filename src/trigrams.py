"""Create a block of text that emulates the style of a given txt file."""
import random
import sys


def main(file_path, num_words):
    """Create a block of text from a given text file.

    Create a block of text that is the given number of words
    long that emulates the style of a given txt file.
    """
    if num_words == 0:
        return ''

    with open(file_path) as book_file:
        book_data = book_file.read()
    main_dict = list_to_dict(book_to_list(book_data))
    return dictionary_to_string(main_dict, num_words)


def book_to_list(book):
    """Split the given block of text into a list of words."""
    return book.split()


def list_to_dict(word_list):
    """Create a dictionary with a list of words."""
    word_dict = {}
    for i in range(len(word_list) - 2):
        dict_key = word_list[i] + ' ' + word_list[i + 1]
        if dict_key in word_dict:
            word_dict[dict_key].append(word_list[i + 2])
        else:
            word_dict[dict_key] = [word_list[i + 2]]
    return word_dict


def dictionary_to_string(words_dict=None, num_words=None):
    """Create a random string based on a dictionary of words."""
    if not num_words or not words_dict:
        return ''

    starting_point = random.choice(list(words_dict.keys()))
    result = starting_point.split()

    if num_words == 1:
        return result[0]

    for _ in range(num_words - 2):
        k_string = ' '.join(result[-2:])
        if k_string in words_dict:
            result.append(random.choice(words_dict[k_string]))
        else:
            words = random.choice(list(words_dict.keys()))
            result.pop()
            result += words.split()
    return ' '.join(result)


if __name__ == '__main__':  # pragma: no cover
    sys.stdout.write(main(sys.argv[1], int(sys.argv[2])))
