# Perform binary search on a sorted list to find the target value.
def binary_search(sorted_list, target):
    # Initialize left and right pointers for the binary search
    left_pointer = 0
    right_pointer = len(sorted_list)
    
    # Perform binary search
    while left_pointer < right_pointer:
        # Calculate mid index and get corresponding value
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
        
        # Check if the target value is found at the mid index
        if mid_val == target:
            return mid_idx
        
        # Adjust pointers based on the target value and mid value comparison
        if target < mid_val:
            right_pointer = mid_idx
        elif target > mid_val:
            left_pointer = mid_idx + 1
    
    # Return a message if the target value is not in the list
    return "Value not in list"

# ________Main Program_________ # 
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))