# Dijkstra's Algorithm Script

This script implements Dijkstra's algorithm to find the shortest distances from a starting node to all other nodes in a weighted graph. It uses a priority queue (min-heap) for efficient exploration of nodes.

## Features

- Calculates shortest path distances from a given start node to all other nodes in a directed, weighted graph
- Uses Python's `heapq` for efficient priority queue operations
- Simple dictionary-based graph representation
- Example usage included in the `__main__` block

## Function

### dijkstras(graph, start)
"""Dijkstra's algorithm: returns shortest distances from start to all nodes in a weighted graph."""
- **Parameters:**
  - `graph` (dict): A dictionary where each key is a node and the value is a list of `(neighbor, edge_weight)` tuples.
  - `start` (any): The starting node for the algorithm.
- **Returns:**
  - `distances` (dict): A dictionary mapping each node to its shortest distance from the start node.

## Example

```
graph = {
  'A': [('B', 10), ('C', 3)],
  'B': [('C', 3), ('D', 2)],
  'C': [('D', 2)],
  'D': [('E', 10)],
  'E': []
}

distances_from_a = dijkstras(graph, 'A')
print(distances_from_a)
```

## Usage

Run the script directly to see the example in action:

```
python dijkstras_algorithm.py
```

The output will display the shortest distances from node 'A' to all other nodes in the graph.
