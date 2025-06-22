# Thread Shed Sales Analyzer

## Overview

Thread Shed Sales Analyzer is a Python script that processes and analyzes sales data for a fictional thread store. It reads raw sales data, cleans and structures it, calculates total sales, and counts the number of threads sold by color.

## Features

- Reads and parses raw sales data from a text file.
- Cleans and structures the data for analysis.
- Calculates the total sales amount.
- Splits multi-color thread sales into individual colors.
- Counts and reports the number of threads sold for each color.
- Outputs a formatted sales summary to the console.

## Function Descriptions

### `get_string()`
- Reads the contents of the sales data file (`text.txt`).
- Returns:
  - The raw sales data as a string.

### `fix_list(my_list, a, b)`
- Replaces all occurrences of a substring with another in each item of a list.
- Parameters:
  - `my_list`: The list to process.
  - `a`: The substring to replace.
  - `b`: The replacement substring.
- Returns:
  - A new list with the replacements applied.

### `populate_lists(string_list, list_1, list_2, list_3)`
- Populates three lists with customer names, sales amounts, and thread colors from the cleaned data list.
- Parameters:
  - `string_list`: The cleaned data list.
  - `list_1`, `list_2`, `list_3`: Empty lists to be filled.
- Returns:
  - The three populated lists: customers, sales, and thread_sold.

### `get_total(store_sales)`
- Calculates the total sales amount from a list of sales values.
- Parameters:
  - `store_sales`: The list of sales as strings (without the dollar sign).
- Returns:
  - The total sales as a float, rounded to two decimal places.

### `split_thread(store_threads)`
- Splits thread color strings containing multiple colors (separated by `&`) into individual colors.
- Parameters:
  - `store_threads`: The list of thread color strings.
- Returns:
  - A flattened list of all individual thread colors sold.

### `colour_count(my_list, colour)`
- Counts the number of times a specific color appears in a list.
- Parameters:
  - `my_list`: The list to search.
  - `colour`: The color to count.
- Returns:
  - The count of the specified color.

## Usage

1. **Analyze Thread Shed Sales**:
   - Ensure the `text.txt` file with sales data is present in the same directory as the script.
   - Run the `thread_shed.py` script to process the data.
   - The script will output the number of threads sold for each color and the total sales amount to the console.
