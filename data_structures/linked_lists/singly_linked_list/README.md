# Singly Linked List Implementation

This project provides Python implementations of singly linked lists, along with various functions and classes for common operations on linked lists.

## Features

- Implementation of singly linked lists with features such as node insertion, node removal, and finding the nth last and middle nodes.
- A function to swap the positions of two nodes in a singly linked list.
- A function to find the nth last element in a singly linked list.
- A function to find the middle node in a singly linked list.
- A utility function to generate a test linked list with a specified number of elements.

## Node Class

The `Node` class represents a node in a singly linked list. It has the following attributes and methods:

- `value`: The value stored in the node.
- `next_node`: Reference to the next node in the list.

### Node Methods

- `get_value()`: Returns the value of the current node.
- `get_next_node()`: Returns the reference to the next node.
- `set_next_node(next_node)`: Sets the reference to the next node.

## LinkedList Class

The `LinkedList` class represents a singly linked list with a head node. It includes the following features and functions:

- `head_node`: Reference to the head (first) node in the list.

### LinkedList Methods

- `get_head_node()`: Returns the head node of the linked list.
- `append_node(new_value)`: Inserts a new node at the beginning of the linked list.
- `remove_node(value_to_remove)`: Removes a node with a specific value from the linked list.
- `stringify_list()`: Converts the linked list into a string representation.

### Additional Functions

- `swap_nodes(input_list, val1, val2)`: Swaps the positions of two nodes in the linked list.
- `nth_last_node(linked_list, n)`: Returns the nth last element of a singly linked list.
- `find_middle(linked_list)`: Returns the middle node from a singly linked list.
- `generate_test_linked_list(n)`: Creates a linked list with `n` elements.

These functions are valuable for performing common operations on singly linked lists and for generating test data to experiment with those operations.
