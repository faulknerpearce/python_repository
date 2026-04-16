def binary_search(sorted_list, target):
    # Check if the list is empty, indicating that the value cannot be found
    if not sorted_list:
        return 'value not found'
    
    # Calculate the index and value of the middle element
    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]
    
    # Check if the middle value is equal to the target
    if mid_val == target:
        return mid_idx
    
    # If the target is smaller than the middle value, perform binary search on the left half
    elif mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)
    
    # If the target is larger than the middle value, perform binary search on the right half
    elif mid_val < target:
        right_half = sorted_list[mid_idx + 1:]
        result = binary_search(right_half, target)
        
        # If the target is not found in the right half, return 'value not found'
        if result == "value not found":
            return result
        else:
            # Adjust the result by adding the index of the middle element in the original list
            return result + mid_idx + 1

# ________Main Program_________ # 
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))