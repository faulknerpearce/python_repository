import random

# Class for creating weapons.  
class Weapon:
    # Sword attributes. 
    def __init__(self, _light_damage, _heavy_damage, level, xp):
        self.level = level
        self.xp = xp 
        self.light_damage = _light_damage * self.level
        self.heavy_damage = _heavy_damage * self.level

    # This method is used to increase the level on the weapon. 
    def level_up(self):
      self.level += 1
      print(f"Your sword has increased to: level {self.level}.")
    
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
    def __init__(self, _name, _health, _weapon, _race, _level):
        self.name = _name 
        self.health = _health
        self.weapon = _weapon
        self.race = _race
        self.level = _level
    
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
          
# This fucntion creates an instance of the character and sword. 
def create_player():
    sword = Weapon(10, 20, 1, 0)
    name = input("\nPlease enter you characters name: ")
    created_player = Character(name, 50, sword, "Human", 1)
    return created_player

# This function will create an instance of a goblin that is the same level as the player. 
def create_goblin():
    sword = Weapon(10, 20, 1, 0)
    created_goblin = Character("Goblin", 50, sword, "Goblin", 1)
    return created_goblin

# This function is called if block is False and will output different statements for the player or the opponent. 
def output_if_not_block(_attacker, _opponent, _tactic, _damage):
    if _attacker.race == "Human":
        print(f"\nYour {_tactic} Attack was successful, you have reduced the {_opponent.name}'s Health by {_damage} points.") 
    else:
        print(f"\nYour block was unsuccessful. The {_attacker.name} reduced your Health by {_damage} points.")

# This function is called if block is True and will output different statements for the player or the opponent.
def output_if_block(_attacker, _opponent, _tactic):
    if _attacker.race == "Human":
        print(f"\nThe {_opponent.name} blocked your {_tactic} Attack.")
    elif _opponent.race == "Human":
        print(f"\nYou successfully blocked the {_attacker.name}'s {_tactic} Attack.")

# This fucntion will use a int as a key for a dictionary and retrun the associated word. 
def convert_int_to_word(player_choice):
    attacks = {1: "Light", 2: "Heavy", 3: "Block", 4: "Parry"}
    return attacks.get(int(player_choice), 3)

def character_combat(_attacker, _opponent, _attack_tactic):
    # If the opponents block is False, then reduce opponents health by the calculated damage of the attack (Light or Heavy). 
    if not _opponent.block(_attacker, _attack_tactic):
        damage_points = _attacker.attack(_opponent, _attack_tactic)
        player.weapon.add_xp(damage_points /2)
        output_if_not_block(_attacker, _opponent, _attack_tactic, damage_points)
    
    # Otherwise no damage is dealt to the opponent and the attackers turn is over. 
    else:
       output_if_block(_attacker, _opponent, _attack_tactic)

# This function is used to parry against an attack. 
def parry(_defender, _opponent, defender_tactic):
    if not _opponent.block(_defender, defender_tactic):
        damage_to_enemy = _defender.parry(_opponent)
        # Add weapon xp for successful hit 
        player.weapon.add_xp(damage_to_enemy /2)
        print(f"\nYour {defender_tactic} was succsessful, and you delt {damage_to_enemy} points of damage to the {_opponent.name}")
    else:
        damage_to_player = _opponent.parry(_defender)
        print(f"\nYour {defender_tactic} was unsuccessful and the {_opponent.name} reduced your health by {damage_to_player} points.")

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

    if player.health > 0 and goblin.health > 0:

        # Players attacking choice. 
        choice = input(f"\nIt is your turn to attack the {goblin.name}\nPress 1 to perform a Light Attack or Press 2 to perform a Heavy Attack: ")
    
        # Ensure that the input is only either the number 1 or 2. 
        while choice != "1" and choice!= "2":
            print("\nIncorrect input for your attack, Try again.")
            choice = input("Press 1 to perform a Light Attack or 2 to perform a Heavy Attack: ")
    
        player_attack_tactic = convert_int_to_word(int(choice))
    
        # Player's attacking trun.   
        character_combat(player, goblin, player_attack_tactic)
    else:
        break

    if player.health > 0 and goblin.health > 0:

        choice = input(f"\nThe {goblin.name} is about to attack you! \nPress 3 to attempt to block the attack, Press 4 to attempt a parry: ")
    
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

    else:
        break

# Print the results of the fight. 
if player.health <= 0:
    print("\nGame Over! You were defeated by the Goblin.")
else:
    print("\nCongratulations! You defeated the Goblin.")
    player.weapon.check_xp()
    
