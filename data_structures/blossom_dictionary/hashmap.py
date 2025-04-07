from linkedlist import Node, LinkedList

class HashMap:
  # Initialize a HashMap with the specified array size.
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for number in range(array_size)]
  
  # Generate a hash code for the given key with optional collision count.
  def hash(self, key, collisions=0):
    encoded_key = key.encode()
    hash_code = sum(encoded_key)
    return hash_code + collisions
  
  # Reduce the hash code to fit within the array size.
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  # Assign a key-value pair to the HashMap using a linkedlist.
  def assign(self, key, value):
    array_index = self.find_index(key)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return 
    list_at_array.insert(payload)
  
  # Retrieve the value associated with a key from the HashMap
  def retrieve(self, key):
    array_index = self.find_index(key)
    list_at_index = self.array[array_index]
   
    for item in list_at_index:
      if key == item[0]:
        return item[1]
    return None

  # Find the array index for a given key.
  def find_index(self, key):
    ar_index = self.compress(self.hash(key))
    return ar_index
  

