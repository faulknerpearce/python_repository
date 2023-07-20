# Santa's Journey

This is a Python script that simulates Santa's journey through a building. It reads directions from a file, converting them into instructions for Santa, and determines which floor Santa ends up on and the position at which Santa first reaches the basement.

## Functions

The script includes three key functions:

1. `convert_to_string()`: This function reads the `text.txt` file and converts it into a string.

2. `convert(my_string)`: This function takes a string as input and returns a list of characters, excluding spaces.

3. `floor_count(my_chars)`: This function takes a list of characters as input, where each character is an instruction for Santa (`(` for going up a floor, `)` for going down a floor). It returns two values: the final floor number and the position at which Santa first reaches the basement.

The `main` part of the script orchestrates these functions and prints the results.

## Sample Output

Santans Floor: 232
Basement position: 1783