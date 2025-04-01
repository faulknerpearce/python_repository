# Swaps the case of each letter in the given string: uppercase letters become lowercase, lowercase letters become uppercase.
def swap_case(s):
    result = ''

    for char in s:
        character = ord(char)
    
        if character >= 65 and character <= 90:
            character += 32
   
        elif character >= 97 and character <= 122:
            character -= 32
        
        converted = chr(character)
        result += converted
    
    return result

if __name__ == '__main__':

    my_sentence = 'HackerRank.com presents "Pythonist 2".'

    swapped_sentence = swap_case(my_sentence)

    print(swapped_sentence)
