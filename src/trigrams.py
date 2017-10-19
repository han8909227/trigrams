"""Create a block of text that emulates the style of a given txt file."""


def main(file_path, num_words):
    """Create a block of text from a given text file.

    Create a block of text that is the given number of words
    long that emulates the style of a given txt file.
    """
    with open(file_path) as book_file:
        book_data = book_file.read()
    main_dict = list_to_dict(book_to_list(book_data))


def book_to_list(book):
    """Split the given block of text into a list of words."""
    return book.split()


def list_to_dict(word_list):
    """Create a dictionary with a list of words """
    word_dict = {}
    for i in range(len(word_list) - 2):
        dict_key = word_list[i] + ' ' + word_list[i + 1]
        if dict_key in word_dict:
            word_dict[dict_key].append(word_list[i + 2])
        else:
            word_dict[dict_key] = [word_list[i + 2]]
    return word_dict

