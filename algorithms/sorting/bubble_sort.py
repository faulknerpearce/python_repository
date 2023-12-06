# Implement the bubble sort algorithm to sort an array in ascending order.
def bubble_sort(arr):
    # Iterate through the array to perform comparisons and swaps.
    for i in range(len(arr)):
        for index in range(len(arr) - i - 1):
            # Swap adjacent elements if they are in the wrong order.
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return arr 

# ________Main Program_________ # 
nums = [5, 2, 9, 1, 5, 6]

sorted_array = bubble_sort(nums)

print(sorted_array)