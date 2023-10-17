import random, sys, time, json, os
# Class for creating weapons.  
class Weapon:
    # Sword attributes. 
    def __init__(self, _light_damage, _heavy_damage, _level, _xp):
        self.level = _level
        self.xp = _xp 
        self.light_damage = _light_damage * self.level
        self.heavy_damage = _heavy_damage * self.level

    # This method is used to increase the level on the weapon. 
    def level_up(self):
      self.level += 1
      delayed_print(f"Your sword has increased to: level {self.level}.")
    
    # This method will increase the weapon level if the current experience is greater than the required experience. 
    def check_xp(self):
        required_xp = self.level * 10
        if self.xp > required_xp:
            self.xp -= required_xp
            self.level_up()

    def add_xp(self, _xp):
        self.xp += _xp

# Class for creating the player and opponents.
class Character:
    # Create attributes for the character. 
    def __init__(self, _name, _health, _race, _level, _weapon):
        self.name = _name 
        self.health = _health
        self.race = _race
        self.level = _level
        self.weapon = _weapon
    
    # This will print information about the Player if they are a human, otherwise it will print the information about the Enemy NPC.
    def __repr__(self):
        if self.race == "Human":
            return f"This characters name is {self.name}, thier level is {self.level} and their current health points are {self.health}."
        else:
            return f"This is a level {self.level} {self.name}."
    
    # This is a the characters methond for attacking.
    def attack(self, _opponent, _attack_tactic):
        if _attack_tactic == "Light":
        # Light attack damage. 
            damage = self.weapon.light_damage
            _opponent.health -= damage
        else:
            # Heavy attack damage.
            damage = self.weapon.heavy_damage
            _opponent.health -= damage
        return damage
    
    # This method is for the characters defence.          
    def block(self, _opponent, _attack_key):
        # adjusted attack rate for light and heavy attack.
        attack_rate = {"Light": 0.6, "Heavy": 0.3, "Parry": 0.4}
        adjusted_rate = attack_rate.get(_attack_key, 1)
    
        # Calculate the success rate for defense based on skill level difference and attack style.
        success_rate = min(1.0, max(0.0, 0.3 + (self.level - _opponent.level) * 0.1 + adjusted_rate)) 
        
        # If the random flaot is greater than the success rate this will return True.
        defence = round(random.random(),1) >= success_rate
        return defence
    
     # This method will return the result of the players parry attempt.
    def parry(self, _enemy):
            damage_to_enemy = random.randint(self.weapon.light_damage, self.weapon.heavy_damage)
            _enemy.health -= damage_to_enemy
            return damage_to_enemy

# This function will delay text that is outputed to the terminal. 
def delayed_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    # Add a newline character at the end of the text
    sys.stdout.write('\n')
    sys.stdout.flush()

# This function will delay test that is output to the terminal and retrun the inputed value. 
def delayed_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    return input()

# This fucntion creates an instance of the character and sword. 
def create_player():
    sword = Weapon(10, 20, 1, 0)
    name = delayed_input("\nPlease enter you characters name: ")
    created_player = Character(name, 50, "Human", 1, sword)
    return created_player

# This function will create an instance of a goblin that is the same level as the player. 
def create_goblin():
    sword = Weapon(10, 20, 1, 0)
    created_goblin = Character("Goblin", 50, "Goblin", 1, sword) 
    return created_goblin

# This function is called if block is False and will output different statements for the player or the opponent. 
def output_if_not_block(_attacker, _opponent, _tactic, _damage):
    if _attacker.race == "Human":
        delayed_print(f"\nYour {_tactic} Attack was successful, you have reduced the {_opponent.name}'s Health by {_damage} points.") 
    else:
        delayed_print(f"\nYour block was unsuccessful. The {_attacker.name} reduced your Health by {_damage} points.")

# This function is called if block is True and will output different statements for the player or the opponent.
def output_if_block(_attacker, _opponent, _tactic):
    if _attacker.race == "Human":
        delayed_print(f"\nThe {_opponent.name} blocked your {_tactic} Attack.")
    elif _opponent.race == "Human":
        delayed_print(f"\nYou successfully blocked the {_attacker.name}'s {_tactic} Attack.")

# This fucntion will use a int as a key for a dictionary and retrun the associated word. 
def convert_int_to_word(player_choice):
    attacks = {1: "Light", 2: "Heavy", 3: "Block", 4: "Parry"}
    return attacks.get(int(player_choice), 3)

def character_combat(_attacker, _opponent, _attack_tactic):
    # If the opponents block is False, then reduce opponents health by the calculated damage of the attack (Light or Heavy). 
    if not _opponent.block(_attacker, _attack_tactic):
        damage_points = _attacker.attack(_opponent, _attack_tactic)
        _attacker.weapon.add_xp(damage_points /2)
        output_if_not_block(_attacker, _opponent, _attack_tactic, damage_points)
    
    # Otherwise no damage is dealt to the opponent and the attackers turn is over. 
    else:
       output_if_block(_attacker, _opponent, _attack_tactic)

# This function is used to parry against an attack. 
def parry(_defender, _opponent, defender_tactic):
    if not _opponent.block(_defender, defender_tactic):
        damage_to_enemy = _defender.parry(_opponent)
        # Add weapon xp for successful hit 
        _defender.weapon.add_xp(damage_to_enemy /2)
        delayed_print(f"\nYour {defender_tactic} was succsessful, and you delt {damage_to_enemy} points of damage to the {_opponent.name}")
    else:
        damage_to_player = _opponent.parry(_defender)
        delayed_print(f"\nYour {defender_tactic} was unsuccessful and the {_opponent.name} reduced your health by {damage_to_player} points.")

