# Day 2: Calculate warpping paper and ribbon 

## Challenge Overview
The challenge involves calculating the exact amount of wrapping paper and ribbon needed for a list of presents. Each present is a box (a perfect right rectangular prism) with given dimensions (length l, width w, and height h).

## Part One
The amount of wrapping paper for each box is determined by the surface area (2lw + 2wh + 2hl) plus the area of the smallest side. The aim is to determine the total square feet of wrapping paper needed for all presents.

## Part Two
The amount of ribbon required to wrap a present is determined by the shortest distance around its sides (the smallest perimeter of any one face), plus a bow made out of ribbon. The feet of ribbon required for the bow equals the cubic feet of volume of the present.

## Functionality 
The script is divided into four functions:

1. ### get_slack_and_ribbon(l, w, h): 
This function takes the dimensions of a box as input and calculates the slack needed for the wrapping paper and the total length of ribbon needed. The slack is calculated as the area of the two smallest sides of the box. The ribbon length is calculated as the perimeter of the smallest face of the box plus the volume of the box (for the bow).

2. ### format_string(): 
This function opens a text file named "text.txt", reads its contents, and returns the content as a string. The text file is expected to contain the dimensions of the boxes, with each dimension separated by 'x' and each box on a new line.

3. ### format_ints(): 
This function calls format_string() to get the string of box dimensions, then parses this string to extract the individual dimensions as integers. It does this by building up each number digit by digit, then converting the string representation of the number to an integer when it encounters an 'x' or a newline. The resulting list of integers is returned.

4. ### box_dimensions(numbers): 
This function takes the list of integers returned by format_ints(), treats every three integers as the dimensions of a box, and calculates the total wrapping paper and ribbon needed for all boxes. It does this by calling get_slack_and_ribbon() for each box to get the slack and ribbon needed, then adds these to running totals. The total wrapping paper and ribbon needed are returned.

The script then calls these functions and prints the total wrapping paper and ribbon needed.



