
# This will replace occurrences of a specified pattern in the string with a given substitute. Optionally case-sensitive; default is case-sensitive.
def replace_pattern(text, pattern, replacement, case_sensitive=True):
    formatted = ''
    end = len(pattern) -1
    idx = 0
    
    for i in range(0, len(text) - end):
        
        cur_pattern = text[i:i+len(pattern)] if case_sensitive else text[i:i+len(pattern)].lower()
        
        if cur_pattern == pattern:
            formatted += text[idx:i] + replacement
            idx = i + len(pattern)

    if i < len(text) - end:
        formatted += text[idx:]

    return formatted     

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."

format_one = replace_pattern(friends_intro, "zzz", '')

format_two = replace_pattern(format_one, '  ', ' ')

format_three = replace_pattern(format_two, "Language", "language")

format_four = replace_pattern(format_three, "pylhon", "Python", False)

format_five = replace_pattern(format_four, "idil", "ideal", False)

format_six = replace_pattern(format_five, "syntacs", "syntax")

format_seven = replace_pattern(format_six, "languuUuage", "language")

print(format_seven)