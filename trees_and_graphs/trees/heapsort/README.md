# Heapsort

## Overview

This implementation provides the heapsort sorting algorithm using a binary heap data structure. Heapsort is an efficient comparison-based sorting algorithm with O(n log n) time complexity that works by building a max heap and repeatedly extracting the maximum element.

## Features

- MaxHeap class implementation with full heap operations
- Heapsort algorithm using the max heap
- Heapify-up for insertion
- Heapify-down for extraction
- Step-by-step visualization of the sorting process

## Functions

`MaxHeap.__init__()`
- Initializes an empty max heap
- Returns: None

`MaxHeap.add(element)`
- Adds an element to the heap and maintains heap property
- Parameters: element (int)
- Returns: None

`MaxHeap.retrieve_max()`
- Removes and returns the maximum element from the heap
- Returns: Maximum element or None if heap is empty

`MaxHeap.heapify_up()`
- Restores heap property by moving element up as needed
- Returns: None

`MaxHeap.heapify_down()`
- Restores heap property by moving element down as needed
- Returns: None

`heapsort(lst)`
- Sorts a list using the heapsort algorithm
- Parameters: lst (list)
- Returns: Sorted list

## Usage

Import heapsort and call it with a list to sort. The function returns a sorted list in ascending order.