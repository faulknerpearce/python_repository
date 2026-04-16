# Breadth-First Search (BFS)

## Overview

This implementation provides breadth-first search for tree traversal, exploring nodes level by level from the root. BFS uses a queue data structure to ensure nodes are visited in order of their depth, making it ideal for finding the shortest path in unweighted trees.

## Features

- TreeNode class for creating tree structures
- BFS implementation using a deque for efficient queue operations
- Path tracking to reconstruct the path from root to target
- Visual tree representation with hierarchical formatting

## Functions

`TreeNode.__init__(value)`
- Creates a new tree node
- Parameters: value (any)
- Returns: None

`TreeNode.__str__()` (from tree.py)
- Returns a visual string representation of the tree
- Returns: String

`bfs(root_node, goal_value)`
- Traverses the tree using breadth-first search to find the goal value
- Parameters: root_node (TreeNode), goal_value (any)
- Returns: List representing path from root to target, or None

## Usage

Create TreeNode objects with children, then call bfs() with the root node and goal value to find the shortest path to the target.