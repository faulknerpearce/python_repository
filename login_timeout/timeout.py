
from datetime import datetime 

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
    msg = "You have " + str(round(remaining_time)) + " seconds remaining."
    return msg

# Function to check if the current time has surpassed the user's lockout timestamp.
def check_timestamp(user_timestamp):
    current_timestamp = get_current_timestamp()
    
    # If the current time is greater than or equal to the lockout time, allow another login attempt.
    if current_timestamp > user_timestamp:
        print("You can attempt another login")
    else:
    
        print(remaining_time(user_timestamp))

# Generate the user's lockout timestamp.
user_lockout = lockout_timestamp()

# Prompt the user to try logging in again.
user_in = input("Press 1 to log in again")

# If the user presses 1, check if the lockout time has passed.
if int(user_in) == 1:
    check_timestamp(user_lockout)
