import csv

# This function will get data from a CSV file
def get_data():
    with open("top-hundred-books.csv", "r") as csv_file:
        # Use csv.DictReader to read the file and convert it into a list of dictionaries
        data = list(csv.DictReader(csv_file))
        return data

# This function will calculate the average age of authors in the data set
def calculate_average_age(data):
    # Create a list of ages by extracting the "Ages" field from each dictionary and converting it to an integer
    my_list = [int(row["Ages"]) for row in data]
    total = sum(my_list)
    average = total / len(my_list)
    return int(average)

csv_data = get_data()

# Call the calculate_average_age function to calculate the average age of authors
average_age = calculate_average_age(csv_data)

# Print the calculated average age as an integer
print(f"The average age of these authors is: {average_age}")
