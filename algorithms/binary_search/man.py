from func import below, above, ask, below_or_above

# Initialize bounds, guess, and tries.
bounds = [0, 100]
guess = 50
tries = 0
response = 2

# Prompt the user to choose a number between 0 and 100.
number = int(input("\n\nPlease chose a number between 0 and 100: "))
print("If I can't guess your number in 10 tries, You win. \n\n")

# Loop until the number is guessed or the maximum number of tries is reached.
while tries < 11:

    # Ask the user if the guess is correct.
    response = ask(guess)

    if response == 2:
        # If the guess is incorrect, ask the user if their number is below or above the current guess.
        pinpoint = below_or_above(guess)
    
        # Update the guess and bounds based on the user's input.
        if pinpoint == 1:
            guess = below(guess, bounds)
        elif pinpoint == 2:
            guess = above(guess, bounds)

    # Increment the number of tries.
    tries += 1 

# Check if the number was guessed correctly and display the appropriate message.
if response == 1:
    print("I found your number. It was " + str(guess))
else:
    print("I could not find your number. You Win! ")
