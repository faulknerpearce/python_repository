# Breadth-First Search (BFS)

## Overview

This implementation provides the breadth-first search algorithm for traversing and searching graph data structures. BFS explores all neighbors at the present depth before moving on to nodes at the next depth level, making it ideal for finding the shortest path in unweighted graphs.

## Features

- Queue-based implementation ensuring level-by-level exploration
- Path tracking to reconstruct the path from start to target
- Visited set to prevent revisiting nodes
- Early termination when target is found

## Functions

`bfs(graph, start_vertex, target_value)`
- Traverses the graph using breadth-first search to find the target value
- Parameters: graph (dict), start_vertex (key), target_value (key)
- Returns: List representing the path from start to target, or None if not found

## Usage

Import and call the `bfs` function with your graph represented as a dictionary and the start/target vertices.