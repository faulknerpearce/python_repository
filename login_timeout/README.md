# Login Lockout
Implements a 1 minute lockout after invalid login attempts.

## Overview
This script simulates a 1 minute lockout after too many failed logins using timestamp logic.

## Key functions:

### get_current_timestamp() 
- Fetch current time using a unix timestamp
### lockout_timestamp() 
- Generate 1 minute future timestamp
### remaining_time() 
- Calculate time left 
### check_timestamp() 
- Check if lockout elapsed

## Usage
Run the script and enter 1 when prompted to simulate a login attempt during lockout.
It will print the remaining lockout time, and allow login after 1 minute elapsed.

## How it works
The key steps are:

1. Generate 1 minute future lockout timestamp
2. On login attempt, compare current time vs lockout time
3. If current >= lockout, allow login
4. Else print remaining time and deny login
This provides a simple way to implement a time based lockout.