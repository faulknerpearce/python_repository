# Import the CSV module for reading CSV files.
import csv 

# Initialize an empty dictionary to store the library data.
library = {}

# Open the "books.csv" file for reading.
with open("books.csv") as books:
    # Read the entire contents of the file into a string.
    content = books.read()

# Replace newline characters with "@" to facilitate splitting the content.
data = content.replace("\n", "@")

# Split the content into a list based on "@" as the delimiter.
data_list = data.split("@")

# Remove the first 4 elements from the list, which are not needed.
data_list = data_list[4:]

# Define a function to populate the dictionary with author, ISBN, and book information.
def populate_dict(dictionary, data_list):
    while len(data_list) > 0:
        # Extract the author, ISBN, and book information from the list.
        author = data_list.pop(0)
        isbn = data_list.pop(0)
        book = data_list.pop(0)
        
        # Update the dictionary with the author as the key and book information as the value.
        dictionary.update({author: {"Book": book, "ISBN": isbn}})
    return dictionary

# Call the populate_dict function to create the authors_library dictionary.
authors_library = populate_dict(library, data_list)

print(authors_library)

