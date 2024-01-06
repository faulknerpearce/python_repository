# This will count the number of occurrences of a specified pattern in a given text.
def count_pattern(text, pattern):
    occurrences = 0
    n = len(pattern)
    
    for i in range(0, len(text) - (n-1)):
        current_string = text[i:i+n]
        if current_string == pattern:
            occurrences += 1
    
    return occurrences     

my_text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
my_pattern = "NEEDLE"

count = count_pattern(my_text, my_pattern)

print(f'The total count of pattern: {my_pattern}. was: {count}')
