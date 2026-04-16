from collections import deque

def bfs(root_node, goal_value):
    path_queue = deque()

    # Start with the root node in our path
    initial_path = [root_node]
    # Append the initial path to the left end of the deque
    path_queue.appendleft(initial_path)
  
    while path_queue:
        # Pop the oldest element (right end of the deque) for BFS
        current_path = path_queue.pop()
        current_node = current_path[-1]

        if current_node.value == goal_value:
            return current_path

        # Extend the path to each child and append it to the left end of the deque
        for child in current_node.children:
            new_path = current_path.copy()
            new_path.append(child)
            path_queue.appendleft(new_path)
    
    return None