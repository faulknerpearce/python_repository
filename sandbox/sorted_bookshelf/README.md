# Book Sorting Project

## Overview

This Python project offers a versatile set of functionalities for sorting books based on different criteria. It consists of three main files: `main.py`, `sorts.py`, and `utils.py`. The project encompasses loading bookshelf data, implementing two sorting algorithms (Bubble Sort and Quicksort), and providing customizable comparison functions to sort books based on specific attributes.

## Features

### 1. Bubble Sort and Quicksort
- **Bubble Sort:** Efficiently sorts books using the Bubble Sort algorithm, allowing users to define custom comparison functions.
- **Quicksort:** Implements the Quicksort algorithm, providing flexibility with user-defined comparison functions for sorting.

### 2. Customizable Comparisons
- Users can define custom comparison functions to sort books based on various attributes, such as the first character of a title or the combined length of multiple attributes.

### 3. Bookshelf Data Handling
- The `utils.py` file includes a function to load bookshelf data from a CSV file. It converts author and title strings to lowercase for case-insensitive comparisons during sorting.

## Functions

#### `sort_by_ascending(book_a, book_b, item)`
- This function compares two books based on the first character of a specific item associated with the given key.

#### `sort_by_length(book_a, book_b, items)`
- Compares books based on the combined length of specific items associated with given keys.

#### `print_books(books, key)`
- Prints the values associated with the specified key for each book in the given list.

#### `bubble_sort(arr, comparison_function, sorting_item)`
- Implements the Bubble Sort algorithm to sort an array using the specified comparison function and sorting item.

#### `quicksort(list, start, end, comparison_function, sorting_item)`
- Implements the Quicksort algorithm to recursively sort a list using the specified comparison function and sorting item.

#### `load_books(filename)`
- Loads bookshelf data from a CSV file, converting author and title to lowercase for consistent and case-insensitive comparisons during sorting.