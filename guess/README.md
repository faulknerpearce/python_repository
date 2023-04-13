# Number Guessing Game
This Python script is a simple number guessing game. The program attempts to guess the user's chosen number between 0 and 100 within 10 tries. It uses a binary search strategy to narrow down the range of possible numbers efficiently.

## How it Works
1. The user is prompted to choose a number between 0 and 100.
2. The program initializes the bounds (min and max) to 0 and 100, respectively, and sets the initial guess to 50.
3. The program enters a loop and continues to guess the user's number until either the guess is correct, or it has reached the maximum of 10 tries.
4. In each iteration, the program asks the user if the guess is correct.
. If the guess is correct, the game ends, and the program displays a winning message.
. If the guess is incorrect, the user is prompted to indicate whether their number is below or above the current guess. Based on the user's input, the program adjusts the bounds and calculates the next guess using the binary search strategy.
5. If the program cannot guess the user's number within 10 tries, it displays a "You Win!" message.