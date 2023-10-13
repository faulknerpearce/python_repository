# Linked List Operations

## Overview
This Python script provides a basic implementation of a singly linked list and includes various operations that can be performed on the linked list. A linked list is a data structure consisting of nodes where each node contains a value and a reference to the next node in the sequence. This script defines classes for nodes and linked lists and demonstrates operations like inserting, removing, swapping nodes, finding the nth last element, and determining the middle node of a linked list.

## Features

- **Node Class**: Represents a node in a singly linked list, with methods to get and set the value and reference to the next node.

- **LinkedList Class**: Represents a singly linked list with methods to insert a new node at the beginning, remove a node with a specific value, and convert the linked list into a string representation.

- **Swap Nodes**: Swaps the positions of two nodes with specified values within the linked list.

- **Find Nth Last Node**: Returns the nth last element from the linked list.

- **Find Middle Element**: Returns the middle node from the linked list.

- **Test Functions**: Includes test functions to demonstrate the functionality of the implemented classes and methods.

## Classes and Functions

### `Node`
- `__init__(self, value, next_node=None)`: Initializes a node with a given value and an optional reference to the next node.
- `get_value(self)`: Returns the value of the node.
- `get_next_node(self)`: Returns the reference to the next node.
- `set_next_node(self, next_node)`: Sets the reference to the next node.

### `LinkedList`
- `__init__(self, value=None)`: Initializes a linked list with an optional initial value.
- `get_head_node(self)`: Returns the head node of the linked list.
- `append_node(self, new_value)`: Inserts a new node at the beginning of the linked list.
- `remove_node(self, value_to_remove)`: Removes a node with a specific value from the linked list.
- `stringify_list(self)`: Converts the linked list into a string representation.

### Functions
- `swap_nodes(input_list, val1, val2)`: Swaps the positions of two nodes with specified values.
- `nth_last_node(linked_list, n)`: Returns the nth last element from the linked list.
- `find_middle(linked_list)`: Returns the middle node from the linked list.
- `generate_test_linked_list(n)`: Creates a linked list for testing purposes.

## Usage
You can use the provided classes and functions to perform various operations on singly linked lists. The included test functions demonstrate how to use these operations. Simply import the classes and functions and adapt them to your specific use case.

For example:
```python
test_linked_list = generate_test_linked_list(10)
print(test_linked_list.stringify_list())

middle_element = find_middle(test_linked_list)
print(middle_element.value)
