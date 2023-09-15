import random

# The Class for creating the player and opponents.
class Character:
    # Create attributes for the character. 
    def __init__(self, name, health, weapon, race, level):
        self.name = name 
        self.health = health
        self.weapon = weapon
        self.race = race
        self.level = level
    
    # This will print information about the Player if they are a human, otherwise it will print the information about the Enemy NPC.
    def __repr__(self):
        if self.race == "Human":
            return f"This characters name is {self.name}, thier level is {self.level} and their current health points are {self.health}."
        else:
            return f"This is a level {self.level} {self.name}."
    
    # This is a the characters methond for attacking.
    def attack(self, opponent, attack_style):
        if attack_style == "Light":
        # Light attack damage. 
            damage = self.weapon.light_damage
            opponent.health -= damage
        else:
            # Heavy attack damage.
            damage = self.weapon.heavy_damage
            opponent.health -= damage
        return damage
    
    # This method is for the characters defence.          
    def block(self, opponent, attack_key):
        # adjusted attack rate for light and heavy attack.
        attack_rate = {"Light": 0.5, "Heavy": 0.3}
        adjusted_rate = attack_rate.get(attack_key, 0.3)
    
        # Calculate the success rate for defense based on skill level difference and attack style.
        success_rate = min(1.0, max(0.0, 0.3 + (self.level - opponent.level) * 0.1 + adjusted_rate)) 
        print(f"seccsess rate: {success_rate}")
        
        # If the random flaot is greater than the success rate this will return True.
        defence = round(random.random(),1) > success_rate
        return defence
    
    def defend_parry():
        pass
    
# This is a class for creating weapons.  
class Weapon:
    # Sword attributes. 
    def __init__(self, light_damage, heavy_damage):
        self.light_damage = light_damage
        self.heavy_damage = heavy_damage
    
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

# This fucntion will use a int as a key for a dictionary and retrun the associated word. 
def convert_int_to_word(player_choice):
    attacks = {1: "Light", 2: "Heavy"}
    return attacks.get(int(player_choice), 3)

def attacking_turn(player, opponent, tactic):
    # If the opponents block is False, then reduce opponents health by the calculated damage of the attack (Light or Heavy). 
    if not opponent.block(player, tactic):
        damage_points = player.attack(opponent, tactic)
        print(f"Your {tactic} Attack was succsessful, you delt {damage_points} points of damage.\nOpponent remaining health points: {opponent.health}")
    
    # Otherwise no damage is dealt to the opponents and the players attacking turn is over. 
    else:
        print(f"The {opponent.name} blocked your {tactic} Attack.")

def defending_turn():
    pass

# Begining of the main game program. 
print(f"Welcome to the Arena, you have been selected for a fight to the death. \n\nPlease chose you character name.")

player = create_player()

goblin = create_goblin()

print(f"You are facing a level {goblin.level} {goblin.race}.")
while player.health > 0 and goblin.health > 0:

    # Add attack probability to this statement. 
    choice = input(f"Press 1 for a Light Attack, Press 2 for a Heavy Attack. ")
    attack = convert_int_to_word(int(choice))
    print(f"The attack word: {attack}")

    attacking_turn(player, goblin, attack)
