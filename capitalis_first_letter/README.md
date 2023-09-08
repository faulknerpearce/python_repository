# Capitalize First Letter Script

## Overview

The Capitalize First Letter Script is a simple Python program designed to capitalize the first letter of a given string. It performs this operation by checking if the first character in the string is a lowercase letter, converting it to uppercase, and then adding the rest of the string back on.

## Features

- The script capitalizes the first letter of a provided string.
- It checks if the string is not empty before performing the operation.
- The script uses ASCII character codes to determine the case of the first letter and convert it to uppercase.
- The script handles the capitalization process case-insensitively.

## Function Descriptions

`capitalize_first_letter(my_string)`

- Accepts an input string (`my_string`) as an argument.
- Checks if the string is not empty.
- Retrieves the ASCII code of the first character in the string.
- Checks if the first character is a lowercase letter (ASCII code between 97 and 127).
- If it's a lowercase letter, subtracts 32 from its ASCII code to make it uppercase.
- Converts the modified ASCII code back to a character.
- Adds the rest of the original string back on.
- Returns the capitalized string.

## Usage

1. Run the script, and it will capitalize the first letter of a predefined string: `"hello, world"`.
2. The script will display the capitalized string: `"Hello, world"`.
3. You can also use the `capitalize_first_letter()` function to capitalize the first letter of any string programmatically.

