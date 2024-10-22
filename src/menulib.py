from ceasarlib import *

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

        elif choice == '2':
            C = input("Enter Message to Decrypt: ")
            K = get_caesar_key()
            DM = caesar_decrypt(C, K)
            print(f"Decrypted Message: {DM}")

        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")
