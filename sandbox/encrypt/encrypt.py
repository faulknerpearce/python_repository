import random

# Shifts a letter by a given amount for encryption or decryption
def shift_letter(letter, amount, encrypt):
    if encrypt:
        return (ord(letter) + amount)
    else:
        return (ord(letter) - amount)


# Encrypts or decrypts a single letter using a shift amount
def encrypt_decrypt(letter, amount, encrypt):

    shifted = shift_letter(letter, amount, encrypt)
    result = (shifted - 97) % 26

    return chr(result + 97)


# Encrypts a string, returning the encrypted string and the list of shift numbers
def encrypt_string(string):
    result = ''
    numbers = []

    for letter in string:

        num = random.randint(1, 26)
        numbers.append(num)
        result += encrypt_decrypt(letter, num, True)
        
    return result, numbers

# Decrypts a string using the provided list of shift numbers
def decrypt_string(string, numbers):
    result = ''

    for i in range(len(string)):
        result += encrypt_decrypt(string[i], numbers[i], False)

    return result

if __name__ == '__main__':

    name, numbers = encrypt_string('austin')

    print(f'The encrypted string is: {name} The encryption numbers are: {numbers}')

    name = decrypt_string('jvsjyd', [9, 1, 26, 16, 16, 16])

    print(name)
