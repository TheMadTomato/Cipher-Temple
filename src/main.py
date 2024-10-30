'''
###########################################################################################
The Main Menu Application it will only  contain the main menu linking to further sub-menus
Right now there is no fancy UI just an attempt of a cool menu look using pyfiglet
###########################################################################################
Developers:
----------------------------
Paul Estephan       12220605
Peter Chalhoub      12220336
Raymond Haddad      12050174
Matieu Abou Jawde   12210606
----------------------------
Version 1.1.0-Beta
----------------------------
'''
from menulib import *
from pyfiglet import Figlet
from utils import clear_term

def main_menu() -> None:
    figlet = Figlet(font='bloody')  # ansi_regular
    cipher_temple_title = figlet.renderText('Cipher Temple')
    while True:
        clear_term()
        print(cipher_temple_title)
        print("1. Caesar Cipher")
        print("2. Pigcrypt Cipher")
        print("3. Exit")
        
        choice = input("Please choose an option: ")

        if choice == '1':
            caesar_menu()
        elif choice == '2':
            pigcrypt_menu()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            clear_term()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

