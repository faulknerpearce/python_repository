# HashMap Python Implementation

This project provides a Python implementation of a HashMap data structure, which allows efficient key-value pair storage and retrieval.

## Features

- Implementation of a HashMap with features like assigning and retrieving key-value pairs.
- Collision handling using open addressing (linear probing) to ensure data integrity.
- Customizable array size to control the number of possible hash collisions.
- Efficient key hashing and compression functions.

## Functions and Classes

### `HashMaps`

The `HashMap` class represents a simple key-value store using an array. It includes the following functions:

- `__init__(self, array_size)`: Constructor for initializing the HashMap with a specified array size.
- `hash(self, key, count_collisions=0)`: Hashes a key and returns a hash code, optionally considering collision count.
- `compressor(self, hash_code)`: Compresses a hash code to fit within the array size.
- `assign(self, key, value)`: Assigns a key-value pair to the HashMap, handling collisions.
- `retrieve(self, key)`: Retrieves the value associated with a specific key from the HashMap, considering collisions.

The `HashMap` class provides a basic yet functional key-value storage solution with collision handling. It uses open addressing to manage collisions, ensuring reliable data storage and retrieval.

Feel free to use this implementation as a foundation for more complex data structures or as a learning tool for understanding the inner workings of HashMaps.
