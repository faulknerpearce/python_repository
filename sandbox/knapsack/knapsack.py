from itertools import combinations

# Check if a given combination is unique in a dictionary
def is_unique(new_combination, dict):
    for value in dict.values():
        if new_combination == value:
            return False
    return True

# Validate if the total weight of items in a combination does not exceed the max weight
def check_combination_weight(items, max_weight):
    total_weight = 0
    for item in items:
        total_weight += item[1]
    if total_weight <= max_weight:
        return True
    else:
        return False 

# Identify the combination with the highest value from a dictionary of item combinations
def get_best_value(items_dict):
    best_value_key = 0
    total = 0 
    for key in items_dict.keys():
        max_val = 0
        for item in items_dict[key]:
            max_val += item[0]

        if max_val > total:
            best_value_key = key
            total = max_val

    return items_dict[best_value_key]

# Generate all possible combinations of items that are below the specified weight limit
def below_weight_combinations(array, max_weight, key=0):
    bag = {}
    combination_length = (len(array))
    
    for i in range(len(array)):
        for combination in combinations(array, combination_length):
             
            if check_combination_weight(combination, max_weight):
                new_combination = sorted(list(combination))
         
                if is_unique(new_combination, bag):
                        bag.update({key: new_combination})
                        key +=1        
        
        combination_length -= 1
    return bag

# ________Main Program_________ #
my_weight_cap = 5

my_itmes = [[250, 1], [300, 3], [500, 5], [150, 1]]

below_weight_items = below_weight_combinations(my_itmes, my_weight_cap)

best_value = get_best_value(below_weight_items)

print(f'The best combination was: {best_value}')