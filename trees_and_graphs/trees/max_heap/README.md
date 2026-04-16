# Max Heap

## Overview

This implementation provides a max heap data structure where the parent node is always greater than or equal to its children. A max heap is a complete binary tree that maintains the heap property, making it efficient for priority queue operations and sorting.

## Features

- Complete binary tree representation using an array
- Parent, left child, and right child index calculations
- Heapify-up for maintaining heap property after insertion
- Heapify-down for maintaining heap property after removal
- Static heapsort method for sorting using the max heap

## Functions

`MaxHeap.__init__()`
- Initializes an empty max heap with a placeholder at index 0
- Returns: None

`MaxHeap.parent_idx(idx)`
- Calculates the parent index of a given index
- Parameters: idx (int)
- Returns: Parent index

`MaxHeap.left_child_idx(idx)`
- Calculates the left child index of a given index
- Parameters: idx (int)
- Returns: Left child index

`MaxHeap.right_child_idx(idx)`
- Calculates the right child index of a given index
- Parameters: idx (int)
- Returns: Right child index

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

`MaxHeap.heapsort(input_list)` (static)
- Sorts a list using the heapsort algorithm
- Parameters: input_list (list)
- Returns: Sorted list

## Usage

Create a MaxHeap instance and use add() to insert elements. Call retrieve_max() to extract the maximum element. Use MaxHeap.heapsort() directly to sort a list.