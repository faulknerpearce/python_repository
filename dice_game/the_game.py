#The player list will hold the player name and the players coins
from the_game_functions import create_player, roll_dice, check_bet_amount, remaining, check_bet, even_or_odd 
player = []
choice = 1
count = 0

create_player(player)

print("\n\nWelcome to the game " + str(player[0][0]) +  ". You can chose to bet on the result of a dice roll.")
remaining(player)

choice = input("Would you like to play? press(1) to play. Press(2) to exit ")
#This is the game loop.
while int(choice) == 1 and player[0][1] > 0:
#i have a variable called count to prevent asking the player if they want to play when entering the loop 
    if count == 1:
        choice = input("\n\nWould you like to play again? Press(1). Press(2) to exit: ")
        remaining(player)
    else:
        count = 1
    if int(choice) == 1: 
       prediction = input("\n\nPlease press(1) to bet on odd. Press(2) to bet on even: ") # fix odd or even 
       #i need to add a limit of tries here 
       check = False
       while check == False:
           bet_amo = input("Please enter an amount you wish to bet: ")
           remaining(player)
           check = check_bet_amount(bet_amo, player)
    
       dice = roll_dice()

       def even_or_odd(dice):
           msg = ""
           if dice % 2 == 0:
              msg = "Even!"
           else:
            msg = "Odd."
           return msg

       msg = even_or_odd(dice)
       check_bet(bet_amo, prediction, dice, player, msg)

if int(choice) == 1 and player[0][1] <= 0:
    print("\n\nYou are out of money... you should consider seeing a specialest")
else:
    print("\n\nThanks for playing. You leave the game with $" + str(player[0][1]))   
