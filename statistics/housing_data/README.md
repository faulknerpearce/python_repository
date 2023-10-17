# Housing Data Analysis

## Overview
The Housing Data Analysis project is a Python script that provides various statistical calculations for housing data. It includes functions to calculate the mean, median, and mode of a list of numbers, as well as reading and processing data from a CSV file.

## Features
- Calculate the average (mean) price of homes.
- Calculate the median price of homes.
- Calculate the mode(s) of prices.
- Read and convert data from a CSV file to a dictionary.

## Functions and Classes

### `calculate_mean(prices)`
This function calculates the average (mean) price of homes based on a list of prices.

### `calculate_median(nums)`
This function calculates the median price of homes based on a list of numbers. It uses the median calculation algorithm to handle even and odd-sized lists.

### `count_frequencies(nums)`
This function counts the frequencies of numbers in a list and adds each number and its frequency to a dictionary. It's primarily used to calculate the mode.

### `calculate_mode(numbers)`
This function calculates the mode(s) of a list of numbers. It uses the `count_frequencies` function to count the frequencies and returns a list of modes, including their frequencies.

### `csv_to_dictionary(csv_file)`
This function reads data from a CSV file and converts it into a dictionary, where keys are column headers, and values are lists of data corresponding to each column.

## Usage
1. Read in housing data from a CSV file using `csv_to_dictionary`.
2. Calculate the mean, median, and mode using the provided functions.
3. Display the results using `print`.

