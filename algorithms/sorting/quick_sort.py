# Implement the quicksort algorithm to sort an array in ascending order.
from random import randrange, shuffle 

def quicksort(list, start, end):
    # Base case: if the subarray has one or zero elements, it is already sorted.
    if start >= end:
        return

    # Choose a random pivot element and move it to the end of the array.
    pivot_index = randrange(start, end + 1)
    pivot_element = list[pivot_index]
    list[end], list[pivot_index] = list[pivot_index], list[end]

    # Initialize a pointer to track elements less than the pivot.
    less_than_pointer = start
    
    # Iterate through the subarray and partition elements based on the pivot.
    for i in range(start, end):
        if list[i] < pivot_element:
            # Swap elements less than the pivot with the current pointer position.
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1

    # Swap the pivot element back to its correct position.
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
    # Recursively sort the subarrays on the left and right of the pivot.
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)

#________Main Program_________ # 
if __name__ == "__main__":

    unsorted_list = [3,7,12,24,36,42]
    shuffle(unsorted_list)
    print(unsorted_list)

    quicksort(unsorted_list, 0, len(unsorted_list) - 1)
    print(unsorted_list)