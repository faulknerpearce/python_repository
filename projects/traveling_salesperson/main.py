import random
from graph import Graph
from vertex import Vertex

# Print the graph with vertices and their connections.
def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

# Build a sample graph for the Traveling Salesperson Problem.
def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Check if all nodes have been visited in the graph.
def visited_all_nodes(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
  return True

# Find a solution to the Traveling Salesperson Problem and print the path.
def traveling_salesperson(graph):
    ts_path = ""
    visited_vertices = {x: "unvisited" for x in graph.graph_dict}

    current_vertex = random.choice(list(graph.graph_dict))
    visited_vertices[current_vertex] = "visited"
    ts_path += current_vertex

    while not visited_all_nodes(visited_vertices):
        current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
        current_vertex_edge_weights = {}

        for edge in current_vertex_edges:
            current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].edge_weight(edge)

        if not current_vertex_edge_weights:
            break

        next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)

        if visited_vertices[next_vertex] != "visited": 
            current_vertex = next_vertex
            visited_vertices[current_vertex] = "visited"
            ts_path += current_vertex

    print(ts_path)

      
graph = build_tsp_graph(False)

traveling_salesperson(graph)

