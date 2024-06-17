# Cloud Jumping Algorithm

## Overview

The Cloud Jumping Algorithm is a Python script designed to calculate the minimum number of jumps needed to reach the end of an array representing clouds. Each element in the array can either be a cumulus cloud (`0`) or a thunderhead cloud (`1`). The player can jump to the next cloud or skip one cloud if it is safe (i.e., a cumulus cloud).

## Features

- Determines if the current index is at the last element of the array.
- Checks if a double jump (jump of two steps) is possible and safe.
- Calculates the minimum number of jumps needed to reach the end of the cloud array.

## Functions

### `at_end(index, n)`

- Checks if the current index is at the last element of the array.
- Parameters:
  - `index`: The current index.
  - `n`: The length of the array.
- Returns:
  - `True` if the current index is at the last element, `False` otherwise.

### `can_double_jump(arr, n)`

- Checks if a double jump (jump of two steps) is possible and will land on an index containing a value of `0`.
- Parameters:
  - `arr`: The array representing the clouds.
  - `n`: The current index.
- Returns:
  - `True` if a double jump is possible and safe, `False` otherwise.

### `jump_clouds(arr, n)`

- Calculates the minimum number of jumps needed to reach the end of the cloud array.
- Parameters:
  - `arr`: The array representing the clouds.
  - `n`: The length of the array.
- Returns:
  - The minimum number of jumps needed to reach the end of the array.
