# Stack Implementation

This project provides Python implementations of stacks, along with various functions and classes for common stack operations.

## Features

- Implementation of a stack with features such as item addition (push), item removal (pop), and item inspection (peek).
- A function to check if the stack has available space.
- A function to check if the stack is empty.
- A default stack size limit of 1000 items.

## Classes

### Node Class

The `Node` class represents a node in the stack. It has the following attributes and methods:

- `value`: The value stored in the node.
- `next_node`: Reference to the next node in the stack.

#### Node Methods

- `set_next_node(next_node)`: Sets the reference to the next node.
- `get_next_node()`: Returns the reference to the next node.
- `get_value()`: Returns the value of the current node.

### Stack Class

The `Stack` class represents a stack data structure. It includes the following features and functions:

- `top_item`: Reference to the top (most recently added) item in the stack.
- `size`: Current number of items in the stack.
- `limit`: The maximum number of items the stack can hold (default is 1000).

#### Stack Methods

- `push(value)`: Adds an item to the top of the stack. If there is available space, the new item is pushed onto the stack.
- `pop()`: Removes the top item from the stack and returns its value. If the stack is empty, it displays a message.
- `peek()`: Returns the value of the top item in the stack without removing it. If the stack is empty, it displays a message.
- `has_space()`: Checks if the stack has available space based on its limit.
- `is_empty()`: Checks if the stack is empty.

## Usage

To create and use a stack, you can create an instance of the `Stack` class, and then use the `push`, `pop`, and `peek` methods to add, remove, and inspect items in the stack.

```python
# Create a stack with a default limit of 1000
my_stack = Stack()

# Add items to the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Remove and retrieve the top item
item = my_stack.pop()
print(f"Popped item: {item}")

# Inspect the top item
top_item = my_stack.peek()
print(f"Top item: {top_item}")