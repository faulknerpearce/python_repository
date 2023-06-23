# User Authentication Script

This script provides a simpl user authentication system with features such as locating existing accounts, verifying passwords, creating new accounts, and checking username availability.

## Features
- Username and password checking: The script locates the entered username and verifies the corresponding password.
- Account creation: Users can create a new account by providing a unique username and password.
- Existing account check: The script ensures that the chosen username is not already taken.
- Login functionality: Users can log in using their username and password.
- User interaction: The script prompts users for their name, provides options for account creation or login, and displays relevant messages based on user actions.

## Functions 

### username_check()
-Locates the entered userName in the user_list.
-Prompts for the corresponding password.
-Calls the password_check function.
-Returns the username (theUser) and the option (option).
-Offers an option to create a new account if the username is not found.

### password_check()
-Verifies the entered userPassWord against the password in the user_list.
-Allows a limited number of password tries (tries).
-Prompts the user for input.
-Returns the username (theName) and the option (option) upon successful password verification.

### create_account()
-Facilitates the creation of a new account.
-Checks if the userName is available using the available function.
-Prompts the user to create a password.
-Adds the username and password to the user_list.
-Returns an option for further processing.
-Provides an option to try again if the username is already taken.

### available()
-Checks if a given name already exists in the user_list.
-Iterates through the list to find a match.
-Returns True if the name is taken, False if it's available, and None if no match is found.