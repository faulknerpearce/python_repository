from itertools import combinations

# Checks if the total weight of items in a combination does not exceed the max weight.


def below_weight(arrays, max_weight):
    total_weight = 0

    for array in arrays:
        total_weight += array[1]

    return total_weight <= max_weight

# Returns a dictionary of below weight combinations.


def get_below_weight_combinations(arrays, maximum_weight):
    items_map = {}
    key = 0

    for i in range(1, len(arrays) + 1):
        for combination in combinations(arrays, i):

            if below_weight(combination, maximum_weight):
                items_map.update({key: list(combination)})
                key += 1

    return items_map

# Returns the combination that is below weight and has the greatest


def get_highest_value_combination(items_map):
    best_value_key = 0
    best_value = 0

    for key in items_map.keys():
        current_value = 0

        for item in items_map[key]:
            current_value += item[0]

        if current_value > best_value:
            best_value_key = items_map[key]

            best_value = current_value

    return best_value_key


if __name__ == '__main__':

    my_items = [[250, 1], [300, 3], [500, 5], [150, 2]]

    my_combinations = get_below_weight_combinations(my_items, 4)

    print(get_highest_value_combination(my_combinations))
