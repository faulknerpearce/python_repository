# SkyRoute

## Overview
SkyRoute is a Python script that helps users find the shortest metro route between landmarks in Vancouver. The script utilizes graph traversal algorithms, specifically Breadth-First Search (BFS) and Depth-First Search (DFS), to find optimal routes through the Vancouver metro system. The application provides a user-friendly interface, allowing users to input their starting and ending landmarks and receive the shortest route information.

## Features
- **Delayed Printing:** The script features a delayed print function that creates a visually appealing text display, character by character.
- **Interactive User Input:** Users can input their choices interactively with delayed input, enhancing the overall user experience.
- **Route Finding:** SkyRoute employs BFS and DFS algorithms to find the shortest route between two landmarks, considering metro station connections.
- **Landmark Information:** Users can view a list of landmarks along with corresponding letters.

## Functions

### `delayed_print(text, delay=0.04)`
- Prints text with a delay between characters to create a typewriter effect.

### `delayed_input(text)`
- Accepts user input with a typewriter effect for the prompt.

### `bfs(graph, start_vertex, target_value)`
- Performs Breadth-First Search to find the shortest route between two vertices in a graph.

### `dfs(graph, current_vertex, target_value, visited=None)`
- Performs Depth-First Search to find a path between two vertices in a graph.

### `create_landmark_string(landmarks_dict)`
- Creates a formatted string listing landmarks and their corresponding letters.

### `greet(landmarks_str)`
- Displays a welcome message for the SkyRoute application.

### `goodbye()`
- Displays a goodbye message for the SkyRoute application.

### `show_landmarks(landmarks_str)`
- Displays the list of landmarks based on user input.

### `get_start()`
- Retrieves the user's input for the starting point of the route.

### `get_end()`
Retrieves the user's input for the ending point of the route.

### `get_active_stations(vc_metro_dict, the_stations_under_construction)`
- Returns an updated metro dictionary with stations under construction removed from neighboring stations.

### `set_start_and_end(start_point, end_point, landmarks_str)`
- Sets the starting and ending points for the route, allowing the user to change them if needed.

### `get_route(start_point, end_point, vc_landmarks_dict, vc_metro_dict, construction)`
- Finds the shortest route between two landmarks using Breadth-First Search.

### `new_route(landmarks_str, vc_landmarks_dict, vc_metro_dict, construction, start_point=None, end_point=None)`
- Displays the shortest route and asks the user if they want to see another route.

### `skyroute(landmarks_str, vc_landmarks_dict, vc_metro_dict, construction)`
- Initiates the SkyRoute application.

---

**Note:** Ensure you have the required Python environment and dependencies installed before running the script.
