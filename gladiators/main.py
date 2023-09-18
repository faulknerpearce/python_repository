import random

# This is a class for creating weapons.  
class Weapon:
    # Sword attributes. 
    def __init__(self, light_damage, heavy_damage):
        self.light_damage = light_damage
        self.heavy_damage = heavy_damage

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
    def attack(self, opponent, chosen_attack_tactic):
        if chosen_attack_tactic == "Light":
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
        attack_rate = {"Light": 0.6, "Heavy": 0.3, "Parry": 0.4}
        adjusted_rate = attack_rate.get(attack_key, 1)
    
        # Calculate the success rate for defense based on skill level difference and attack style.
        success_rate = min(1.0, max(0.0, 0.3 + (self.level - opponent.level) * 0.1 + adjusted_rate)) 
        
        # If the random flaot is greater than the success rate this will return True.
        defence = round(random.random(),1) >= success_rate
        return defence
          
# This fucntion creates an instance of the character and sword. 
def create_player():
    sword = Weapon(10, 20)
    name = input("\nPlease enter you characters name: ")
    created_player = Character(name, 50, sword, "Human", 1)
    return created_player

# This function will create an instance of a goblin that is the same level as the player. 
def create_goblin():
    sword = Weapon(10, 20)
    created_goblin = Character("Goblin", 50, sword, "Goblin", 1)
    return created_goblin

# This function is called if block is False and will output different statements for the player or the opponent. 
def output_if_not_block(the_attacker, the_opponent, the_tactic, the_damage):
    if the_attacker.race == "Human":
        print(f"\nYour {the_tactic} Attack was succsessful, you have reduced the {the_opponent.name}'s Health by {the_damage} points.") 
    else:
        print(f"\nYour block was unsuccessful. The {the_attacker.name} reduced your Health by {the_damage} points.")

# This function is called if block is True and will output different statements for the player or the opponent.
def output_if_block(the_attacker, the_opponent, the_tactic):
    if the_attacker.race == "Human":
        print(f"\nThe {the_opponent.name} blocked your {the_tactic} Attack.")
    elif the_opponent.race == "Human":
        print(f"\nYou succsessfully blocked the {the_attacker.name}'s {the_tactic}.")

# This fucntion will use a int as a key for a dictionary and retrun the associated word. 
def convert_int_to_word(player_choice):
    attacks = {1: "Light", 2: "Heavy", 3: "Block", 4: "Parry"}
    return attacks.get(int(player_choice), 3)

def character_combat(attacker, opponent, attack_tactic):
    # If the opponents block is False, then reduce opponents health by the calculated damage of the attack (Light or Heavy). 
    if not opponent.block(attacker, attack_tactic):
        damage_points = attacker.attack(opponent, attack_tactic)
        output_if_not_block(attacker, opponent, attack_tactic, damage_points)
    
    # Otherwise no damage is dealt to the opponent and the attackers turn is over. 
    else:
       output_if_block(attacker, opponent, attack_tactic)

# This function will return the result of the players defence choice, block or parry 
def parry(defender, enemy, defender_tactic):
    if not enemy.block(defender, defender_tactic):
        damage_to_enemy = random.randint(defender.weapon.light_damage, defender.weapon.heavy_damage)
        enemy.health -= damage_to_enemy
        print(f"\nYour {defender_tactic} was succsessful, and you delt {damage_to_enemy} points of damage to the {enemy.name}")
    else:
        damage_to_player = random.randint(enemy.weapon.light_damage, enemy.weapon.heavy_damage)
        defender.health -= damage_to_player
        print(f"\nYour {defender_tactic} was unsuccessful and the {enemy.race} reduced your health by {damage_to_player} points.")

# This fucntion will return the NPC's randomly selected attack choice, in the form of a string "Light" or "Heavy" attack.
def enemy_random_attack():
    num = random.randint(1,2)
    word = convert_int_to_word(num)
    return word

# TO DO: Print some information to the player about the structure of the game and the genral rules and controls 

# Begining of the main game program. 
print("\nYou slowly open your eyes, trying to adjust to the darkness. \nYou feel a cold metal chain around your wrist, and as you try to move, you realize you're chained to a wall. \nSuddenly, you hear heavy footsteps approaching. A prison guard bursts into the room, his eyes scanning the cell. \n'On your feet, maggot!' he barks, his voice echoing through the walls.")
print("\nYou struggle to stand up, your legs weak from being chained for so long. The guard unlocks your chains and drags you out of the cell. \nYou're pushed into a dimly lit arena, surrounded by cheering crowds. The guard turns to you and asks, 'What is your name?'")

player = create_player()

goblin = create_goblin()

print(f"\nWelcome to the Arena\nYou are facing a level {goblin.level} {goblin.race}.")

while player.health > 0 and goblin.health > 0:

    # Add attack probability to this statement. 
    choice = input("\nPress 1 to perform a Light Attack or Press 2 to perform a Heavy Attack: ")
    
    # Ensure that the input is only either the number 1 or 2. 
    while choice != "1" and choice != "2":
        print("\nIncorrect input for your attack, Try again.")
        choice = input("Press 1 to perform a Light Attack or 2 to perform a Heavy Attack: ")
    
    player_attack_tactic = convert_int_to_word(int(choice))
    
    # Player's attacking turn. 
    character_combat(player, goblin, player_attack_tactic)

    choice = input("\nPress 3 to block, Press 4 to parry: ")
    
    # Ensure that the input is only either the number 3 or 4. 
    while choice != "3" and choice != "4":
        print("\nIncorect input for your defence, try again.")
        choice = input("Press 3 to block, Press 4 to parry: ")
    
    # Get the NPC's randomly selected attack. 
    enemy_attacking_tactic = enemy_random_attack()

    player_defence_tactic = convert_int_to_word(int(choice))
    
    # Player's defending turn. 
    if player_defence_tactic == "Block":
        character_combat(goblin, player, enemy_attacking_tactic)
        
    else:
        parry(player, goblin, player_defence_tactic)

    print(f"\nYou have {player.health} health points remaining,")
    print(f"and the {goblin.name} has {goblin.health} health points remaining.")

if player.health <= 0:
    print("\nGame Over! You were defeated by the Goblin.")
else:
    print("\nCongratulations! You defeated the Goblin.")