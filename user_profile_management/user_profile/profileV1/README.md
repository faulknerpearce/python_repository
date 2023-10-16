# User Authentication Script: Password Only. 
This is a Python program that allows users to create/log into a profile. 
The program provides a command-line interface that prompts the user to enter their password and then checks if the password matches any existing profiles.
If a match is found, the program displays information about the user's account, including their ID number, name, and age. 
If no match is found, the program prompts the user to create a new account by entering their name and age.


## Functions
The program uses several functions to manage user profiles:

###  check_user()

This function takes two arguments: user_password, which is a string representing the password entered by the user, and profiles, which is a list of user profiles. 
The function checks if user_password matches any of the passwords in profiles. 
If a match is found, the function returns the index of the matching profile in profiles. If no match is found, the function returns the string "no match".

### found_account()

This function takes two arguments:
which is an integer representing the index of the matching profile in profiles, and profiles, which is a list of user profiles.
The function displays information about the user's account, including their ID number, name, and age.

### password_check()

This function takes one argument: profiles, which is a list of user profiles. The function prompts the user to enter a password and checks if the password meets certain requirements, 
such as being at least 8 characters long and containing at least one uppercase letter and one number. 
If the password is valid, the function returns the value 1. If the password is invalid, the function returns the value 0.

### make_account()

This function takes one argument: profiles, which is a list of user profiles. The function prompts the user to enter their name and age,
generates a unique ID number for the profile, and adds the new profile to profiles.
