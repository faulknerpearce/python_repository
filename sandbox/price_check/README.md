# Price Check Utility

## Overview

The Price Check Utility is a Python script designed to help users compare and analyze prices of products. This tool can be used to input, process, and display price information, making it easier to identify the best deals or track price changes over time.

## Features

- Accepts and processes a list of product prices.
- Compares prices to find the lowest, highest, or average price.
- Outputs formatted price information for easy review.
- Can be extended to support additional price analysis features.

## Function Descriptions

### `get_price_list(input_data)`

- Processes the input data to extract a list of prices.
- Parameters:
  - `input_data`: The raw input containing product prices (e.g., a string or list).
- Returns:
  - A list of prices as floats or integers.

### `compare_prices(price_list)`

- Compares the prices in the list to find the minimum, maximum, and average price.
- Parameters:
  - `price_list`: The list of prices to compare.
- Returns:
  - A dictionary with keys `min`, `max`, and `average` representing the respective price values.

### `format_price_output(price_stats)`

- Formats the price statistics for display.
- Parameters:
  - `price_stats`: The dictionary containing price statistics.
- Returns:
  - A formatted string summarizing the price information.

### `print_price_report(formatted_output)`

- Prints the formatted price report to the console.
- Parameters:
  - `formatted_output`: The string containing the formatted price report.

## Usage

1. **Analyze Prices**:
   - Prepare the input data containing product prices.
   - Call the `get_price_list` function to process the input data.
   - Use the `compare_prices` function to analyze the prices.
   - Format the results with `format_price_output`.
   - Print the final report using `print_price_report`.
