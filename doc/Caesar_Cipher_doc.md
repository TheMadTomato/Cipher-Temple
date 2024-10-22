# Ceasar Cipher 

The Caesar Cipher is a **Classical**, **Mono-Alphabetical**, **Substitution** cipher that was created by Julius Caesar himself around 58-50 BCE. It works by shifting each letter in the message by a fixed number of positions in the alphabet. The number of positions to shift is determined by the key.

Here is the explanation of each function in the `caesarlib` library:

### Caesar Encrypt Function
```python
def caesar_encrypt(plaintext, key):
    result = []
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 + key) % 26 + 65
            result.append(chr(shift))
    return ''.join(result)
```

This function takes two arguments: `plaintext` or `M` (the message to encrypt) and `key` or `K` (the number of positions to shift). 

- The function loops through each character in the `plaintext`. If the character is an alphabetic letter (`char.isalpha()`), it is converted to its corresponding uppercase ASCII value using `ord(char.upper())`.
- The value is then shifted by the key using the formula `(ord(char.upper()) - 65 + key) % 26 + 65`. This shifts the letter while ensuring it wraps around within the alphabet's 26-letter range.
- The result is stored in a list (`result.append(chr(shift))`), and finally, the encrypted message is returned as a single concatenated string (`''.join(result)`).
  
Note: The function only deals with alphabetic characters. Non-alphabetic characters are ignored, and all output is returned in uppercase and space-free.

### Caesar Decrypt Function
```python 
def caesar_decrypt(ciphertext, key):
    result = []
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 - key) % 26 + 65
            result.append(chr(shift))
    return ''.join(result)
```

The `caesar_decrypt` function operates the same way as the encryption function but decrements the key to reverse the transformation, decrypting the ciphertext back into plaintext.

### Get Caesar Key Function

```python
def get_caesar_key():
    input_key = getpass("Enter your password: ")
    try:
        return int(input_key)
    except ValueError:
        return len(input_key)
```

This function is used to obtain the encryption/decryption in a secure and masked way.

- It prompts the user to enter a key using `getpass()` for privacy. The user is expected to input a number or a password.
- The function first attempts to convert the input into an integer (`int(input_key)`).
- If the input is not a valid number (raises `ValueError`), it falls back to returning the length of the input string (`len(input_key)`), effectively using the password length as the key.

