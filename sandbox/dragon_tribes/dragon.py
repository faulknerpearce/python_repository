
# This is my first class creation in python. 
class Dragon:
  def __init__(self, name, kind, power, health):
    self.name = name
    self.kind = kind
    self.power = power
    self.health = health
    self.tribe = []
  
  # Provide a representation of the Dragon instance.
  def __repr__(self):
    if len(self.tribe) > 0: 
      description =f"{self.name} is an {self.kind} dragon, and has a tribe size of {len(self.tribe)}."
    else:
      description = f"{self.name} is an {self.kind} dragon, and has not joined a tribe."
    return description
  
  # This function will create tribes if the dragons are alike. 
  def join_tribe(self, other_dragon):
    if other_dragon.kind == self.kind:
      self.tribe.append(other_dragon)
      print(f"{self.name} has joined a tribe with {other_dragon.name}")

      other_dragon.tribe.append(self)
    else:
      print(f"These dragons are not alike so they cannot join the tribe. ")

  # This function will increase or decrease the dragons health points. 
  def adjust_health(self, adjusted_health, damage):
    if damage == True:
      self.health -= adjusted_health
      print(f'{self.name} has lost {adjusted_health} health points.')
    else:
      self.health += adjusted_health
      print(f'{self.name} has gained {adjusted_health} health points.') 
      

first_dragon = Dragon("Ozark", "Ice", "Frost Breath", 100)

second_dragon = Dragon("Izurk", "Ice", "Ice Spikes", 100) 

first_dragon.join_tribe(second_dragon)

