# Weight-Limited Item Combination Finder

## Overview

The Weight-Limited Item Combination Finder is a Python script designed for generating combinations of items that meet a specific weight limit. It can identify the combination with the highest total value within the weight constraint. This script is particularly useful in scenarios like optimizing packing, resource allocation, and other decision-making processes that involve weight and value considerations.

## Features

- Generates all possible combinations of items under a given weight limit.
- Ensures that the total weight of the items in a combination does not exceed the specified maximum weight.
- Identifies the combination of items that offers the highest total value within the weight constraint.

## Functions

`is_unique(combination, dict)`

- Checks if a given combination of items is unique in a dictionary.
- Parameters:
  - `combination`: A tuple representing a combination of items.
  - `dict`: A dictionary where the combination is being checked for uniqueness.
- Returns `True` if unique, `False` otherwise.

`check_combination_weight(items, max_weight)`

- Validates if the total weight of items in a combination does not exceed the specified maximum weight.
- Parameters:
  - `items`: A list of tuples, each representing an item and its weight.
  - `max_weight`: The maximum allowed weight for a combination.
- Returns `True` if the total weight is within the limit, `False` otherwise.

`get_best_value(items_dict)`

- Identifies the combination with the highest value from a dictionary of item combinations.
- Parameter:
  - `items_dict`: A dictionary with keys as identifiers and values as combinations of items.
- Returns the combination with the highest total value.

`below_weight_combinations(array, max_weight)`

- Generates all possible combinations of items that are below the specified weight limit.
- Parameters:
  - `array`: A list of tuples, each representing an item and its weight.
  - `max_weight`: The maximum allowed weight for a combination.
- Returns a dictionary of valid combinations.

## Usage

1. Initialize the script with a list of items, each represented as a tuple of value and weight, and a maximum weight limit.

2. Call `below_weight_combinations()` with the item list and the weight limit to generate all valid combinations.

3. Use `get_best_value()` to find the combination with the highest total value within the weight limit.

4. The script returns the optimal combination based on the provided criteria.
