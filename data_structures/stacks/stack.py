from node import Node

class Stack:
  
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  # Adds an item to the top of the stack.
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print('The stack is full.')

  # Removes the top item from the stack.
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The stack is empty.")
   
  # Returns the value of the top item in the stack.
  def peek(self):
    if not self.is_empty():
     return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0