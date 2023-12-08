from message_delay import delayed_input, delayed_print

class TreeNode:
  #Initializes a new instance of a tree node with a given value and an empty list of children.
  def __init__(self, name,  introduction, information=None, parent=None):
    self.name = name
    self.introduction = introduction
    self.information = information
    self.parent = parent 
    self.children = []
  
  # Adds a child node to the current node.
  def add_child(self, child_node):
    # print(f'Adding {child_node.name}.\n')
    self.children.append(child_node)
    child_node.parent = self

  # Removes a child node from the current node.
  def remove_child(self, child_node):
    delayed_print(f'Removing {child_node.name} from {self.name}.\n')

    self.children = [child for child in self.children if child is not child_node]
  
  # Breadth-first search to find a child node by name
  def find_by_name(self, name):
        queue = [self]

        while queue:
            current_node = queue.pop(0)
            if current_node.name == name:
                return current_node
            queue.extend(current_node.children)
        return None
  
  # Find the parent node and add the child to it
  def add_child_to_found_parent(self, parent_name, child_node):
        parent_node = self.find_by_name(parent_name)
        if parent_node:

            parent_node.add_child(child_node)
        else:
            delayed_print(f"Error: Parent node '{parent_name}' not found.\n")

  def print_node_information(self, current_node):
    # Print information about the node (price, rating, address) or list of children's names.
    if current_node.information is None:
        delayed_print([child.name for child in current_node.children])
    else:
        price, rating, address = current_node.information
        delayed_print('\n-------------------------------------------------------------------\n')
        delayed_print(f'Name: {current_node.name}.\nPrice: {price}/5.\nRating: {rating}/5.')
        delayed_print('\n-------------------------------------------------------------------\n')

  #Traverses the tree in breath first manner. 
  def traverse(self):
    current_node = self
    stack = []

    while len(current_node.children) >=0:
        
        delayed_print(current_node.introduction)
        self.print_node_information(current_node)

        first_letters = [child.name[:2].lower() for child in current_node.children]

        if len(current_node.children) == 0:
            choice = delayed_input('\nWould you like to go to this restaurant?\nEnter ( Yes ) for the address. ( No ) to go back. Or type ( exit ) to exit: ')
            if choice.lower() == 'yes':
                break
            
            elif choice.lower() == 'no':
                if stack:
                    current_node = stack.pop()
                else:
                    delayed_print('\nCannot go back further. Now exiting.')
                    break
            
            elif choice.lower() == 'exit':
                break
            
            else:
                delayed_print('\nInvalid choice. Try again: ')
        else:
            choice = delayed_input('\nEnter the first two letters of your choice or type back to go back: ')

            if choice.lower() not in first_letters and choice.lower() != 'back':
                delayed_print('\nInvalid choice. Try again: ')
            
            elif choice.lower() == 'back':
                if stack:
                    current_node = stack.pop()
                else:
                    delayed_print('\nCannot go back further. Now exiting.')
                    break
            else:
                choice_index = first_letters.index(choice.lower())
                chosen_child = current_node.children[choice_index]

                stack.append(current_node)
                current_node = chosen_child

    if choice.lower() == 'yes':
        delayed_print(f'Great choice. The address is {current_node.information[2]}')

    else:
        delayed_print("We are sorry you couldn't find anything you like. ")
