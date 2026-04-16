# A* Algorithm

## Overview

This implementation demonstrates the A* pathfinding algorithm for finding the shortest path between two points using heuristic estimates. The algorithm combines the actual cost from the start node with a heuristic estimate to the goal to efficiently find the optimal path.

## Features

- Manhattan distance heuristic implementation for grid-based navigation
- Priority queue-based vertex exploration for optimal path finding
- Path reconstruction showing the sequence of nodes visited
- Step-by-step visualization of the algorithm's execution
- Integration with a Manhattan graph example (NYC stations)

## Functions

`heuristic(start, target)`
- Calculates the Manhattan distance between two points
- Parameters: start (Vertex), target (Vertex)
- Returns: Integer representing the heuristic distance

`a_star(graph, start, target)`
- Implements the A* algorithm to find the shortest path
- Parameters: graph (dict), start (Vertex), target (Vertex)
- Returns: List of node names representing the path from start to target

## Usage

Run `python main.py` to execute the A* algorithm on the Manhattan graph, finding the path from Penn Station to Grand Central Station.