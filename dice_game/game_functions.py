#This function will append the input name and give the player money to bet with
def create_player(list):
    user = input("Please create a username: ")
    list.append([user])
    money = 100
    list[0].insert(1, money)

#this function will output the dice sum 
def roll_dice():
    import random 
    diceSum = 0 
    for i in range(2):
        roll = random.randint(0,6)
        dnum = i + 1 
        print("Dice " + str(dnum) + " rolled: " + str(roll))
        diceSum += roll 
    return diceSum

#This function will check if the play if betting with more money than they have.
def check_bet_amount(bet, player):
    mybool = bool
    money = player[0][1]
    if int(bet) > money:
        print("\n\nYou do not have enough money please bet again ")
        mybool = False
    else:
        mybool = True
    return mybool

#this function will check if the player guessed the result of the dice roll. 
#if their prediction was successful the player will win the amount they bet       
def check_bet(bet_amount, bet, dice, player):
    diceval = int
    if dice % 2 == 0:
        diceval = 1
    else:
        diceval = 2
    if int(bet) == diceval:
        print("Even! You win $" + str(bet_amount))
        player[0][1] += int(bet_amount)
    else:
        print("Odd. You lose $" + str(bet_amount))
        player[0][1] -= int(bet_amount)

#This function will output the remaining balance of the players funds.  
def remining(money):
    print("You have $" + str(money[0][1]) + " available to bet with.\n\n")