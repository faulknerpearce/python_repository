# Word Count
A Python script that counts the occurrence of each word in an input sentence.

## Overview
This script processes a sentence entered by the user to:

- Split into individual words
- Remove punctuation
- Count frequency of each word
- Print the word with the highest count

## Key Functions

 `split_sentence()`
- Splits an input sentence into a list of words.
- removes common punctuation marks such as commas and periods.

 `update_words()`
- Increments word counts in a dictionary.
- If the word already exists in the dictionary, it increments the count.
- If the word is not in the dictionary, it adds it with a count of 1.


## Usage
Run the script and input a sentence when prompted.
It will print the word with the highest count.
