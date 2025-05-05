# Blossom Dictionary

A simple yet elegant implementation of a hash map data structure for storing and retrieving flower names and their symbolic meanings.

## Project Overview

This project demonstrates a custom hash map implementation in Python, designed to efficiently store and retrieve key-value pairs. The implementation includes:

- A hash function that converts keys to numeric hash codes
- A compression function to fit hash codes within the array size
- Collision handling using chaining with linked lists

## Files in this Project

- `hashmap.py` - Contains the HashMap class implementation
- `linkedlist.py` - Contains the LinkedList and Node classes for the chaining mechanism
- `flower_library.py` - Demo application that uses the HashMap to create a flower dictionary

## How the Hash Map Works

1. **Hashing**: The `hash()` method converts a string key into a numeric value by summing the ASCII values of each character.

2. **Compression**: The `compress()` method ensures the hash code fits within the array size using modulo operation.

3. **Collision Handling**: When two keys hash to the same array index, a linked list stores multiple key-value pairs at that index.

## Implementation Details

- The HashMap uses a fixed-size array of linked lists to store elements
- Time complexity for assign and retrieve operations is O(1) on average, but can degrade to O(n) in worst case
- Space complexity is O(n) where n is the number of key-value pairs stored

## Potential Improvements

- Implement dynamic resizing to maintain load factor
- Add more sophisticated hash functions to reduce collisions
- Implement deletion functionality