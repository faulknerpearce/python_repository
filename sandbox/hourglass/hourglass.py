# Computes the sums of all hourglass patterns in a 2D array.
def get_hourglass_sums(array):
    sums = []
    for row in range(len(array) - 3 + 1):

        for col in range(len(array) - 3 + 1):
        
            hourglass = array[row][col:col+3]
            hourglass.insert(-1, array[row+1][col+1])
            hourglass += array[row+2][col:col+3]
            
            sums.append((sum(map(int, hourglass))))

    return sums
        
# Finds the maximum hourglass sum in the given array of sums.
def max_hourglass(array):
    max_hourglass = None

    for num in array:
        if max_hourglass is None or num > max_hourglass:
            max_hourglass = num
    return max_hourglass
    
if __name__ == '__main__':
    # Define a 2D array of numbers as strings
    numbers = [['-9', '-9', '-9', '1', '1', '1'], 
               ['0', '-9', '0', '4', '3', '2'], 
               ['-9', '-9', '-9', '1', '2', '3'], 
               ['0', '0', '8', '6', '6', '0'], 
               ['0', '0', '0', '-2', '0', '0'], 
               ['0', '0', '1', '2', '4', '0']]

    # Compute the sums of all hourglass patterns in the 2D array
    hourglass_sums = get_hourglass_sums(numbers)

    # Find and print the maximum hourglass sum.
    print(max_hourglass(hourglass_sums))