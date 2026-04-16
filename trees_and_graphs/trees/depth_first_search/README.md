# Depth-First Search (DFS)

## Overview

This implementation provides depth-first search for tree traversal, exploring branches as deep as possible before backtracking. DFS uses recursion (or a stack) to explore as far as possible along each branch before returning, making it useful for detecting cycles, topological sorting, and path finding in trees.

## Features

- TreeNode class for creating tree structures
- DFS implementation using recursion
- Path tracking to reconstruct the path from root to target
- Tree visualization with hierarchical formatting
- Helper functions for printing trees and paths

## Functions

`TreeNode.__init__(value)`
- Creates a new tree node
- Parameters: value (any)
- Returns: None

`TreeNode.add_child(child_node)`
- Adds a child node to this node
- Parameters: child_node (TreeNode)
- Returns: None

`TreeNode.remove_child(child_node)`
- Removes a child node from this node
- Parameters: child_node (TreeNode)
- Returns: None

`TreeNode.traverse()`
- Traverses the tree using depth-first search (pre-order)
- Returns: None (prints each node)

`dfs(root, target, path=())`
- Traverses the tree using depth-first search to find the target value
- Parameters: root (TreeNode), target (any), path (tuple, optional)
- Returns: Tuple representing path from root to target, or None

`print_tree(root)`
- Prints a visual representation of the tree
- Parameters: root (TreeNode)
- Returns: None

`print_path(path)`
- Prints the path found by DFS
- Parameters: path (tuple)
- Returns: None

## Usage

Create TreeNode objects and build the tree structure using add_child(). Call dfs() with the root node and target value to find the path. Use print_tree() to visualize the tree structure.