# Tree Node

## Overview

This implementation provides a basic TreeNode class for creating tree data structures. Tree nodes are the fundamental building blocks of tree data structures, containing a value and references to child nodes, enabling hierarchical data representation.

## Features

- TreeNode class with value and children list
- Add child functionality for building tree structures
- Remove child functionality for tree modification
- Depth-first traversal method for visiting all nodes
- Hierarchical tree structure representation

## Functions

`TreeNode.__init__(value)`
- Initializes a new tree node with a given value and empty children list
- Parameters: value (any)
- Returns: None

`TreeNode.add_child(child_node)`
- Adds a child node to the current node
- Parameters: child_node (TreeNode)
- Returns: None

`TreeNode.remove_child(child_node)`
- Removes a child node from the current node
- Parameters: child_node (TreeNode)
- Returns: None

`TreeNode.traverse()`
- Traverses the tree in depth-first manner, printing each node's value
- Returns: None

## Usage

Create TreeNode instances and use add_child() to build the tree structure. Call traverse() to print all nodes in depth-first order.