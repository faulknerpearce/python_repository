from datetime import datetime 

# This function will compare the inputed username to the usernames stored in the profiles dictionary, and it will return a bool bassed on the result. 
def username_availability(profiles_dict, username):
    for id in range(len(profiles_dict)):
        if username in profiles_dict[id]["Username"]:
            return False
        else:
            return True
  
# Function to create an account.  
def create_account(profiles_dict):
    create_choice = 4
    while int(create_choice) == 4:
        user_username = input("Create a username: ")
        # Check for a unique username. 
        if username_availability(profiles_dict, user_username):
            id = len(profiles_dict)
            password = input("Username successfully created.\nCreate a password: ")
            name = input("password successfully created.\nEnter your name: ")
            # Update the profiles dictionary with the new user information. 
            profiles_dict.update( {id: {"Username": user_username, "Password": password, "Name": name} })
            create_choice = input("Account created, Press 2 to log in: ")
        else:
            create_choice = input("That username is taken. press 4 to try another, Press 5 to exit ")
    return create_choice
    
# This function will check for a mach from an inputed username and compare it to the existing userrnames. 
def check_username(user_profiles, username):
    for id, profile in user_profiles.items():
        if profile["Username"] == username:
            return True, id  
    return False, None

# This function will check if the inputed password matches the users saved password. 
def check_password(user_profiles, password, id):
    tries = 0
    while tries < 1:
        if password in user_profiles[id]["Password"]:
            password_choice = input("Login successful. Press 3 to enter the applicartion: ")
            return password_choice, id, False
        else:
            tries += 1
            password = input("Incorrect password, try again: ")
    # add the lockout here if the tries exceed 3 but the user still wishes to log in 
    if tries == 1:
        timeout = lockout_timestamp()
        user_profiles[id].update({"Timeout": timeout})
        password_choice = input("You have been timed out Press 2 to try again, Press 5 to exit. ")
        return password_choice, id, True
    
# Function to fetch the current hour and minute.
def get_current_timestamp():
    current_timestamp = datetime.now().timestamp()  
    return current_timestamp
 
# Function to determine the lockout timestamp, which is one minute from the current time.
def lockout_timestamp():
    user_lockout_timestamp = get_current_timestamp() + 60
    return user_lockout_timestamp

# Function to calculate the time remaining for the lockout based on the current time and the lockout timestamp.
def remaining_time(lockout_timestamp):
    current_timestamp = get_current_timestamp()
    remaining_time = lockout_timestamp - current_timestamp 
    return f"You have {round(remaining_time)} seconds remaining "
    
# Function to check if the current time has surpassed the user's lockout timestamp.
def check_timestamp(user_timestamp):
    current_timestamp = get_current_timestamp()
    # If the current time is greater than or equal to the lockout time, allow another login attempt.
    if current_timestamp > user_timestamp:
        return False
    else:
        return True

# Main program script. 
profile_dictionaries = { 
    0: {
        "Username": "firefly",
        "Password": "1234",
        "Name": "James Bancroft", 
        "Points": 100
        } 
     }

choice = input("\n\nWelcome, Press 1 to create an account, Press 2 to log in, Press 5 to exit: ")

# Log in loop. 
while int(choice) == 1 or int(choice) == 2:
    # User can create an account. 
    if int(choice) == 1:
        choice = create_account(profile_dictionaries)
    # User can log in. 
    elif int(choice) == 2:
        user_in = input("Welcome to the application. Please enter your username: ")
        username_found, id = check_username(profile_dictionaries, user_in)

        if username_found:
            # Check if the user has a timeout. 
            if profile_dictionaries[id].get("Timeout", 0):
                
                # Check the remaining time for the user.
                if check_timestamp(profile_dictionaries[id]["Timeout"]):
                    time = remaining_time(profile_dictionaries[id]["Timeout"])
                    print(time)
                    choice = input("Press 2 to try again, press 5 to exit. ")
                # Remove timestamp from the user. 
                else:
                    print("Your timeout has expired, you can log in again. ")
                    profile_dictionaries[id].pop("Timeout")
            else:
                password = input("please enter your password: ")
                choice, password_found, user_timeout = check_password(profile_dictionaries, password, id)
                
                # Assign a lockout timestamp to the user. 
                if user_timeout == True:
                    timeout = lockout_timestamp()
                    profile_dictionaries[id].update({"Timeout": timeout})
                    print(profile_dictionaries[id])
        else: 
            choice = input("No account found, press 1 to create an account, press 2 to try again, press 5 to exit: ")
       

if int(choice) == 3 and password_found == True:
    person = profile_dictionaries[id]["Name"]
    print(person)

else: 
    print("Program terminated. ")
