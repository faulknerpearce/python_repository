# Perform a linear search on an array and return the indices of matches for a specified target value.
def replace_pattern(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)

  if len(matches) > 0:
    return matches
  
  raise ValueError("{0} not in list".format(target_value))

tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

tour_stops = replace_pattern(tour_locations, target_city)
print(tour_stops)   

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."

format_one = replace_pattern(friends_intro, "zzz", '')

format_two = replace_pattern(format_one, '  ', ' ')

format_three = replace_pattern(format_two, "Language", "language")

format_four = replace_pattern(format_three, "pylhon", "Python", False)

format_five = replace_pattern(format_four, "idil", "ideal", False)

format_six = replace_pattern(format_five, "syntacs", "syntax")

format_seven = replace_pattern(format_six, "languuUuage", "language")

print(format_seven)