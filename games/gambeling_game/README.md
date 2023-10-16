
# Dice Betting Game

## Overview

The Dice Betting Game is a Python script that simulates a simple betting game using dice rolls. The player can create a username, place bets on the outcome of dice rolls, and win or lose money based on their predictions.

## Features

- Create a player with a username and an initial amount of money.
- Roll two dice and display the sum of their values.
- Check if the player's bet amount is within their available funds.
- Allow the player to bet on whether the sum of the dice roll is even or odd.
- Determine the outcome of the bet and update the player's money accordingly.
- Keep track of the player's remaining funds and provide an option to continue playing or exit the game.

## Function

`create_player(player_list)`
- Creates a new player by taking a username and initializing their money with $100.
- Parameters:
  - `player_list` (list): A list that stores player information.

 `roll_dice()`
- Simulates the roll of two dice, calculates their sum, and displays the individual rolls.
- Returns:
  - `int`: The sum of the dice values.

`check_bet_amount(bet_amount, player)`
- Checks if the player's bet amount is within their available funds.
- Parameters:
  - `bet_amount` (str): The amount the player wants to bet.
  - `player` (list): The player's information, including their available money.
- Returns:
  - `bool`: True if the bet amount is valid; False otherwise.

`check_bet(bet_amount, bet, dice, player, message)`
- Checks if the player's bet matches the outcome of the dice roll (even or odd) and updates their money accordingly.
- Parameters:
  - `bet_amount` (str): The amount the player has bet.
  - `bet` (str): The player's bet (even or odd).
  - `dice` (int): The sum of the dice values.
  - `player` (list): The player's information, including their money.
  - `message` (str): The result message based on the bet outcome.

 `remaining(money)`
- Outputs the remaining balance of the player's funds.
- Parameters:
  - `money` (list): The player's money information.

 `even_or_odd(dice)`
- Determines if the sum of the dice roll is even or odd.
- Parameters:
  - `dice` (int): The sum of the dice values.
- Returns:
  - `str`: "Even!" if the sum is even, "Odd." if it's odd.
