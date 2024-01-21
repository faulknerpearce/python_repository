import random

# Creates a list of socks with specified colors.
def create_socks(pairs):
    socks = []
   
    for colour in range(pairs):
        for _ in range(10):
            socks.append(colour)
    
    return socks

# Simulates finding a pair of socks in a shuffled list.
def find_pair(socks):
    collected_socks = {}
    turns = 0

    for sock in socks:
        turns += 1

        if collected_socks.get(sock, 0):
            collected_socks[sock] += 1
            if collected_socks[sock] == 2:
                return turns
        else:
            collected_socks.update({sock: 1})
    
    return turns

# Simulates finding pairs multiple times and records the number of turns.
def generate_tires(socks, amount_of_tries):
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
if __name__ == '__main__':

    my_socks = create_socks(2)

    my_tires = generate_tires(my_socks, 1000)

    the_average = calculate_average(my_tires)

    print(f'The average number of atempts needed to get a pair of socks is: {the_average}')