import random

# The Class for creating the player and the enemies.
class Character:
    # Create attributes for the player 
    def __init__(self, name, health, weapon, race, level):
        self.name = name 
        self.health = health
        self.weapon = weapon
        self.race = race
        self.level = level
    
    def __repr__(self):
        if self.race == "Human":
            return f"This characters name is {self.name}, thier level is {self.level} and their current health points are {self.health}."
        else:
            return f"This is a level {self.level} {self.name}."
    
    # This is a methond for the characters light attack. (Higher chance of succsessful hit.) 
    def attack(self, opponent, the_style):
            if the_style == 1:
                damage = self.weapon.light_damage
                opponent.health -= damage
            else:
                damage = self.weapon.heavy_damage
                
    # This is a method for the characters heavy attack. (Lesser chance of a succsessful hit.) 
    def heavy_attack(self, opponent):
        damage = self.weapon.heavy_damage
    
    def defend_block(self, opponent, attack_style):
       
       attack_rate = {"light": 0.3, "heavy": 0.2}

       adjusted_rate = attack_rate.get(attack_style, 0.5)
    
       # Calculate the success rate for defense based on skill level difference.
       success_rate = min(1.0, max(0.0, 0.5 + (self.level - opponent.level) * 0.1 + adjusted_rate))
       # This generates a boolean value based on whether a random number is less than the given success rate.
       defence = random.random() < success_rate
       
       return defence

    def defend_parry():
        pass 

# This is a class for creating weapons.  
class Weapon:
    # Sword attributes. 
    def __init__(self, light_damage, heavy_damage):
        self.light_damage = light_damage
        self.heavy_damage = heavy_damage

    def parry(self):
        pass
      
# This fucntion creates an instance of the character and sword. 
def create_player():
    #name = input("Please enter you characters name: ")
    sword = Weapon(10, 20)
    created_player = Character("Galahad", 100, sword, "Human", 1)
    return created_player

# This function will create an instance of a goblin that is the same level as the player. 
def create_goblin():
    sword = Weapon(10, 20)
    created_goblin = Character("Goblin", 100, sword, "Goblin", 1)
    return created_goblin

def player_combat_attack(player, opponent):
        
        tactic = input("Press 1 for a Light Attack, Press 2 for a Heavy Attack.")
        if int(tactic) == 1:
            # opponents chance of succsessful block.
            if opponent.defend_block(player, "light"):
                player.attack(opponent, 1)
                print(f"Your Light Attack was sucsessful. You delt {player.weapon.light_damage} points of damage to the {opponent.name}")
            
            else:
                print(f"The {opponent.name} blocked your Light Attack.")


        else: 
            pass
            # defending logic

def player_combat_defend():
    pass

    

# This function should check the level of the player after combat. 
def arena(the_player, the_enemy):
    print(f"You are facing a level {the_enemy.level} {the_enemy.name} in the arena.")

    while the_player.health > 0 and the_enemy.health > 0:


        player_combat_attack(the_player, the_enemy)
        print(f"health of goblin: {the_enemy.health}")

        #player_combat_defend(the_player, the_enemy)
    



player = create_player()

goblin = create_goblin()

arena(player, goblin)



