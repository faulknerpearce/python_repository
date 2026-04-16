from math import inf
from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, penn_station, grand_central_station

# Calculates the Manhattan distance (heuristic) between two points.
def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance

# Implements the A* algorithm to find the shortest path between start and target nodes in a graph.
def a_star(graph, start, target):
    count = 0  # Initialize step counter
    paths_and_distances = {}  # Dictionary to store the shortest distance and path to each vertex

    # Initialize all distances to infinity and paths to start from the starting vertex.
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]
    
    paths_and_distances[start][0] = 0  # Distance to the start vertex is 0
    vertices_to_explore = [(0, start)]  # Priority queue to explore vertices

    # Explore the graph until all vertices are explored or the target is reached
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)  # Get the vertex with the lowest cost
        
        # Check each neighbor of the current vertex
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)  # Calculate new distance
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]  # Update the path
            
            # Update the distance and path if a shorter path is found
            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1
                print("\nAt " + vertices_to_explore[0][1].name)  # Print current vertex being explored
                
    print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
    return paths_and_distances[target][1]

if __name__ == '__main__':
    # Execute the A* algorithm on the Manhattan graph from Penn Station to Grand Central Station.
    a_star(manhattan_graph, penn_station, grand_central_station)
