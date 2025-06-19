# List and String Reversal Script

## Overview

The List and String Reversal Script is a Python program designed to reverse lists and strings. The script includes two main functions: one to reverse a list in place and another to reverse a string by converting it to a list, reversing the list, and then joining it back into a string.

## Features

- Reverses a list in place without using additional space for another list.
- Converts a string to a list, reverses the list, and then joins it back into a string.
- Uses in-place reversal for lists and minimal additional space for strings.

## Function Descriptions

### `reverse_list(lst)`

- Reverses a list in place.
- Parameters:
  - `lst`: The list to be reversed.
- Returns:
  - The reversed list.

### `reverse_string(string_item)`

- Reverses a string by converting it to a list, reversing the list, and then joining it back into a string.
- Parameters:
  - `string_item`: The string to be reversed.
- Returns:
  - The reversed string.

## Usage

1. **Reverse List**:
   - Define the list `my_list` with the elements you want to reverse.
   - Call the `reverse_list` function with `my_list` as the argument.
   - The function will return the reversed list.

2. **Reverse String**:
   - Define the string `my_string` with the text you want to reverse.
   - Call the `reverse_string` function with `my_string` as the argument.
   - The function will return the reversed string.
