# Sorted Bookshelf

Sorted Bookshelf is a utility for loading and managing a collection of books from a CSV file. It processes book data, making it easier to search and sort by author or title in a case-insensitive manner.

## Features

- Loads book data from a CSV file
- Converts author and title fields to lowercase for easier searching and sorting
- Returns a list of book dictionaries for further processing
- Provides sorting algorithms (Bubble Sort and Quicksort) for custom book sorting
- Includes flexible comparison functions for sorting by different criteria

## Functions

### utils.py

#### load_books(filename)
Loads book data from the specified CSV file and returns a list of dictionaries, each representing a book with the following keys:
- `author`: The author's name
- `title`: The book's title
- `author_lower`: Lowercase version of the author's name
- `title_lower`: Lowercase version of the book's title

**Parameters:**
- `filename` (str): Path to the CSV file containing book data. The file should have columns named `author` and `title`.

**Returns:**
- `bookshelf` (list of dict): List of book dictionaries with lowercase fields for easier searching and sorting.

### sorts.py

#### bubble_sort(arr, comparison_function, sorting_item)
Sorts a list in place using the Bubble Sort algorithm and a custom comparison function.

**Parameters:**
- `arr` (list): List to be sorted.
- `comparison_function` (function): Function that compares two elements and returns True if they should be swapped.
- `sorting_item` (str): Key in the dictionary to use for comparison.

**Returns:**
- The sorted list.

#### quicksort(list, start, end, comparison_function, sorting_item)
Sorts a list in place using the Quicksort algorithm and a custom comparison function.

**Parameters:**
- `list` (list): List to be sorted.
- `start` (int): Starting index for the sort.
- `end` (int): Ending index for the sort.
- `comparison_function` (function): Function that compares two elements and returns True if they should be swapped.
- `sorting_item` (str): Key in the dictionary to use for comparison.

**Returns:**
- None (the list is sorted in place).

### main.py

#### sort_by_ascending(book_a, book_b, item)
Compares two books based on the first character of a specified item (e.g., 'title_lower' or 'author_lower').

**Parameters:**
- `book_a`, `book_b` (dict): Book dictionaries to compare.
- `item` (str): Key to compare (e.g., 'title_lower').

**Returns:**
- True if `book_a` should come after `book_b` alphabetically, otherwise False.

#### sort_by_length(book_a, book_b, items)
Compares two books by the combined length of two specified fields.

**Parameters:**
- `book_a`, `book_b` (dict): Book dictionaries to compare.
- `items` (list of str): List of two keys to sum the lengths of (e.g., ['author_lower', 'title_lower']).

**Returns:**
- True if the combined length for `book_a` is greater than for `book_b`, otherwise False.

#### print_books(books, key)
Prints the value of a specified key for each book in the list.

**Parameters:**
- `books` (list): List of book dictionaries.
- `key` (str): Key to print (e.g., 'title_lower').

**Returns:**
- None (prints output to the console).

## Usage

Import the `load_books` function and call it with the path to your CSV file to retrieve the bookshelf data for further processing or display. Use the provided sorting functions and comparison functions to sort and display your books as needed.
