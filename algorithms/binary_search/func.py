 # Functions that will be used in the main script. 

# Function to update the guess and bounds when the chosen number is below the current guess.
def below(guess, bound):
    num = (guess - bound[0]) / 2  
    bound[1] = guess - 1
    guess -= num
    return round(guess)
      
# Function to update the guess and bounds when the chosen number is above the current guess.
def above(guess, bound): 
    num = (bound[1] - guess) / 2
    bound[0] = guess + 1
    guess += num 
    return round(guess)

# Function to ask the user if the guess is correct.
def ask(guess):
    output = int(input("\n\nIs your number: " + str(guess) + "? Press(1) For yes. Press(2) For No: "))
    return output 

# Function to ask the user if their number is below or above the current guess.
def below_or_above(guess):
    output = int(input("If your number was below " + str(guess) + " Press(1). If Your number was above " + str(guess) + " Press(2): "))
    return output

