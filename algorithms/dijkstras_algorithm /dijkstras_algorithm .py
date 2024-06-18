from heapq import heappop, heappush
from math import inf

# Implements Dijkstra's algorithm to find the shortest paths from the start vertex to all other vertices in the graph.
def dijkstras(graph, start):
    distances = {}
    
    # Initialize distances to infinity for all vertices except the start vertex.
    for vertex in graph:
        distances[vertex] = inf
    
    distances[start] = 0  # Distance to the start vertex is 0
    vertices_to_explore = [(0, start)]  # Priority queue to explore vertices

    # Explore the graph until all vertices are processed
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)  # Get the vertex with the shortest distance

        # Check each neighbor of the current vertex
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight  # Calculate new distance
            
            # Update the distance if a shorter path is found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))  # Push the neighbor with updated distance

    return distances

# Main Program
if __name__ == "__main__":
    # Define the graph with vertices and weighted edges
    graph = {
        'A': [('B', 10), ('C', 3)],
        'B': [('C', 3), ('D', 2)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': []
    }
    
    # Run Dijkstra's algorithm from vertex 'A'
    distances_from_a = dijkstras(graph, 'A')
    
    # Print the shortest distances from vertex 'A' to all other vertices
    print(f"Shortest Distances: {distances_from_a}")
