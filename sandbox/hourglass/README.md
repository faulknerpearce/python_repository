# Hourglass Sum Calculator

## Overview

The Hourglass Sum Calculator is a Python script designed to compute the sums of all hourglass patterns in a 2D array and find the maximum hourglass sum. An hourglass pattern in a 2D array consists of three consecutive elements in the top row, one element in the middle row, and three consecutive elements in the bottom row, forming the shape of an hourglass.

## Features

- Calculates the sums of all hourglass patterns in a given 2D array.
- Identifies the maximum sum among all computed hourglass sums.

## Functions

`get_hourglass_sums(array)`

- Computes the sums of all hourglass patterns in the provided 2D array.
- Parameters:
  - `array`: The 2D array of numbers (as strings) to compute hourglass sums from.
- Returns:
  - A list of sums for all hourglass patterns found in the array.

`max_hourglass(array)`

- Finds the maximum hourglass sum in the given list of hourglass sums.
- Parameters:
  - `array`: The list of hourglass sums.
- Returns:
  - The maximum hourglass sum.
