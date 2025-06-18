# Reverses a list in place.
def reverse_list(lst):
    end = len(lst) // 2
    
    for i in range(end):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
    return lst

# Reverses a string by converting it to a list, reversing the list, and then joining it back into a string.
def reverse_string(string_item):
    lst = list(string_item)
    end = len(lst) // 2
    
    for i in range(end):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
    
    return ''.join(lst)
    
if __name__ == '__main__':
 
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    my_string = 'Hello World!'

    print(reverse_list(my_list))

    print(reverse_string(my_string))