from heapq import heappop, heappush
from math import inf

def dijkstras(graph, start):
  """Dijkstra's algorithm: returns shortest distances from start to all nodes in a weighted graph."""
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))

  return distances
        
if __name__ == '__main__':

  graph = {'A': [('B', 10), ('C', 3)], 'C': [('D', 2)], 'D': [('E', 10)], 'E': [], 'B': [('C', 3), ('D', 2)]}

  distances_from_a = dijkstras(graph, 'A')

  print("\n\nShortest Distances: {0}".format(distances_from_a))
