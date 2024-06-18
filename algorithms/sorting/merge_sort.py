# Implement the merge sort algorithm to sort an array in ascending order.
def merge_sort(items):
    # Base case: if the array has one or zero elements, it is already sorted.
    if len(items) <= 1:
        return items
    
    # Split the array into two halves.
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    # Recursively sort the two halves.
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    # Merge the sorted halves into a single sorted array.
    return merge(left_sorted, right_sorted)

# Merge two sorted arrays into a single sorted array.
def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        
        if left[0] < right[0]:
            # Append the smaller element from the left array to the result.
            left_val = left.pop(0)
            result.append(left_val)
        else:
            # Append the smaller element from the right array to the result.
            right_val = right.pop(0)
            result.append(right_val)

    # Append any remaining elements from the left and right arrays.
    if left:
        result += left
    
    if right:
        result += right

    return result

#________Main Program_________ # 
if __name__ == "__main__":
    
    unordered_list = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]

    ordered_list = merge_sort(unordered_list)

    print(ordered_list)