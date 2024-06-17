from itertools import combinations

# Checks if the total weight of items in a combination does not exceed the max weight.
def below_weight(arrays, max_weight):
    total_weight = 0

    for array in arrays:
        total_weight += array[1]

    return total_weight <= max_weight

# Returns a dictionary of below weight combinations.
def get_below_weight_combinations(items, max_weight):
    valid_combinations = {}
    key = 0

    for i in range(1, len(items) +1):

        for combination in combinations(items, i):

            if below_weight(combination, max_weight):
                valid_combinations.update({key: combination})
                key += 1

    return valid_combinations

# Returns the combination that is below weight and has the greatest
def get_highest_value_combination(items_map):
    best_combination = 0
    best_value = 0

    for key in items_map.keys():
        current_value = 0

        for item in items_map[key]:
            current_value += item[0]

        if current_value > best_value:
            best_combination = items_map[key]

            best_value = current_value

    return best_combination


if __name__ == '__main__':

    my_items = [[250, 1], [300, 3], [500, 5], [150, 1]]

    my_combinations = get_below_weight_combinations(my_items, 5)

    print(get_highest_value_combination(my_combinations))
