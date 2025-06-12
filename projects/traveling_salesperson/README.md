# Traveling Salesperson Project

This project provides a simple Python implementation of the Traveling Salesperson Problem (TSP) using a graph data structure. It demonstrates how to represent graphs with vertices and edges, and includes a basic greedy algorithm to find a path visiting all nodes.

## Features

- Custom `Graph` and `Vertex` classes for flexible graph construction
- Weighted, undirected graph support
- Greedy TSP path-finding algorithm
- Utility functions for graph building and visualization

## Files

- `main.py`: Runs the TSP algorithm and prints the resulting path
- `graph.py`: Contains the `Graph` class for managing vertices and edges
- `vertex.py`: Contains the `Vertex` class for representing graph nodes

## Functions

### main.py

#### print_graph(graph)
Prints each vertex and its connected neighbors in the graph.

**Parameters:**
- `graph` (`Graph`): The graph to print.

**Returns:**
- None (prints output to the console).

#### build_tsp_graph(directed)
Builds and returns a sample graph for the TSP.

**Parameters:**
- `directed` (bool): Whether the graph is directed.

**Returns:**
- `g` (`Graph`): The constructed graph object.

#### visited_all_nodes(visited_vertices)
Checks if all nodes in the graph have been visited.

**Parameters:**
- `visited_vertices` (dict): Dictionary mapping vertex names to 'visited' or 'unvisited'.

**Returns:**
- True if all nodes are visited, otherwise False.

#### traveling_salesperson(graph)
Finds a path visiting all nodes using a greedy approach and prints the path.

**Parameters:**
- `graph` (`Graph`): The graph to solve TSP on.

**Returns:**
- None (prints the path to the console).

### graph.py

#### Graph class
Represents a graph with methods to add vertices, add edges, and find paths.

- `add_vertex(vertex)`: Adds a vertex to the graph.
- `add_edge(from_vertex, to_vertex, weight=0)`: Adds an edge between two vertices with an optional weight.
- `find_path(start_vertex, end_vertex)`: Checks if a path exists between two vertices.

### vertex.py

#### Vertex class
Represents a graph node with methods to manage edges.

- `add_edge(vertex, weight=0)`: Adds an edge to another vertex with an optional weight.
- `get_edges()`: Returns a list of connected vertices.
- `edge_weight(edge)`: Returns the weight of the edge to a given vertex.

## Usage

1. Run `main.py` to build a sample graph and solve the TSP using the provided algorithm:
   ```
   python main.py
   ```
2. The script will print the path found by the greedy TSP algorithm.

## Example Output

```
a b c d
```

## Notes

- The provided TSP solution is a greedy heuristic and does not guarantee the optimal path.
- You can modify the graph in `build_tsp_graph()` to experiment with different node and edge configurations.

## License

This project is open source and available under the MIT License.
