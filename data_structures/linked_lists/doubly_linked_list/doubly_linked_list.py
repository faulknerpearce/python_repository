# Node class represents a node in a doubly linked list.
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        # Initialize a node with a value, next_node reference, and prev_node reference.
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    # Set the reference to the next node.
    def set_next_node(self, next_node):
        self.next_node = next_node

    # Get the reference to the next node.
    def get_next_node(self):
        return self.next_node

    # Set the reference to the previous node.
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    # Get the reference to the previous node.
    def get_prev_node(self):
        return self.prev_node

    # Get the value of the current node.
    def get_value(self):
        return self.value

# DoublyLinkedList class represents a doubly linked list with head and tail nodes.
class DoublyLinkedList:
    def __init__(self, head_node=None, tail_node=None):
        self.head_node = head_node
        self.tail_node = tail_node

    # Add a new node to the head of the linked list.
    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    # Add a new node to the tail of the linked list.
    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    # Remove the head of the list. 
    def remove_head(self):
        removed_head = self.head_node

        if removed_head == None:
            return None
        
        self.head_node = removed_head.get_next_node()

        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()
    
    # Remove the tail of the list.
    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail == None:
            return None
        
        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()
    
    # Removes a specific node with a given value from the doubly linked list.
    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        if node_to_remove == None:
            return None

        elif node_to_remove == self.head_node:
            self.remove_head()

        elif node_to_remove == self.tail_node: 
            self.remove_tail()

        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove
    
    def show_list(self):
        elements = '\n'
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None: 
                elements += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return elements 







