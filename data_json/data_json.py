# Import necessary modules.
from datetime import datetime
import json

# Function to get user data: username, full name, and current Unix timestamp.
def get_data():
    while True:
        input_username = input("Please create a username: ")
        input_name = input("Please enter your full name: ")
        
        # Ensure that the input data fields are not empty. 
        if input_username and input_name:
            unix_time = datetime.now().timestamp()
            return input_username, input_name, unix_time
        else:
            print("Username and full name cannot be empty. Please provide valid inputs. ")

# Function to create a dictionary with provided user data.
def create_dict(username_data, name_data, timestamp_data):
    data_dict = {}
    data_dict.update({"Username": username_data, "Name": name_data, "Timestamp": timestamp_data})
    return data_dict

# Collect user data.
username, name, timestamp = get_data()

# Create a dictionary with the user data.
user_data = create_dict(username, name, timestamp)

# Check if user data exists.
if user_data:
    # Write user data to a JSON file.
    with open("user_data.json", "w") as user_data_json:
        json.dump(user_data, user_data_json)
