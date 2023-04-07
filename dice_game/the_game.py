#The player list will hold the player name and the players coins
from game_functions import create_player, roll_dice, check_bet_amount, remining, check_bet
player = []
choice = 1
count = 0
check = False

create_player(player)

print("\n\nWelcome to the game " + str(player[0][0]) +  ". You can chose to bet on the result of a dice roll.")
remining(player)

choice = input("Would you like to play? press(1) to play. Press(2) to exit ")
#This is the game loop.
while int(choice) == 1 and player[0][1] > 0:
#i have a variable called count to prevent asking the player if they want to play when entering the loop 
    if count == 1:
        choice = input("\n\nWould you like to play again? Press(1). Press(2) to exit: ")
        remining(player)
    else:
        count = 1
    if int(choice) == 1: 
       prediction = input("\n\nPlease press(1) to bet on even. Press(2) to bet on odd: ")
       #i need to add a limit of tries here 
       while check == False:
           bet_amo = input("Please enter an amount you wish to bet: ")
           check = check_bet_amount(bet_amo, player)
    
       dice = roll_dice()
    
       check_bet(bet_amo, prediction, dice, player)

if int(choice) == 1 and player[0][1] <= 0:
    print("\n\nYou are out of money... you should consider seeing a specialest")
else:
    print("\n\nThanks for playing. You leave the game with $" + str(player[0][1]))   
