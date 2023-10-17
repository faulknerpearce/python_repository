# Number Guessing Game 

## Overview
This Python script is designed to play a number guessing game. The program prompts the user to think of a number between 0 and 100 and then attempts to guess the number within a limited number of tries. The user provides feedback, guiding the program to adjust its guesses. The goal is for the program to guess the user's number within 10 tries.

## Features
- Interactive number guessing game with user input.
- Adaptive guessing: The program calculates a median value based on user feedback to make more informed guesses.
- Bound control: The program maintains a minimum and maximum bound for the guessing range and adjusts them with each guess.
- Limited tries: The game allows a maximum of 10 tries for the program to guess the number correctly.

## Functions and Classes

### `below(guess, bound)`
- Calculates the median value and updates the maximum bound.
- Used when the user indicates their number is below the current guess.

### `above(guess, bound)`
- Calculates the median value and updates the minimum bound.
- Used when the user indicates their number is above the current guess.

### `ask(guess)`
- Prompts the user to confirm if the program's guess is correct.
- Returns the user's response (1 for "yes" or 2 for "no").

### `below_or_above(guess)`
- Asks the user to specify whether their number is below or above the current guess.
- Returns the user's choice (1 for "below" or 2 for "above").

### Main
- Initializes the bounds (minimum and maximum) for the guessing range.
- Sets the initial guess to 50.
- Allows the user to choose a number between 0 and 100.
- Iteratively guesses the user's number and updates the bounds.
- Limits the game to a maximum of 10 tries.
- Concludes the game by declaring whether the program successfully guessed the user's number.

## Usage
1. Run the script.
2. Follow the prompts to interact with the program, providing feedback on the guesses.
3. The program will attempt to guess your number within 10 tries.