# Function to update the guess and bounds when the chosen number is below the current guess
def below(guess, bound):
    num = (guess - bound[0]) / 2  
    bound[1] = guess
    guess -= num
    return round(guess)
      
# Function to update the guess and bounds when the chosen number is above the current guess
def above(guess, bound): 
    num = (bound[1] - guess) / 2
    bound[0] = guess 
    guess += num 
    return round(guess)

# Function to ask the user if the guess is correct
def ask(guess):
    output = int(input("\n\nIs your number: " + str(guess) + "? Press(1) For yes. Press(2) For No: "))
    return output 

# Function to ask the user if their number is below or above the current guess
def below_or_above(guess):
    output = int(input("If your number was below " + str(guess) + " Press(1). If Your number was above " + str(guess) + " Press(2): "))
    return output

# Initialize bounds, guess, and tries
bounds = [0, 100]
guess = 50
tries = 0
response = 2

# Prompt the user to choose a number between 0 and 100
number = int(input("\n\nPlease chose a number between 0 and 100: "))
print("If I can't guess your number in 10 tries, You win. \n\n")

# Loop until the number is guessed or the maximum number of tries is reached
while tries < 11:

    # Ask the user if the guess is correct
    response = ask(guess)

    if response == 2:
        # If the guess is incorrect, ask the user if their number is below or above the current guess
        pinpoint = below_or_above(guess)
    
        # Update the guess and bounds based on the user's input
        if pinpoint == 1:
            guess = below(guess, bounds)
        elif pinpoint == 2:
            guess = above(guess, bounds)

    # Increment the number of tries
    tries += 1 

# Check if the number was guessed correctly and display the appropriate message
if response == 1:
    print("I found your number. It was " + str(guess))
else:
    print("I could not find your number. You Win! ")
