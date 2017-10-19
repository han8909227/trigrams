"""Create a block of text that emulates the style of a given txt file."""


def main(file_path, num_words):
    """Create a block of text from a given text file.

    Create a block of text that is the given number of words
    long that emulates the style of a given txt file.
    """
    with open(file_path) as book_file:
        book_data = book_file.read()


def book_to_list(book):
    """Split the given block of text into a list of words."""
    return book.split()
