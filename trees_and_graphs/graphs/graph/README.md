# Graph

## Overview

This folder contains core graph data structure implementations including the Vertex and Graph classes. It provides an adjacency list representation for graphs with support for both directed and undirected edges, along with basic graph traversal operations.

## Features

- Vertex class representing individual nodes in a graph
- Graph class with adjacency list representation
- Support for weighted edges
- Option for directed or undirected graphs
- Basic path finding functionality

## Functions

`Vertex.add_edge(vertex, weight=0)`
- Adds an edge from this vertex to another with an optional weight
- Parameters: vertex (str), weight (int, default 0)
- Returns: None

`Vertex.get_edges()`
- Returns all edges connected to this vertex
- Returns: List of vertex keys

`Graph.add_vertex(vertex)`
- Adds a vertex to the graph
- Parameters: vertex (Vertex)
- Returns: None

`Graph.add_edge(from_vertex, to_vertex, weight=0)`
- Adds an edge between two vertices
- Parameters: from_vertex (Vertex), to_vertex (Vertex), weight (int, default 0)
- Returns: None

`Graph.find_path(start_vertex, end_vertex)`
- Finds if a path exists between start and end vertices
- Parameters: start_vertex (str), end_vertex (str)
- Returns: Boolean indicating if path exists

## Usage

Create Vertex and Graph objects, add vertices and edges, then use find_path to check connectivity. Run main.py for a demonstration.