import random

class Player:
    # Create attributes for the player 
    def __init__(self, name):
        self.name = name 
        self.health = 100
        self.level = 1
        self.xp = 0
        self.weapon = None
    
    def __repr__(self):
        return f"This characters name is {self.name}, thier level is {self.level} and their curret health point are {self.health}"
    
    # Create methods for atacking, blocking, healing, and leveling up.
    def attack(self, opponent):
        damage = self.weapon.damage
        if not opponent.defend:
            opponent.health -= damage
            print(f"Your strike was successful the {opponent.name} was dealt {damage} points of damage.")
        else: 
            print(f"The {opponent.name} blocked your attack. ")
    
    def defend(self, opponent):
       # Calculate the success rate for defense based on skill level difference.
       success_rate = min(1.0, max(0.0, 0.5 + (self.level - opponent.level) * 0.1))
       
       # This generates a boolean value based on whether a random number is less than the given success rate.
       defence = random.random() < success_rate

       if defence:
           print(f"You successfully blocked the {opponent.name}'s attack.")
       else:
           print("You defence was unsuccsessful. ")
       return defence 
           
class Goblin:
    # Goblin attributes. 
    def __init__(self, level):
        self.name = "Goblin"
        self.health = 90 + (level * 10)
        self.level = level
        self.xp_value = 10 + (level * 5)

    def __repr__(self):
        return f"This is a level {self.level}, {self.name}."
    
    def attack():
        pass

    def defend(self, opponent):
       # Calculate the success rate for defense based on skill level difference.
       success_rate = min(1.0, max(0.0, 0.5 + (self.level - opponent.level) * 0.1))
       
       # This generates a boolean value based on whether a random number is less than the given success rate.
       defence = random.random() < success_rate
       return defence

# This is a class for a sword.  
class Sword:
    # Sword attributes. 
    def __init__(self):
        self.level = 0
        self.damage = 10 
        self.xp = 0

# This fucntion creates an instance of the character and sword. 
def create_player_and_sword():
    #name = input("Please enter you characters name: ")
    created_player = Player("White Knight")
    sword = Sword()
    created_player.weapon = sword
    return created_player

# This function will create an instance of a goblin that is the same level as the player. 
def create_goblin(player_level):
    created_goblin = Goblin(player_level)
    return created_goblin

# This function should check the level of the player after combat. 
def combat(the_player, the_enemy):
    print(f"You are facing a level {the_enemy.level} {the_enemy.name} in the arena.")

    choice = input(f"You can start with an attack on the {the_enemy.name}, or you can prepare to block. \nPress 1 to attack, Press 2 to block: ")

    if int(choice) == 1:
        the_enemy.defend(the_player)
        the_player.attack(the_enemy)

# Create a function for combat between the player and the enemy. 
player = create_player_and_sword()

goblin = create_goblin(player.level)

combat(player, goblin)

