
from datetime import datetime 

# Function to fetch the current hour and minute.
def get_current_time():
    current_time = datetime.now()  # Fetch the current datetime object
    hour = current_time.hour  # Extract the hour
    minute = current_time.minute  # Extract the minute
    return hour, minute
 
# Function to determine the lockout timestamp, which is one minute from the current time.
def lockout_timestamp():
    lockout_hour, lockout_minute = get_current_time()

    # Handle the edge case where the current minute is 59.
    if lockout_minute == 59:
        lockout_hour += 1  # Increment the hour
        lockout_minute = 0  # Reset the minute to 0
    else:
        lockout_minute += 1  # Otherwise, just increment the minute

    timestamp = (lockout_hour, lockout_minute)
    return timestamp

# Function to calculate the time remaining for the lockout based on the current time and the lockout timestamp.
def remaining_time(current_minute, lockout_minute):
    seconds = datetime.now().second  # Fetch the current second

    # If the current minute is the same as the lockout minute, calculate the seconds remaining in the current minute.
    if current_minute == lockout_minute:
        remaining_seconds = 60 - seconds
    else:
        # Otherwise, calculate the total seconds remaining including the difference in minutes.
        remaining_seconds = (lockout_minute - current_minute - 1) * 60 + 60 - seconds
    
    msg = "You have " + str(remaining_seconds) + " seconds remaining."
    return msg

# Function to check if the current time has surpassed the user's lockout timestamp.
def check_timestamp(user_timestamp):
    current_hour, current_minute = get_current_time()
    timestamp_hour, timestamp_minute = user_timestamp

    # If the current time is greater than or equal to the lockout time, allow another login attempt.
    if current_hour > timestamp_hour or (current_hour == timestamp_hour and current_minute >= timestamp_minute):
        print("You can attempt another login")
    else:
        # Otherwise, print the time remaining for the lockout.
        print(remaining_time(current_minute, timestamp_minute))

# Generate the user's lockout timestamp.
user_lockout = lockout_timestamp()

# Prompt the user to try logging in again.
user_in = input("Press 1 to log in again")

# If the user presses 1, check if the lockout time has passed.
if int(user_in) == 1:
    check_timestamp(user_lockout)
