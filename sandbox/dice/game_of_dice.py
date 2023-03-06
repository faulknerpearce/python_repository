import random
money = 50 
lost = 0 

print("\n\nI will rool a dice. if sum of dice is even, you win the amount that you bet. ")
print("if the sum dice is odd, then you will lose the amount you bet.\n\n")
user_in = input("Would you like to play? Yes? Press(1) No? Press(2) ")

while money > 1 and int(user_in) == 1:
    #create the dice 
    dice_list = []
    i = 0 
    
    #Nested while loop to reset the dice sum. 
    while i < 2:
        dice = random.randint(1,6)
        dice_list.append(dice)
        i += 1
    
    dice_sum = 0
    for num in dice_list:
        dice_sum += num
    
    #This is the game loop.  
    print("\n\nYou have $" + str(money) + " avaliable.")
    bet = input("How much would you like to bet? $")
    
    if int(bet) > money:
        bet = 0
        print("\n\nyou do not have that much money ")
        user_in = input("Would you like to bet again? 1 for yes: ")
    elif money <= 0:
        break
    elif dice_sum % 2 == 0 and int(bet) > 0:
        money += int(bet)
        print("\n\nDice one: ("  + str(dice_list[0]) + ") Dice two: (" + str(dice_list[1]) + ") \nThe result is even! You Won $" + str(bet))
        user_in = input("\n\nWould you like to play again? Yes, press(1) No, Press(2): " )
    else:
        money += - int(bet)
        lost += int(bet)
        print("\n\nDice one: (" + str(dice_list[0]) + ") Dice two: (" + str(dice_list[1]) + ") \nThe result is odd.. You Lost $" + str(bet))
        user_in = input("\n\nWould you like to play again? press(1) for yes: " )

#Once the loop breaks, the game ends.   
if int(user_in) == 2:
    print("\n\nThanks for playing. \nYou take home $"  + str(money))

elif int(user_in) != 1 or int(user_in) != 2 and money > 0:
    print("Invalid key.")

else:
  print("You are out of money. You should consider seeing someone about your gambling addiction.\nYou lost $" + str(lost) + "\n\n")