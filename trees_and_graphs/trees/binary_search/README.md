# Binary Search

## Overview

This implementation provides both iterative and recursive versions of the binary search algorithm for efficiently finding elements in sorted arrays. Binary search achieves O(log n) time complexity by repeatedly dividing the search interval in half.

## Features

- Iterative binary search implementation
- Recursive binary search implementation
- Efficient O(log n) time complexity
- Works with any sorted list of comparable elements
- Returns index of found element or error message if not found

## Functions

`binary_search(sorted_list, target)` (Iterative)
- Performs binary search using iteration
- Parameters: sorted_list (list), target (value)
- Returns: Index of target if found, or "Value not in list"

`binary_search(sorted_list, target)` (Recursive)
- Performs binary search using recursion
- Parameters: sorted_list (list), target (value)
- Returns: Index of target if found, or "value not found"

## Usage

Import the binary_search function and pass a sorted list and target value. The function returns the index of the target or an error message.