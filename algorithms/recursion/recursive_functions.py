
# Recursively prints each element in a list.
def print_name(name):
    if len(name) == 0:
        print('All done.')
    else:
        print(name[0])
        print_name(name[1:])

# Sum of elements in a list using recursion.
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

# Recursively sums integers from n to 1.
def sum_to_one(n):
    if n == 0:
        return 0
    else:
        print(f'Recursing with input: {n}')
        return n + sum_to_one(n - 1)

# Recursive factorial function.
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive Fibonacci sequence.
def fibonacci(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Sum of digits in an integer using recursion.
def sum_digits(n):
    if n <= 9:
        return n
    else:
        result = n % 10
        return sum_digits(n // 10) + result

# Recursively finds the minimum value in a list.
def find_min(my_list, minimum=None):
    if not my_list:
        return minimum

    if not minimum or my_list[0] < minimum:
        minimum = my_list[0]
    return find_min(my_list[1:], minimum)

# Checks if a string is a palindrome using recursion.
def is_palindrome(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome(str[1:-1])

# Recursive multiplication of two numbers.
def multiplication(num_a, num_b):
  if num_a == 0 or num_b == 0:
    return 0

  return num_a + multiplication(num_a, num_b - 1)

# Recursive multiplication of two numbers.]
def move_to_end(lst, val):
  result = []
  if len(lst) == 0:
    return []
      
  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)

  return result

# Wraps a string with specified characters n times.
def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  result += "<"
  result += wrap_string(str, n-1)
  result += ">"

  return result

# Reverses the elements of a list using recursion.
def reverse_list(the_list):
    # Base case
    if len(the_list) == 0:
        return []
    else:
        return [the_list[-1]] + reverse_list(the_list[:-1])
