# trigrams

**Author**: Megan Flood and Han Bao
**Version**: 1.0.0


## Overview
Trigram analysis is very simple. Look at each set of three adjacent words in a document. Use the first two words of the set as a key, and remember the fact that the third word followed that key. Once you’ve finished, you know the list of individual words that can follow each two word sequence in the document.

The trigram function takes two argument:
1. relative path to the file
2. number of words you wish to return


## Getting Started
Can be run directly from the trigrams.py file.

OR

``` python trigrams.py some_book.txt 500 > my_submission.txt```


## Architecture
Written in Python, used pytest, pytest-cov, pytest-watch modules testing.
Use setup to created the package.


## Change Log
10-20-2017 2:00pm - Created the trigrams function and designed tests for various scenarios
