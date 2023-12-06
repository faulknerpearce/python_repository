from node import Node

class Queue:

  def __init__(self, max_size=None, size=0):
    # Initialize a new Queue with an optional maximum size.
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = size
  
  # Adds a new node with the given value to the end of the queue.
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
  
  # Removes and returns the value of the node at the front of the queue.
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")

  # Get the value of the head of the queue without removing it.
  def peek(self):
    if not self.is_empty():
      return self.head.get_value()
  
  # Get the current size of the queue.
  def get_size(self):
    return self.size

  # Check if the queue has available space based on the maximum size.
  def has_space(self):
    if self.max_size == None:
        return True
    else:
      return self.size < self.max_size
    
  # Check if the queue is empty.
  def is_empty(self):
    if self.size == 0:
      return True
    return False
