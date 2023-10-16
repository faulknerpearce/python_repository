class Node:
    # Node constructor initializes a node with a value and an optional next_node reference.
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Returns the value of the current node.
    def get_value(self):
        return self.value

    # Returns the reference to the next node.
    def get_next_node(self):
        return self.next_node

    # Sets the reference to the next node.
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    # LinkedList constructor initializes the linked list with an optional initial value.
    def __init__(self, value=None):
        self.head_node = Node(value)

    # Returns the head node of the linked list.
    def get_head_node(self):
        return self.head_node

    # Inserts a new node at the beginning of the linked list.
    def append_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # Removes a node with a specific value from the linked list.
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()

                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    # Converts the linked list into a string representation.
    def stringify_list(self):
        my_string = []
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:  # Updated to "is not None"
                my_string.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return my_string

# This function swaps the positions of two nodes in the linked list.
def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')
    
    # Initialize variables to keep track of previous nodes for val1 and val2.
    node1_prev = None
    node2_prev = None
    
    # Start from the head of the list for both nodes.
    node1 = input_list.head_node
    node2 = input_list.head_node
    
    # If val1 and val2 are the same, there's no need to swap.
    if val1 == val2:
        print("Elements are the same - no swap needed")
        return

    # Search for the node with value val1.
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    # Search for the node with value val2.
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    # Check if either of the nodes is not in the list.
    if node1 is None or node2 is None:
        print("Swap not possible - one or more elements is not in the list")
        return

    # Adjust the references to perform the swap.
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    # Swap the next_node references to complete the node swap.
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
    
# This function will return the nth last element of a singly linked list.
def nth_last_node(linked_list, n):
  count = 1
  current = None
  tail_node = linked_list.head_node

  while tail_node:
      tail_node = tail_node.get_next_node()
      count += 1

      if count >= n + 1:
          if current is None:
              current = linked_list.head_node
          else:
              current = current.get_next_node()
  return current

# This function will return the middle node from a linked list.
def find_middle(linked_list):
  count = 0
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if count % 2 != 0:
      slow = slow.get_next_node()
    count += 1
  return slow

# This function will create a linked list.
def generate_test_linked_list(n):
  linked_list = LinkedList()
  for i in range(n, 0, -1):
    linked_list.append_node(i)
  return linked_list

# Tests for the code: 
test_linked_list = generate_test_linked_list(10)
print(test_linked_list.stringify_list())

middle_element = find_middle(test_linked_list)
print(middle_element.value)