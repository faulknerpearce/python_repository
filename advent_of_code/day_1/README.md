# Day 1: Santa's Journey

## Overview
This script determines Santa's final floor and the position that first brings Santa to the basement (-1 floor) in a building, based on a series of instructions. The instructions are read from a text file ("text.txt"), where each character represents an instruction: "(" means go up one floor, and ")" means go down one floor.

## Functions
The script has the following main functions:

1. `convert_to_string()`: This function reads the instructions from a text file, converting the content into a string.

2. `convert(my_string)`: This function takes the string of instructions and breaks it into a list of characters (instructions). It ignores any spaces in the input string.

3. `floor_count(my_chars)`: This function takes the list of instructions and processes them to determine Santa's final floor and the position that first brings him to the basement. It uses a while loop to iterate through the list of instructions, incrementing a 'floor' counter for "(" instructions and decrementing it for ")" instructions. It also keeps track of the 'position' within the instructions. The first time Santa reaches the basement (floor -1), it records that position.

## Sample Output

Santans Floor: 232
Basement position: 1783