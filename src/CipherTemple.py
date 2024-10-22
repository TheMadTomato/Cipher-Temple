from ceasarlib import *

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Caesar Cipher")
        print("2. Exit")
        
        choice = input("Please choose an option: ")

        if choice == '1':
            caesar_menu()
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

