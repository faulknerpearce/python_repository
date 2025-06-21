def get_string():
    file = open("text.txt", "r")
    text = file.read() 
    file.close()
    return text 

def fix_list(my_list, a, b):
    new_list = []
    for item in my_list:
        new_item = item.replace(a, b)
        new_list.append(new_item)
    return new_list

# This function will populate to 3 strings from the sorted contents of one list. 
def populate_lists(string_list, list_1, list_2, list_3):
    i = 0 
    while i < len(string_list):
        list_1.append(string_list[i])
        list_2.append(string_list[i+1])
        list_3.append(string_list[i+2])
        i += 4
    return list_1, list_2, list_3

# This function will calculate the total sales from the sales list.
def get_total(store_sales):
    total = 0 
    for sale in store_sales:
        total += float(sale)
    rounded = round(total, 2)
    return rounded

# This function splits each string in the provided list at the "&" character and returns a flattened list of the results.
def split_thread(store_threads):
    threads_split = []
    for colours in store_threads:
        if "&" in colours:
            temporary = colours.split("&")
            for colour in temporary:
                threads_split.append(colour)
        else:
            threads_split.append(colours)
    return threads_split

def colour_count(my_list, colour):
    count = 0
    for element in my_list:
        if colour in element:
            count += 1 
    return count

# Convert the text.txt file to a string.
daily_sales = get_string()

# First set of sting refinements, using the replace module. 
daily_sales_replaced = daily_sales.replace(";,;", ",")
# Second set of string refinements, using the replace module. 
daily_sales_fixed = daily_sales_replaced.replace(" ", "")

# create a list from the refined string, using the split module.
sales_list = daily_sales_fixed.split(",")

# Using my fix_list function to refine the list. 
removed_commas = fix_list(sales_list, ",", "")

# Second set of list refinements. 
removed_new_lines = fix_list(removed_commas, "\n", "")

# Third set of refinements.
transactions_clean = fix_list(removed_new_lines, '"""', '')

empty_customers = []
empty_sales = []
empty_thread_sold = []

customers, sales, thread_sold = populate_lists(transactions_clean, empty_customers, empty_sales, empty_thread_sold)
# Remove the dollar symbol from the sales list. 
fixed_sales = fix_list(sales, "$", "")

total_sold = get_total(fixed_sales)

thread_sales_split = split_thread(thread_sold)

thread_shed_colours = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

i = 0
template = "We sold {} Threads of {}\n"
formated = "" 

while i < len(thread_shed_colours):
    count = colour_count(thread_sales_split, thread_shed_colours[i])
    formated += template.format(str(count), thread_shed_colours[i].title())
    i += 1

print(formated)  

    
