# Ultra Super Calculator (USCC)

This project provides a Python implementation of the Ultra Super Calculator (USCC), a programmable calculator that operates on binary instructions and simulates register-based arithmetic operations.

## Features

- Register-based storage for numbers and calculation history.
- Supports addition, subtraction, multiplication, and division using binary instructions.
- Binary instruction parser for executing operations and storing results.
- Methods for storing, loading, and retrieving values from registers.
- User display for operation feedback and error messages.

## Classes and Methods

### `UltraSuperCalculator`
Implements the calculator logic and binary instruction parsing.

- `__init__(self, name=None)`: Initializes the calculator, registers, and display.
- `update_display(self, to_update)`: Updates and prints the user display message.
- `store_value_to_register(self, value_to_store)`: Stores a binary value to the next available register.
- `load_value_from_register(self, register_address)`: Loads a value from a specified register address.
- `store_to_history_register(self, result_to_store)`: Stores a result to the history register.
- `add(self, address_num1, address_num2)`: Adds values from two registers.
- `multiply(self, address_num1, address_num2)`: Multiplies values from two registers.
- `subtract(self, address_num1, address_num2)`: Subtracts one register value from another.
- `divide(self, address_num1, address_num2)`: Divides one register value by another, handling division by zero.
- `get_last_calculation(self)`: Displays the last calculation result from history.
- `binary_reader(self, instruction)`: Parses and executes a 32-bit binary instruction.

## Example Usage

```python
my_calculator = UltraSuperCalculator()
my_calculator.binary_reader("00000100000000000000000101000000")
```

Explore the code for more details and usage instructions. Each method is documented for clarity and educational purposes.
