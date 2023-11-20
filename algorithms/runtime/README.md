# Stack and Queue Script

## Overview
This Python script demonstrates the implementation and usage of a stack and a queue. It initializes a stack and a queue with a predefined size `N` and adds several countries to both data structures. The script then prints the top value of the stack and the front value of the queue. Additionally, it dequeues the first value from the queue and pops the first value from the stack, providing information about the runtime complexities.

## Features

- Implementation of a stack and a queue using Python.
- Demonstrates basic operations like push, pop, enqueue, dequeue.
- Displays the top value of the stack and the front value of the queue.
- Calculates and prints the runtime complexities for accessing the front of the queue and the bottom of the stack.

## Functions and Classes

### Stack
The `Stack` class represents a stack data structure. It has the following methods:

- `__init__(self, size)`: Initializes a stack with the given size.
- `push(self, item)`: Adds an item to the top of the stack.
- `pop(self)`: Removes and returns the item from the top of the stack.
- `peek(self)`: Returns the top item of the stack without removing it.
- `is_empty(self)`: Returns `True` if the stack is empty; otherwise, `False`.

### Queue
The `Queue` class represents a queue data structure. It has the following methods:

- `__init__(self, size)`: Initializes a queue with the given size.
- `enqueue(self, item)`: Adds an item to the rear of the queue.
- `dequeue(self)`: Removes and returns the item from the front of the queue.
- `peek(self)`: Returns the front item of the queue without removing it.
- `is_empty(self)`: Returns `True` if the queue is empty; otherwise, `False`.

### Script Usage
The script initializes instances of the `Stack` and `Queue` classes, adds values to them, and performs various operations. Checkpoints are included to demonstrate the runtime complexities of accessing elements from the stack and the queue.
Feel free to customize the content further based on your specific needs.
