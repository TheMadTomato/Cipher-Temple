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

def caesar_menu():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Go back to main menu")
        
        choice = input("Please choose an option: ")

        if choice == '1':
            M = input("Enter Message to Encrypt: ")
            K = get_caesar_key()
            C = caesar_encrypt(M, K)
            print(f"Encrypted Message: {C}") 
            print("The encrypted message has been copied to the clipboard.")

        elif choice == '2':
            C = input("Enter Message to Decrypt: ")
            K = get_caesar_key()
            DM = caesar_decrypt(C, K)
            print(f"Decrypted Message: {DM}")
            print("The decrypted message has been copied to the clipboard.")

        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")
