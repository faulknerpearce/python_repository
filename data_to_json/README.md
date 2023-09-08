# User Data Recorder

This Python script is a simple user data recorder that allows users to create a username, provide their full name, and records the current Unix timestamp.

## Features

- Prompts users to create a username and enter their full name.
- Timestamp: Records the current Unix timestamp to track when the data was collected.
- Data Storage: Stores user data in a JSON file for easy retrieval.

## Functions

`get_data()`

- This function collects user data.
- It prompts the user to create a username and provide their full name.
- It records the current Unix timestamp.
- Returns the username, full name, and timestamp as a tuple.

`create_dict(username_data, name_data, timestamp_data)`

- This function creates a dictionary with the provided user data.
- It takes three parameters: username, full name, and timestamp.
- Returns a dictionary with keys "Username," "Name," and "Timestamp."

### Main Logic

- The script collects user data using `get_data()`.
- It creates a dictionary with the collected data using `create_dict()`.
- Checks if user data exists.
- If user data is present, it writes the data to a JSON file named "user_data.json."

Please note that this script doesn't include extensive error handling or validation. You can enhance it to suit your specific requirements.

Enjoy using this simple user data recorder!
