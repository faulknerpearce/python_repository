# Depth-First Search (DFS)

## Overview

This implementation provides the depth-first search algorithm for traversing and searching graph data structures. DFS explores as far as possible along each branch before backtracking, making it useful for detecting cycles, topological sorting, and path finding.

## Features

- Recursive implementation for clean and readable code
- Visited tracking to prevent infinite loops
- Path reconstruction upon finding the target
- Can be adapted for both graph and tree traversals

## Functions

`dfs(graph, current_vertex, target_value, visited=None)`
- Traverses the graph using depth-first search to find the target value
- Parameters: graph (dict), current_vertex (key), target_value (key), visited (list, optional)
- Returns: List representing the path from start to target, or None if not found

## Usage

Import and call the `dfs` function with your graph represented as a dictionary and the start/target vertices.