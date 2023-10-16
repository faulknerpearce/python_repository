# Doubly Linked List Implementation

## Overview
This Python script provides an implementation of a doubly linked list using two classes: `Node` and `DoublyLinkedList`. A doubly linked list is a data structure in which elements are connected by two references, one to the next element, and one to the previous element. This script allows you to create and manipulate doubly linked lists efficiently.

## Features
- Creation of a doubly linked list with head and tail nodes.
- Adding elements to the head or tail of the linked list.
- Removing elements from the head, tail, or by a specific value.
- Displaying the elements in the linked list.

## Functions and Classes

### `Node` Class
- **Description**: Represents a node in a doubly linked list.
- **Constructor**:
    - `__init__(self, value, next_node=None, prev_node=None)`: Initializes a node with the specified value and optional references to the next and previous nodes.
- **Methods**:
    - `set_next_node(self, next_node)`: Sets the reference to the next node.
    - `get_next_node(self)`: Returns the reference to the next node.
    - `set_prev_node(self, prev_node)`: Sets the reference to the previous node.
    - `get_prev_node(self)`: Returns the reference to the previous node.
    - `get_value(self)`: Returns the value of the current node.

### `DoublyLinkedList` Class
- **Description**: Represents a doubly linked list with head and tail nodes.
- **Constructor**:
    - `__init__(self, head_node=None, tail_node=None)`: Initializes a doubly linked list with optional head and tail nodes.
- **Methods**:
    - `add_to_head(self, new_value)`: Adds a new node with the specified value to the head of the linked list.
    - `add_to_tail(self, new_value)`: Adds a new node with the specified value to the tail of the linked list.
    - `remove_head(self)`: Removes the head node from the linked list.
    - `remove_tail(self)`: Removes the tail node from the linked list.
    - `remove_by_value(self, value_to_remove)`: Removes a specific node with the given value from the linked list.
    - `show_list(self)`: Generates a string representation of the linked list, displaying its elements.

These classes and functions enable you to create, modify, and interact with doubly linked lists efficiently. You can use them to manage a sequence of elements with both forward and backward traversal capabilities. The provided methods offer flexibility for adding, removing, and displaying elements within the linked list.


