# Sorting Algorithms

## Overview

This project implements three classic sorting algorithms in Python: Bubble Sort, Merge Sort, and Quicksort. Each algorithm sorts an array in ascending order and demonstrates different approaches to sorting. The implementations are designed to provide a clear understanding of how these algorithms work.

## Features

- **Bubble Sort**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Merge Sort**: A divide-and-conquer algorithm that splits the list into halves, recursively sorts each half, and then merges the sorted halves.
- **Quicksort**: A divide-and-conquer algorithm that selects a pivot element, partitions the array around the pivot, and recursively sorts the subarrays.

## Functions

### bubble_sort

`bubble_sort(arr)`

- Implements the Bubble Sort algorithm to sort an array in ascending order.
- Parameters:
  - `arr`: The list of elements to be sorted.
- Returns:
  - The sorted list.

### merge_sort

`merge_sort(items)`

- Implements the Merge Sort algorithm to sort an array in ascending order.
- Parameters:
  - `items`: The list of elements to be sorted.
- Returns:
  - The sorted list.

 `merge(left, right)`

- Merges two sorted arrays into a single sorted array.
- Parameters:
  - `left`: The first sorted list.
  - `right`: The second sorted list.
- Returns:
  - A merged and sorted list.

### quicksort

`quicksort(list, start, end)`

- Implements the Quicksort algorithm to sort an array in ascending order.
- Parameters:
  - `list`: The list of elements to be sorted.
  - `start`: The starting index of the subarray to be sorted.
  - `end`: The ending index of the subarray to be sorted.