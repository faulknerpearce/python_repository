 # This will calculate the median and decrease the max bound 
def below(guess, bound):
    num = (guess - bound[0]) / 2  
    bound[1] = guess
    guess -= num
    return round(guess)
      
# This will calculate the median and increase the min bound
def above(guess, bound): 
    num = (bound[1] - guess) / 2
    bound[0] = guess 
    guess += num 
    return round(guess)
    
def ask(guess):
    output = int(input("Is your number: " + str(guess) + "? Press(1) For yes. Press(2) For No: "))
    return output 

def below_or_above(guess):
    output = int(input("Press(1) if your number was below " + str(guess) + " Press(2) If it was above " + str(guess) +": "))
    return output

# Main 
bounds = [0, 100]
guess = 50
tries = 0
response = 2

number = int(input("Please chose a number between 0 and 100 "))

# The last task to complete: check if the guess is equal to the chosen number 
while tries < 11 and response == 2:

    response = ask(guess)

    if response == 2:
        pinpoint = below_or_above(guess)
    
    if pinpoint == 1:
        guess = below(guess, bounds)

    elif pinpoint == 2:
        guess = above(guess, bounds)

    tries += 1 

if tries < 11:
    print("I guessed your number! I win. ")

else: 
    print("I was unable to guess your number, You win. ")