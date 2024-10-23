from ceasarlib import *
from menulib import *
from pyfiglet import Figlet

def main_menu():
    figlet = Figlet(font='bloody')  # ansi_regular
    cipher_temple_title = figlet.renderText('Cipher Temple')
    while True:
        print(cipher_temple_title)
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

