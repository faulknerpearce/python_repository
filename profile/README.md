# An Account Login Program

This Python script allows users to create an account and login to an existing account by entering their username and password

## About

The script will prompt the user to enter their username. If the username already exists in the profile list, the script prompts the user to enter their password. If the password matches the password associated with the username in the profile list, the script welcomes the user and exits the while loop. If the password does not match, the script prompts the user to try again or terminates the program if the user has no more tries.

If the username does not exist in the profile list, the script prompts the user to create an account by entering a new username. The script checks if the username is already taken and allows the user a maximum of three tries to enter a unique username. If the user successfully enters a unique username, the script prompts the user to create a password and enter their full name. The script then adds the new account information to the profile list.

The script runs until the user chooses to quit by entering "2"
