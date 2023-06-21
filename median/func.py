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

