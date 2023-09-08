# Word Count
A Python script that counts the occurrence of each word in an input sentence.

## Overview
This script processes a sentence entered by the user to:

- Split into individual words
- Remove punctuation
- Count frequency of each word
- Print the word with the highest count

## Key Functions

### `split_sentence(sentence)`
- Splits an input sentence into a list of words.
- Parameters:
  - `sentence` (str): The input sentence to be split.
- Returns:
  - `list`: A list of individual words from the input sentence.

### `update_words(word, used_words)`
- Increments word counts in a dictionary.
- If the word already exists in the dictionary, it increments the count.
- If the word is not in the dictionary, it adds it with a count of 1.
- Parameters:
  - `word` (str): The word to be counted and updated.
  - `used_words` (dict): A dictionary that stores word counts.
- Returns:
  - `dict`: The updated dictionary with word counts. 

## Usage
Run the script and input a sentence when prompted.
It will print the word with the highest count.
