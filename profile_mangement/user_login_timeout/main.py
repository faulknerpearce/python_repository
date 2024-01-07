from timeout_functions import create_account, check_username, check_timestamp, remaining_time, check_password, lockout_timestamp

# Main program script. 
profile_dictionaries = { 
    0: {
        "Username": "firefly",
        "Password": "1234",
        "Name": "James Bancroft",  
        "Timeout": 0
        } 
     }

choice = input("\nWelcome, Press 1 to create an account, Press 2 to log in, Press 5 to exit: ")

# Log in loop. 
while choice == '1' or choice == '2':
    # User can create an account. 
    if choice == '1':
        choice = create_account(profile_dictionaries)
    
    # User can log in. 
    elif choice == '2':
        user_in = input("\nWelcome back. Please enter your username: ")
        username_found, id = check_username(profile_dictionaries, user_in)

        if username_found:
        
                # Check if the user has a timeout. 
                if check_timestamp(profile_dictionaries[id]["Timeout"]):
                    time = remaining_time(profile_dictionaries[id]["Timeout"])
                    print(f'You are still timed out. You have {time} seconds remaining. ')
                    choice = input("\nPress 2 to try again, press 5 to exit. ")
      
                else:
                    if profile_dictionaries[id]["Timeout"] > 0:
                        print("\nYour timeout has expired, you can log in again. ")
                    
                    password = input("\nPlease enter your password: ")
                    choice, password_found = check_password(profile_dictionaries, password, id)
        else: 
            choice = input("\nNo account found, press 1 to create an account, press 2 to try again, press 5 to exit: ")
    
if choice == '3' and password_found == True:
    person = profile_dictionaries[id]["Name"]
    print(f'\nWelcome back {person}.')

elif choice == '5':
    print("\nProgram terminated. ")
