import random

# Generates a list containing ten socks for each specified color.
def create_socks_list(colours):
    return [i for i in range(colours) for _ in range(10)]

# Simulates finding a pair of socks in a shuffled list.
def find_pair(socks_draw):
    collected_socks = {}
    tries = 0 

    for sock in socks_draw:
        tries += 1

        if collected_socks.get(sock):
            collected_socks[sock] += 1
            break
        else:
            collected_socks.update({sock: 1})

    return tries 

# Simulates finding pairs multiple times and records the number of turns.
def generate_tires_arr(socks, amount_of_tries):
    result = []

    for _ in range(amount_of_tries):
        random.shuffle(socks)
        tires = find_pair(socks)
        result.append(tires)

    return result
        
# Calculates the average value of the array of attempts.
def calculate_average(arr):
    total = sum(arr)
    average = total / len(arr)

    return round(average)

# ________Main Program_________ #
my_socks = create_socks_list(2)

my_tires = generate_tires_arr(my_socks, 1000)

the_average = calculate_average(my_tires)

print(f'The average number of atempts needed to get a pair of socks is: {the_average}')