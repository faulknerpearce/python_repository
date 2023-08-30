# Login Timeout
 This program implements user account creation, login, and lockout functionality.

## Features
- Create new user account
- Check username availability
- Set username, password, name
- Login with username and password
- Lockout after 3 failed attempts
- 1 minute lockout duration
- Countdown timer shown
- Lockout expires after time limit
- Main menu flow: Options to create account, login, or exit

## Code Overview

### Data Structures
- profiles: Dictionary holding user data Keys are numeric IDs
- Values are dictionaries with username, password, etc 

### Account Creation

#### username_availability() 
- Checks if username taken

#### create_account() 
- Gets user input and adds to profiles

### Login

#### check_username() 
- Finds ID for username if exists

### check_password()
 - Validates password, handles failures
Lockout

#### lockout_timestamp() 
- Sets timeout 1 minute from now

#### check_timestamp() 
- Checks if elapsed and lockout expired