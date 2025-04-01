import random

def shift_letter(letter, amount, encrypt):
    if encrypt:
        return (ord(letter) + amount)
    else:
        return (ord(letter) - amount)


def encrypt_decrypt(letter, amount, encrypt):

    shifted = shift_letter(letter, amount, encrypt)
    result = (shifted - 97) % 26

    return chr(result + 97)


def encrypt_string(string):
    result = ''
    numbers = []

    for letter in string:

        num = random.randint(1, 26)
        numbers.append(num)
        result += encrypt_decrypt(letter, num, True)
        
    return result, numbers

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




