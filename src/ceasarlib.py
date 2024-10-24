'''
Ceasar Cipher contains 3 functions one for encryption one for decryption and one to accept both integers and strings as input, by converting strigns input into their length.
also the key input is masked
'''
from getpass import getpass


def caesar_encrypt(plaintext, key):
    # For each alphabetical character, skip spaces and numbers, shift the ascii decimal value then append it to a list. Following the content of the list is concatenated with no spaces and returned
    result = []
    for char in plaintext:
        if char.isalpha():
            # If you want the output to be in lower case, change upper() to lower, and both 65s to 97s
            shift = (ord(char.upper()) - 65 + key) % 26 + 65
            result.append(chr(shift))
    return ''.join(result)

def caesar_decrypt(ciphertext, key):
    # Same as encrypt method but instead of "+ key" we use "-key"
    result = []
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 - key) % 26 + 65
            result.append(chr(shift))
    return ''.join(result)

def get_caesar_key():
    # getpass module allow the input to be hidden within the active session.
    input_key = getpass("Enter your password: ")
    # Usage of try-except statment is better for this case because it is handeling dynamic input. and if statment wht the type() function is not pythonic and only good for static input
    try:
        return int(input_key)
    except ValueError:
        return len(input_key)

