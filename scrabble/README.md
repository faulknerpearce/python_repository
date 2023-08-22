# Scrabble Scorer
This program calculates Scrabble scores for players and words using point values from a dictionary.

## Overview

The script does the following:
- Defines point values for each letter in a dictionary
- Contains a function to calculate score for a word by summing letter values
- Stores player names and words in a nested dictionary
- Loops through player words to calculate per-player score
- Allows scoring additional words entered for a player
- Outputs updated scores after entering a new word

## Code Overview
Point Value Dictionary

Defines a list of letters and corresponding point values
Zips into a dictionary with letter:point pairs
Adds blank tile point value of 0

### score_word()
- Accepts a word and points dictionary
- Sums points for each letter after uppercasing
- Uses dictionary .get() method for non-letter characters
- Returns total score

### get_player_score()
- Accepts player name, profiles dict, points dict
- Loops through player's words in profiles
- Sums score per word using score_word()
- Returns total player score


### play_another_word()
- Accepts new word, player name, profiles dict, points dict
- Calculates score for new word and adds to player's score
- Returns updated profiles dict
- Usage
- Update player words in the nested dict