# This fucntion will return the NPC's randomly selected attack choice, in the form of a string "Light" or "Heavy" attack.
def enemy_random_attack():
    num = random.randint(1,2)
    word = convert_int_to_word(num)
    return word

# This function will delay text that is outputed to the terminal. 
def delayed_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    # Add a newline character at the end of the text
    sys.stdout.write('\n')
    sys.stdout.flush()

# This function will delay test that is output to the terminal and retrun the inputed value. 
def delayed_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    return input()

# This will save the players character data (Only to be used for one player it will overwrite all data in the JSON file.) light_damage, _heavy_damage, level, xp
def save_character(player):
    player_stats = {"Name": player.name, "Health": player.health, "Race": player.race, "Level": player.level, "Weapon": {"Light": player.weapon.light_damage, "Heavy": player.weapon.heavy_damage, "Level": player.weapon.level, "XP": player.weapon.xp}}
    with open("player_data.json", "w") as player_data:
        json.dump(player_stats, player_data)

# This will load the player character data from a JSON file. 
def get_saved_character():
    choice = '2'
    character = None
    if os.path.isfile("player_data.json"):
        with open("player_data.json", "r") as player_data:
            character = json.load(player_data)
        
        while choice != '1' and choice != '2':
            choice = input(f'Available saved charater: {character["Name"]}, Level {character["Level"]}.\nPress 1 to load this character, Press 2 to play a new game.')
    else:
        print('No saved character data found.\nStarting a new game.......')
    return choice, character

# This function will Load a players character and weapon from a dictionary of characters data.
def load_player(data):
    saved_weapon = Weapon(data['Weapon']['Light'], data['Weapon']['Heavy'], data['Weapon']['Level'], data['Weapon']['XP'])
    saved_player = Character(data['Name'], data['Health'], data['Race'], data['Level'], saved_weapon)
    return saved_player

def level_one(_player, _goblin):

    delayed_print(f"\nWelcome to the Arena\nYou are facing a level {_goblin.level} {_goblin.race}.")

    while _player.health > 0 and _goblin.health > 0:

        if _player.health > 0 and _goblin.health > 0:

            # Players attacking choice. 
            choice = delayed_input(f"\nIt is your turn to attack the {_goblin.name}\nPress 1 to perform a Light Attack or Press 2 to perform a Heavy Attack: ")
    
            # Ensure that the input is only either the number 1 or 2. 
            while choice != "1" and choice!= "2":
                delayed_print("\nIncorrect input for your attack, Try again.")
                choice = delayed_input("Press 1 to perform a Light Attack or 2 to perform a Heavy Attack: ")
    
            player_attack_tactic = convert_int_to_word(int(choice))
    
            # Player's attacking trun.   
            character_combat(_player, _goblin, player_attack_tactic)
        else:
            break

        if _player.health > 0 and _goblin.health > 0:

            choice = delayed_input(f"\nThe {_goblin.name} is about to attack you! \nPress 3 to attempt to block the attack, Press 4 to attempt a parry: ")
    
            # Ensure that the input is only either the number 3 or 4. 

            while choice != "3" and choice != "4":
                delayed_print("\nIncorect input for your defence, try again.")
                choice = delayed_input("Press 3 to block, Press 4 to parry: ")
 
            # Get the NPC's randomly selected attack. 
            enemy_attacking_tactic = enemy_random_attack()

            player_defence_tactic = convert_int_to_word(int(choice))
    
            # Player's defending turn. 
            if player_defence_tactic == "Block":
                character_combat(_goblin, _player, enemy_attacking_tactic)
        
            else:
                parry(_player, _goblin, player_defence_tactic)
                
        else:
            break

        delayed_print(f"\nYou have {_player.health} health points remaining,")
        delayed_print(f"and the {_goblin.name} has {_goblin.health} health points remaining.")

# Game main menu
delayed_print(f"welcome to the Gladiators game.")
keyboard = delayed_input("Press 1 to start a new game. Press 2 to continue from a saved game. ")

if keyboard == "2":
    choice, characters = get_saved_character()

else: 
    choice = '2'  

# Begining of the new game. 
if choice == '2': 
    delayed_print("\nYou slowly open your eyes, trying to adjust to the darkness. \nYou feel a cold metal chain around your wrist, and as you try to move, you realize you're chained to a wall. \nSuddenly, you hear heavy footsteps approaching. A prison guard bursts into the room, his eyes scanning the cell. \n'On your feet, maggot!' he barks, his voice echoing through the walls.")
    delayed_print("\nYou struggle to stand up, your legs weak from being chained for so long. The guard unlocks your chains and drags you out of the cell. \nYou're pushed into a dimly lit arena, surrounded by cheering crowds. The guard turns to you and asks, 'What is your name?'")

    player = create_player()
    goblin = create_goblin()

    # This is the players first combat level in the game. 
    level_one(player, goblin)
else: 
    pass
    # Load saved character. 
    #player = load_player()

# Print the results of the fight. 
if player.health <= 0:
    delayed_print("\nGame Over! You were defeated by the Goblin.")
else:
    delayed_print("\nCongratulations! You defeated the Goblin.")
    save_character(player)
    player.weapon.check_xp()