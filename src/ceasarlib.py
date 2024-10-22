from getpass import getpass
import os

def caesar_encrypt(plaintext, key):
    result = []
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 + key) % 26 + 65
            result.append(chr(shift))
    return ''.join(result)

def caesar_decrypt(ciphertext, key):
    result = []
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 - key) % 26 + 65
            result.append(chr(shift))
    return ''.join(result)

def get_caesar_key():
    input_key = getpass("Enter your password: ")
    try:
        return int(input_key)
    except ValueError:
        return len(input_key)

