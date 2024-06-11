# Dijkstra's Algorithm

## Overview

This project implements Dijkstra's algorithm in Python to find the shortest path from a starting vertex to all other vertices in a weighted graph. The algorithm uses a priority queue (min-heap) to explore vertices in the order of their current known shortest distance from the starting vertex.

## Features

- **Shortest Path Calculation**: Computes the shortest path from a specified starting vertex to all other vertices in the graph.
- **Graph Representation**: Accepts a graph represented as an adjacency list.
- **Priority Queue**: Utilizes a min-heap for efficient vertex exploration based on the shortest known distance.

## Function Description

`dijkstras(graph, start)`

- Implements Dijkstra's algorithm to compute the shortest paths from the starting vertex.
- Parameters:
  - `graph`: A dictionary representing the weighted graph as an adjacency list. Each key is a vertex, and each value is a list of tuples representing adjacent vertices and edge weights.
  - `start`: The starting vertex for the algorithm.
- Returns:
  - A dictionary containing the shortest distance from the starting vertex to each other vertex in the graph.

## Usage

1. Define the graph as a dictionary where each key is a vertex, and the corresponding value is a list of tuples representing neighboring vertices and edge weights.
2. Call the `dijkstras` function with the graph and the starting vertex as arguments.
3. The function returns a dictionary with the shortest distances from the starting vertex to each vertex in the graph.
