
# This will replace occurrences of a specified pattern in the string with a given substitute. Optionally case-sensitive; default is case-sensitive.
def replace_pattern(text, pattern, replacement, case_sensitive=True):
    fixed_text = ''
    n = len(pattern)
    last_index = 0

    formatted_pattern = pattern if case_sensitive else pattern.lower()
    
    for index in range(0, len(text) - (n-1)):
    
        current_string = text[index:index+n]

        formatted_string = current_string if case_sensitive else current_string.lower()
         
        if formatted_string == formatted_pattern:
                fixed_text += (text[last_index:index])
                fixed_text += replacement 
                last_index = (index + n)
        
    fixed_text += text[last_index:]
            
    return fixed_text     

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."

format_one = replace_pattern(friends_intro, "zzz", '')

format_two = replace_pattern(format_one, '  ', ' ')

format_three = replace_pattern(format_two, "Language", "language")

format_four = replace_pattern(format_three, "pylhon", "Python", False)

format_five = replace_pattern(format_four, "idil", "ideal", False)

format_six = replace_pattern(format_five, "syntacs", "syntax")

format_seven = replace_pattern(format_six, "languuUuage", "language")

print(format_seven)