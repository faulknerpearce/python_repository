# Weekday Checker

## Overview

The **Weekday Checker** is a Python script that helps you determine the current day of the week. It is a simple utility class that can be used to retrieve the name of the day (e.g., "Monday," "Tuesday") based on the current date and time.

## Features

- Get the current day of the week.
- Simple and easy-to-use class.
- Utilizes Python's built-in `datetime` module for accurate results.

## Functions and Classes

### `Weekday` Class

- **Description**: The `Weekday` class is a utility class for retrieving the current day of the week.
- **Constructor**:
    - `__init__(self)`: Initializes the `Weekday` object with a list of days of the week.
- **Methods**:
    - `get_weekday(self)`: Returns the name of the current day of the week based on the system's date and time.

## Usage

1. Create an instance of the `Weekday` class:
    ```python
    today = Weekday()
    ```

2. Retrieve the current day of the week:
    ```python
    current_day = today.get_weekday()
    print(f"Today is {current_day}.")
    ```

This script can be helpful in various applications where you need to perform actions or display information based on the current day of the week.

