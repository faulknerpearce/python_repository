my_sentence = 'HackerRank.com presents "Pythonist 2".'

def swap_case(s):
    result = ''

    for char in s:
        character = ord(char)
        
        # Check if the character is uppercase.
        if character >= 65 and character <= 90:
            character += 32
        # Check if the character is lowercase.
        elif character >= 97 and character <= 122:
            character -= 32
        
        converted = chr(character)
        result += converted
    return result
