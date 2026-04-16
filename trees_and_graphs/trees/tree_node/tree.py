class TreeNode:
  #Initializes a new instance of a tree node with a given value and an empty list of children.
  def __init__(self, value):
    self.value = value
    self.children = []
  
  # Adds a child node to the current node.
  def add_child(self, child_node):
    print(f'Adding {child_node.value}.')
    self.children.append(child_node)

  # Removes a child node from the current node.
  def remove_child(self, child_node):
    print(f'Removing {child_node.value} from {self.value}.')

    self.children = [child for child in self.children if child is not child_node]
  
  # Traverses the tree in a depth-first manner, printing the values of the nodes.
  def traverse(self):
    print("Traversing.")
    nodes_to_visit = [self]

    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


