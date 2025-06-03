import utils
import sorts

# This function compares books based on the first character of a specific item associated with the given key
def sort_by_ascending(book_a, book_b, item):

    if ord(book_a[item][0]) > ord(book_b[item][0]):
        return True
    
    return False 

# This function compares books by the combined length of specific items associated with given keys.
def sort_by_length(book_a, book_b, items):

    # Unpack the items in the list. 
    item_a, item_b = items[0], items[1]

    if len(book_a[item_a]) + len(book_a[item_b]) > len(book_b[item_a]) + len(book_b[item_b]):
        return True
    
    return False

def print_books(books, key):
    for book in books:
        print(book[key])

# ________Main Program_________ #
bookshelf_v1 = utils.load_books('books_small.csv')

bookshelf_v2 = utils.load_books('books_large.csv')

# # Sort using the Bubble sort function. 
sorted_by_title = sorts.bubble_sort(bookshelf_v1, sort_by_ascending, 'title_lower')

# sort using the quicksort function. 
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) -1, sort_by_ascending, 'author_lower')

print_books(sorted_by_title, 'title_lower')





