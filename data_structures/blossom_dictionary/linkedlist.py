class Node:
  # Initialize a node with the given value.
  def __init__(self, value):
    self.value = value
    self.next_node = None

  # Retrieve and return the value of this node.
  def get_value(self):
    return self.value
  
  # Get the next node connected to this node.
  def get_next_node(self):
    return self.next_node
  
  # Set the next node connected to this node.
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  # Initialize a linked list with an optional head node.
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  # Insert a new node into the linked list.
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node
  
  # Iterate through the linked list nodes and yield their values.
  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()