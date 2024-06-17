# Checks if the current index is at the last element of the array.
def at_end(index, n):
    return index == n - 1

# Checks if a double jump (jump of two steps) is possible and will land on an index containing a value of 0.
def can_double_jump(arr, n):
    return (n + 2) < len(arr) and arr[n + 2] == 0

# Calculates the minimum number of jumps needed to reach the end of the cloud array.
def jump_clouds(arr, n):
    jumps = 0 
    i = 0

    for _ in range(n):
        jumps += 1
        
        if can_double_jump(arr, i):
            i += 2
        else:
            i += 1 
        
        if at_end(i, n):
            return jumps
         
if __name__ == '__main__':
 
    test_one = [0, 0, 1, 0, 0, 1, 0]

    print(f'Total Jumps: {jump_clouds(test_one, 7)}')