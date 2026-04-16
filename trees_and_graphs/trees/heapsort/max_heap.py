class MaxHeap:
  
  def __init__(self):
    # Initialize an empty heap list with a None placeholder at index 0.
    self.heap_list = [None]
    # Track the number of elements in the heap.
    self.count = 0

  def parent_idx(self, idx):
    # Calculate the index of the parent of a given index.
    return idx // 2

  def left_child_idx(self, idx):
    # Calculate the index of the left child of a given index.
    return idx * 2

  def right_child_idx(self, idx):
    # Calculate the index of the right child of a given index.
    return idx * 2 + 1
  
  def add(self, element):
    # Add an element to the heap and perform heapify-up.
    self.count += 1
    print(f'Adding: {element} to {self.heap_list}.')
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    # Restore the heap property by moving a newly added element up.
    print('Heapifying up.')
    idx = self.count

    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]

      if parent < child:
        print(f'swapping {parent} with {child}.')
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
      print("Heap Restored {0}".format(self.heap_list))
  
  def heapify_down(self):
    # Restore the heap property by moving the first element down.
    idx = 1
    
    while self.child_present(idx):
      print('Heapifying down.')
      larger_child_idx = self.get_larger_child_idx(idx)
      parent = self.heap_list[idx]
      child = self.heap_list[larger_child_idx]

      if parent.value < child.value:
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent

      idx = larger_child_idx
    print(f'Heap Restored. {self.heap_list}')
  
  def retrieve_max(self):
    # Remove and return the maximum element from the heap.
    if self.count == 0:
      print('No items in heap.')
      return None
    
    max_val = self.heap_list[1]
    print(f'Removing: {max_val} from {self.heap_list}.')
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print(f'Last element moved to first: {self.heap_list}.')
    self.heapify_down()
    return max_val
  
  def get_larger_child_idx(self, idx):
    # Determine the index of the larger child of a given index.
    if self.right_child_idx(idx) > self.count:
      print('There is only a left child.')
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]

      if left_child > right_child:
        print(f'Left child {left_child} is larger than right child {right_child}.')
        return self.left_child_idx(idx)
      else:
        print(f'Right child {right_child} is larger than left child {left_child}.' )
        return self.right_child_idx(idx)
