def capitalize_first_letter(my_string):

  # Check if string is empty
  if my_string:

    # Get ASCII code of first character
    character = ord(my_string[0])  

    # Check if it's a lowercase letter
    if character >= 97 and character <= 127:

      # Subtract 32 to make uppercase 
      character -= 32
    
    # Convert ASCII code back to char   
    capitalized = chr(character)

    # Add rest of string back on
    capitalized += my_string[1:]

  # Return capitalized string
  return capitalized

print(capitalize_first_letter("hello, world"))