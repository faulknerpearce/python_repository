# Word Count Script

## Overview

The Word Count Script is a simple Python program designed to count the frequency of words in a user-entered sentence. It offers basic text processing capabilities, including word counting and removal of punctuation.

## Features

- The script counts the occurrence of each word in the input sentence.
- *It removes common punctuation marks (`,` and `.`) from the sentence.
- The script treats words in a case-insensitive manner for accurate word counting.
- The script interacts with the user to input a sentence and displays the word count results.

## Function Descriptions

`update_words(word, used_words)`

- Checks if a word exists in the `used_words` dictionary. If found, it increments the word count by 1. If not found, it adds the new word to the dictionary with a count of 1.
- Returns the updated `used_words` dictionary.

`split_sentence(sentence)`

- Takes an input sentence and performs text processing to split it into a list of words.
- Removes common punctuation marks (`,` and `.`) using regular expressions.
- Splits the sentence into words based on whitespace.
- Returns a list of cleaned words.

 `main()`

- The main function initializes an empty `words_count` dictionary to store word counts.
- Prompts the user to enter a sentence.
- Calls `split_sentence()` to clean and split the sentence into words.
- Iterates through the words, updating the `words_count` dictionary using `update_words()`.
- Displays the word count results to the user.

## Usage

1. Run the script, and it will prompt you to enter a sentence.

2. Enter the sentence you want to analyze, and the script will count the occurrence of each word, ignoring case and common punctuation.

3. View the word count results displayed by the script.

