# User Lockout Management

## Overview

The User Lockout Management script is designed to handle user login attempts by implementing a lockout mechanism. This program provides functions to fetch the current Unix timestamp, calculate a lockout timestamp, determine the remaining lockout time, and check if the lockout period has elapsed.
## Features

- Fetch the current Unix timestamp.
- Calculate the timestamp for a user lockout, set to one minute from the current time.
- Calculate and display the time remaining for the lockout based on the current time and the lockout timestamp.
- Check if the current time has surpassed the user's lockout timestamp and allow for another login attempt when the lockout period has elapsed.
- Prompt the user to initiate another login attempt.

## Function Descriptions

 `get_current_timestamp()`

- Retrieves the current Unix timestamp, representing the number of seconds that have elapsed since January 1, 1970 (Coordinated Universal Time, UTC).
- Returns the current Unix timestamp as an integer value.

`lockout_timestamp()`

- Calculates and returns the timestamp for user lockout, typically set to one minute from the current Unix timestamp.

`remaining_time(lockout_timestamp)`

- Calculates and displays the time remaining for the lockout based on the current Unix time and the provided lockout timestamp.
- Returns a message with the remaining time in seconds.

`check_timestamp(user_timestamp)`

- Compares the current Unix time with the provided user lockout timestamp.
- If the current Unix time is greater than or equal to the lockout time, it allows another login attempt.
- If not, it invokes `remaining_time()` to display the remaining lockout time.

## Usage

1. Import the required libraries by running `from datetime import datetime`.

2. Use the provided functions to manage user lockout:
   - Call `lockout_timestamp()` to generate a user lockout timestamp.
   - Prompt the user to initiate another login attempt by pressing 1.
   - Call `check_timestamp(user_timestamp)` with the generated lockout timestamp to handle the lockout.

