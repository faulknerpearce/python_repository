# HashMap Implementation

A Python implementation of a hash map data structure that demonstrates fundamental concepts of hash tables including hashing, compression, and collision resolution.

## Project Overview

This project provides a custom HashMap class that efficiently maps keys to values using hashing techniques. The implementation includes:

- A hash function that converts string keys into numeric hash codes
- A compression function to map hash codes to valid array indices
- Collision resolution using open addressing with linear probing

## Features

- **Custom Hashing**: Converts string keys to numeric values by summing ASCII values
- **Hash Code Compression**: Ensures hash codes fit within the array bounds
- **Collision Handling**: Implements linear probing to resolve hash collisions
- **Key-Value Storage**: Supports assignment and retrieval operations

## Implementation Details

### Hashing Function
The hashing function converts a string key into a numeric value by:
1. Encoding the string to bytes
2. Summing the ASCII values of each byte
3. Adding an optional collision count for conflict resolution

### Compression Function
The compression function ensures that hash codes map to valid indices within the array using the modulo operation:
```python
hash_code % array_size
```

### Collision Resolution
When two different keys hash to the same array index (collision), the implementation:
1. Increments a collision counter
2. Rehashes the key with the collision count
3. Compresses the new hash code to find an alternative array position
4. Continues this process until an empty slot or the same key is found

## Performance Characteristics

- **Time Complexity**: 
  - Average case: O(1) for both assign and retrieve operations
  - Worst case: O(n) when many collisions occur
- **Space Complexity**: O(n) where n is the array size

## Limitations and Future Improvements

- No dynamic resizing when the load factor increases
- No deletion functionality
- Linear probing may lead to clustering
- Could be improved with alternative collision resolution strategies