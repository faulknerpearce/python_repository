# Binary Search Tree

## Overview

This implementation provides a binary search tree (BST) data structure with methods for inserting nodes, searching for values, and performing depth-first traversal. A BST organizes data hierarchically where left children are smaller than the parent and right children are larger.

## Features

- Node insertion maintaining BST property
- Search functionality to find nodes by value
- Depth-first traversal (in-order) of the tree
- Automatic depth tracking for each node
- Recursive implementations for all operations

## Functions

`BinarySearchTree.__init__(value, depth=1)`
- Initializes a new node in the BST
- Parameters: value (int), depth (int, default 1)
- Returns: None

`BinarySearchTree.insert(value)`
- Inserts a new value into the BST
- Parameters: value (int)
- Returns: None

`BinarySearchTree.get_node_by_value(value)`
- Searches for a node with the given value
- Parameters: value (int)
- Returns: Node if found, or None

`BinarySearchTree.depth_first_traversal()`
- Performs in-order traversal of the tree
- Returns: None (prints each node)

## Usage

Create a BinarySearchTree with an initial value, use insert() to add nodes, and use get_node_by_value() to search. Call depth_first_traversal() to print all nodes in sorted order.