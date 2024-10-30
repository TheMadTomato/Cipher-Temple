'''
This Library will contain the sub-menu for each cipher algorithm. Sepearated from the main script in order keep things clean and modular
'''
from ceasarlib import *
from pigcryptlib import * 

def caesar_menu() -> None:
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

        elif choice == '2':
            C = input("Enter Message to Decrypt: ")
            K = get_caesar_key()
            DM = caesar_decrypt(C, K)
            print(f"Decrypted Message: {DM}")

        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")

def pigcrypt_menu() -> None:
    while True:
        print("\nPigcrypt Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Go back to main menu")
        
        choice = input("Please choose an option: ")

        if choice == '1':
            M = input("Enter Message to Encrypt: ").upper()
            C = pigcrypt_encrypt(M)
            print(f"Encrypted Message: {C}") 

        elif choice == '2':
            C = input("Enter Message to Decrypt: ").upper()
            DM = pigcrypt_decrypt(C)
            print(f"Decrypted Message: {DM}")

        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")
