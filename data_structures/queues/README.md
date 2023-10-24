# Queue Implementation

This project provides Python implementations of queues, along with various functions and classes for common operations on queues.

## Features

- Implementation of queues with features such as enqueue, dequeue, peeking at the head element, and checking queue size and availability.
- A function to add elements to the end of the queue.
- A function to remove elements from the front of the queue.
- A function to view the head element without removing it.
- Functions to check the current size and available space in the queue.

## Classes and Methods

### `Node`

The `Node` class represents a node in a queue.

- `__init__(self, value, next_node=None)`: Initializes a new node with a value and an optional reference to the next node.
- `get_value()`: Returns the value of the current node.
- `get_next_node()`: Returns the reference to the next node.
- `set_next_node(next_node)`: Sets the reference to the next node.

### `Queue`

The `Queue` class represents a queue, a linear data structure with a "first in, first out" (FIFO) ordering.

- `__init__(self, max_size=None, size=0)`: Initializes a new queue with an optional maximum size.
- `enqueue(self, value)`: Adds an element to the end of the queue.
- `dequeue(self)`: Removes the element at the front of the queue and returns its value.
- `peek(self)`: Returns the value of the element at the front of the queue without removing it.
- `get_size(self)`: Returns the current size of the queue.
- `has_space(self)`: Checks if the queue has available space based on the maximum size.
- `is_empty(self)`: Checks if the queue is empty.

This queue implementation provides essential queue operations and is designed to be easily customized for various applications.


# Inspect the top item
top_item = my_stack.peek()
print(f"Top item: {top_item}")
