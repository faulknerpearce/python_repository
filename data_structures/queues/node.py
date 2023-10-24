class Node:
    # Node constructor initializes a node with a value and an optional next_node reference.
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Returns the value of the current node.
    def get_value(self):
        return self.value

    # Returns the reference to the next node.
    def get_next_node(self):
        return self.next_node

    # Sets the reference to the next node.
    def set_next_node(self, next_node):
        self.next_node = next_node