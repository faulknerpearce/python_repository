# Thread Shed Sales Analysis
This program analyzes sales data for a fictional Thread Shed fabric store. It takes raw sales data as text input, processes it, and generates a report showing total sales and breakdowns by thread color.

## Overview

### The script executes the following steps:
- Imports raw sales data from a text file as a long string
- Performs multiple string replacement operations to clean the data:
- Replaces delimiter characters for easier splitting
- Removes whitespace
- Splits the string into a list of sales transactions
### Further cleans the list by:
- Removing commas between values
- Removing newline characters
- Splits transactions into separate lists for customers, sale amounts, and threads sold
- Iterates through sales amounts to calculate total sales
- Flattens the thread sold list into individual colors using string splitting
- Counts the occurrences of each thread color
### Prints a report showing:
The calculated total sales and a breakdown of the number sold of each thread color. 

## Functions

### get_string()
- Opens the text file "text.txt" and returns the contents as a string

### fix_list()
- Accepts a list and strings to find/replace as arguments
- Iterates through each element of the list
- Replaces all instances of the find string with the replace string
- Returns the modified list

### populate_lists()
- Accepts the transactions list and 3 empty lists as arguments
- Iterates through transactions list, indexing to populate the 3 lists
- Returns the 3 populated lists (customers, sales, thread sold)

### get_total()
- Accepts the list of sales amounts as argument
- Iterates through each element, converting to float
- Calculates and returns the total

### split_thread()
- Accepts thread sold list as argument
- Iterates through, splitting any strings containing "&" on that delimiter
- Returns a flattened list with each color as a separate element

### colour_count()
- Accepts thread color list and a thread color string as arguments
- Iterates through thread color list, counting occurrences of given color
- Returns the count