# Generates the pattern for a given row in the Rangoli starting from a specified letter.
def get_pattern(start, size):
    letters = [chr(start + 97)]
      
    for i in range(start + 1, size):
        letters.append('-' + chr(int(i) + 97))
        letters.insert(0, chr(int(i) + 97) + '-')
    
    return letters

# Adds edge dashes to the given letters array to form a complete row in the Rangoli.
def add_edge_to_pattern(letters_array, size):
    for _ in range(size +1 * size):
        letters_array.append('-')
        letters_array.insert(0, '-')
    
    return ''.join(letters_array)

# Generates the list of strings representing the Rangoli of a given size.
def get_rangoli_list(size):
    rangoli = [''.join(get_pattern(0, size))]

    for i in range(1, size):
        letters_list = get_pattern(i, size)
        letters = add_edge_to_pattern(letters_list, i)

        rangoli.append(letters)
        rangoli.insert(0, letters)

    return rangoli

# Prints the generated Rangoli pattern.
def print_rangoli(rangoli):
    for line in rangoli:
        print(line)
                 
if __name__ == '__main__':
    
    # Generates and prints a Rangoli pattern of size 5.
    my_rangoli = get_rangoli_list(26)
    
    print_rangoli(my_rangoli)