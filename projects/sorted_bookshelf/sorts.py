import random

# This function implements the Bubble Sort algorithm to sort an array using the specified comparison function and sorting item.
def bubble_sort(arr, comparison_function, sorting_item):
  sorted = False
  
  while not sorted:
    sorted = True
    
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1], sorting_item):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
  return arr

# This function implements the Quicksort algorithm to recursively sort a list using the specified comparison function and sorting item.
def quicksort(list, start, end, comparison_function, sorting_item):
  
  if start >= end:
    return
  
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  
  for i in range(start, end):

    if comparison_function(pivot_element, list[i], sorting_item):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  quicksort(list, start, less_than_pointer - 1, comparison_function, sorting_item)
  quicksort(list, less_than_pointer + 1, end, comparison_function, sorting_item)