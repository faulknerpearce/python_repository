# Doubly Linked List Implementation

This project provides Python implementations of doubly linked lists, along with various functions and classes for common operations on linked lists.

## Features

- Implementation of doubly linked lists with features such as node insertion, node removal, and displaying the elements.
- A function to remove the head and tail nodes from the list.
- A function to remove a node with a specific value from the list.
- A utility function to generate a test linked list with specified elements.

## Node Class

The `Node` class represents a node in a doubly linked list. It has the following attributes and methods:

- `value`: The value stored in the node.
- `next_node`: Reference to the next node in the list.
- `prev_node`: Reference to the previous node in the list.

### Node Methods

- `set_next_node(next_node)`: Sets the reference to the next node.
- `get_next_node()`: Returns the reference to the next node.
- `set_prev_node(prev_node)`: Sets the reference to the previous node.
- `get_prev_node()`: Returns the reference to the previous node.
- `get_value()`: Returns the value of the current node.

## DoublyLinkedList Class

The `DoublyLinkedList` class represents a doubly linked list with head and tail nodes. It includes the following features and functions:

- `head_node`: Reference to the head (first) node in the list.
- `tail_node`: Reference to the tail (last) node in the list.

### DoublyLinkedList Methods

- `add_to_head(new_value)`: Add a new node to the head of the linked list.
- `add_to_tail(new_value)`: Add a new node to the tail of the linked list.
- `remove_head()`: Remove the head node from the list.
- `remove_tail()`: Remove the tail node from the list.
- `remove_by_value(value_to_remove)`: Remove a node with a specific value from the list.
- `show_list()`: Display the elements in the linked list.



