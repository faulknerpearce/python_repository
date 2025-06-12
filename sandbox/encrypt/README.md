# Simple String Encryption

This project provides a basic Python script for encrypting and decrypting lowercase alphabetic strings using a random shift cipher. Each letter in the string is shifted by a random amount, and the shift values are stored for decryption.

## Features

- Encrypts a string by shifting each letter by a random amount
- Decrypts a string using the list of shift values
- Simple functions for shifting, encrypting, and decrypting
- Example usage included in the main block

## Functions

`shift_letter(letter, amount, encrypt)`
- Shifts a letter by a given amount for encryption or decryption.

`encrypt_decrypt(letter, amount, encrypt)`
- Encrypts or decrypts a single letter using a shift amount.

`encrypt_string(string)`
- Encrypts a string, returning the encrypted string and the list of shift numbers.

`decrypt_string(string, numbers)`
- Decrypts a string using the provided list of shift numbers.

## Usage

1. Run the script:

2. The script will print the encrypted string, the shift numbers, and the decrypted result.

## Example Output

```
The encrypted string is: jvsjyd The encryption numbers are: [9, 1, 26, 16, 16, 16]
austin
```

## Notes

- Only lowercase alphabetic characters are supported.
- The encryption is not secure for real-world use; it is for educational and demonstration purposes only.

## License

This project is open source and available under the MIT License.
