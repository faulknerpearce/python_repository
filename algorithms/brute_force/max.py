#Linear Search Algorithm

# This will traverse an array and retun the max value.
def linear_search(search_list):
  max_val = None

  for i in range(len(search_list)):
    if not max_val or search_list[i] > max_val:
      max_val = search_list[i]
    
  return max_val

test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

highest_score = linear_search(test_scores)

print(highest_score)