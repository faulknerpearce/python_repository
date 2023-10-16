# Binary Search: Number Guessing Game

## Overview

The Number Guessing Game script is an interactive game where the program attempts to guess a number chosen by the user between 0 and 100. The program uses a series of smart guesses based on user feedback to narrow down the possible range and ultimately guess the correct number.

## Features

- Engage in a guessing game with the program.
- The program asks the user for feedback after each guess to refine its next guess.
- The program uses a strategy to guess numbers efficiently, reducing the search space.
- If the program can't guess the number within 10 tries, the user wins.
- Clear messages guide the user through each step of the game.
- Easily change the range of numbers (0 to 100) to suit your preferences.


## Functions

`below(guess, bound)`

- Updates the guess and bounds when the chosen number is below the current guess.
- Calculates a new guess by considering the lower bound.
- Returns the new rounded guess.

 `above(guess, bound)`

- Updates the guess and bounds when the chosen number is above the current guess.
- Calculates a new guess by considering the upper bound.
- Returns the new rounded guess.

`ask(guess)`

- Asks the user if the current guess is correct.
- Takes the current guess as input and prompts the user for confirmation.
- Returns the user's response (1 for yes, 2 for no).

`below_or_above(guess)`

- Asks the user if their chosen number is below or above the current guess.
- Takes the current guess as input and prompts the user for their choice.
- Returns the user's choice (1 for below, 2 for above).

