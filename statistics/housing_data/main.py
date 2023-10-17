import csv

# This function will calculate the average price of the homes. 
def calculate_mean(prices):
    total = sum([int(price) for price in prices])
    mean = total / len(prices)
    return round(mean, 2)

# This function will calculate the median of a list of numbers
def calculate_median(nums):
    nums.sort()
    i = len(nums) // 2
    
    if len(nums) % 2 == 0:
        median = (int(nums[i - 1]) + int(nums[i])) / 2.0
    else:
        median = nums[i]
    
    return float(median)

# This function will count the frequencies of numbers in a list and add number and the frequency of the number to a dictionary.
def count_frequencies(nums):
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else: 
            nums_dict.update({num: 1})
    return nums_dict

# Function to calculate the mode(s) from a dictionary of frequencies
def calculate_mode(numbers):
    nums = count_frequencies(numbers)
    most_frequent = max(nums.values()) 
    modes_result = []

    for key, value in nums.items():
        if value == most_frequent:
            modes_result.append([key])
            modes_result[-1].append(value)
        
    return modes_result

# This function will read from a CSV file and convert it to a dictionary. 
def csv_to_dictionary(csv_file):
    data = {}
    with open(csv_file, 'r') as file:
        content = csv.DictReader(file)
        for row in content:
            for key, value in row.items():
                if key not in data:
                    data.update({key: []})

                data[key].append(value)
    return data

# Read in housing data
brooklyn_one_bed = csv_to_dictionary('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

# Add mean calculations below
brooklyn_mean = calculate_mean(brooklyn_price) 


# Add median calculations below
brooklyn_median = calculate_median(brooklyn_price)


# Add mode calculations below
brooklyn_mode = calculate_mode(brooklyn_price)
 
print(f"The averange price for a Brooklyn one bedroom appartment is: ${brooklyn_mean}")
print(f"The median price for a Brooklyn one bedroom appartment is: ${brooklyn_median}")
print(f"The mode price for a Brooklyn one bedroom appartment is: ${brooklyn_mode[0][0]} and it appears {brooklyn_mode[0][1]} times.")








