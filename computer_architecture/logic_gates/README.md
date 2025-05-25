# Logic Gates

This project provides Python implementations of basic logic gates, fundamental components in computer architecture. Logic gates perform simple binary operations and are the building blocks of digital circuits.

## Features

- Implementation of AND, OR, and NOT logic gates.
- Each gate is implemented as a class with a method to compute its logical operation.
- Simple, reusable, and easy-to-understand code for educational and practical purposes.

## Classes and Methods

### `AndGate`
Represents the AND logic gate.
- `__init__(self)`: Initializes the AND gate.
- `compute(self, *inputs)`: Returns True if all inputs are True, otherwise False.

### `OrGate`
Represents the OR logic gate.
- `__init__(self)`: Initializes the OR gate.
- `compute(self, *inputs)`: Returns True if at least one input is True, otherwise False.

### `NotGate`
Represents the NOT logic gate.
- `__init__(self)`: Initializes the NOT gate.
- `compute(self, input)`: Returns the inverse (not) of the input.

## Example Usage

```python
and_gate = AndGate()
print(and_gate.compute(True, True))  # Output: True

or_gate = OrGate()
print(or_gate.compute(True, False))  # Output: True

not_gate = NotGate()
print(not_gate.compute(False))       # Output: True
```

Explore each subfolder for code examples and implementations. Refer to each subfolder's README for more details and usage instructions.