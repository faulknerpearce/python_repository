# Rangoli Pattern Generator

## Overview

The Rangoli Pattern Generator is a Python script designed to generate and print Rangoli patterns. Rangoli is a traditional Indian art form that creates intricate designs. This script generates a Rangoli pattern for a given size starting from a specified letter and prints it.

## Features

- Creates the pattern for a specific row in the Rangoli starting from a given letter.
- Adds edge dashes to form a complete row in the Rangoli.
- Constructs the full list of strings representing the Rangoli pattern for a given size.
- Outputs the generated Rangoli pattern to the console.

## Function Descriptions

### `get_pattern(start, size)`

- Generates the pattern for a given row in the Rangoli starting from a specified letter.
- Parameters:
  - `start`: The starting letter index (0 for 'a', 1 for 'b', etc.).
  - `size`: The size of the Rangoli.
- Returns:
  - A list of characters representing the pattern for the specified row.

### `add_edge_to_pattern(letters_array, size)`

- Adds edge dashes to the given letters array to form a complete row in the Rangoli.
- Parameters:
  - `letters_array`: The array of letters forming the pattern.
  - `size`: The size of the Rangoli.
- Returns:
  - A string representing the complete row with edge dashes.

### `get_rangoli_list(size)`

- Generates the list of strings representing the Rangoli of a given size.
- Parameters:
  - `size`: The size of the Rangoli.
- Returns:
  - A list of strings representing the complete Rangoli pattern.

### `print_rangoli(rangoli)`

- Prints the generated Rangoli pattern.
- Parameters:
  - `rangoli`: The list of strings representing the Rangoli pattern.

## Usage

1. **Generate and Print Rangoli**:
   - Define the size of the Rangoli.
   - Call the `get_rangoli_list` function with the specified size to generate the Rangoli pattern.
   - Use the `print_rangoli` function to print the generated pattern to the console.
