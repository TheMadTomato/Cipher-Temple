#==============================================================================#
#==============================================================================#
'''
This Library will contain the sub-menu for each cipher algorithm. 
Seperated from the main script in order to keep things clean and modular
'''
#=================================IMPORTS======================================#
#==============================================================================#
from ceasarlib import CaesarCipher
from pigcryptlib import PigCrypt
from columnartranspositionlib import ColumnarTranspositionCipher
from rsalib import RSACipher
from caesarattacklib import CaesarAttack
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style


#=============================INITSTYLE========================================#
#==============================================================================#
console = Console()
style = Style.from_dict({
    'prompt': 'bold #ffcc00',
})

#============================CAESAR MENU=======================================#
#==============================================================================#
def caesar_menu() -> None:
    cipher = CaesarCipher()
    while True:
        console.print("\n[bold cyan]Caesar Cipher Menu:[/bold cyan]")
        console.print("[1] Encrypt a message", style="bold green")
        console.print("[2] Decrypt a message", style="bold green")
        console.print("[3] Perform a Caesar Cipher Attack", style="bold yellow")
        console.print("[4] Show All Possible Decryptions (Brute Force)", style="bold yellow")
        console.print("[5] Go back to main menu", style="bold red")

        choice = prompt("Please choose an option: ", style=style).strip()

        if choice == '1':
            message = input("Enter Message to Encrypt: ")
            cipher.set_message(message)
            cipher.get_key_from_user()
            encrypted_message = cipher.caesar_encrypt()
            console.print(f"Encrypted Message: [bold green]{encrypted_message}[/bold green]")
        elif choice == '2':
            message = input("Enter Message to Decrypt: ")
            cipher.set_message(message)
            cipher.get_key_from_user()
            decrypted_message = cipher.caesar_decrypt()
            console.print(f"Decrypted Message: [bold green]{decrypted_message}[/bold green]")
        elif choice == '3':
            ciphertext = input("Enter Ciphertext to Attack: ")
            attack = CaesarAttack(ciphertext)
            probable_key, probable_plaintext = attack.brute_force_attack()
            console.print(f"Most Probable Key: [bold yellow]{probable_key}[/bold yellow]")
            console.print(f"Decrypted Text with Probable Key: [bold green]{probable_plaintext}[/bold green]")
        elif choice == '4':
            ciphertext = input("Enter Ciphertext to Analyze: ")
            attack = CaesarAttack(ciphertext)
            attack.show_all_possible_texts()
        elif choice == '5':
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")

#============================PIGCRYPT MENU=====================================#
#==============================================================================#
def pigcrypt_menu() -> None:
    cipher = PigCrypt()
    while True:
        console.print("\n[bold cyan]Pigcrypt Menu:[/bold cyan]")
        console.print("[1] Encrypt a message", style="bold green")
        console.print("[2] Decrypt a message", style="bold green")
        console.print("[3] Go back to main menu", style="bold red")
        
        choice = prompt("Please choose an option: ", style=style).strip()

        if choice == '1':
            message = input("Enter Message to Encrypt: ")
            cipher.set_message(message)
            encrypted_message = cipher.pigcrypt_encrypt()
            console.print(f"Encrypted Message: [bold green]{encrypted_message}[/bold green]")
        elif choice == '2':
            message = input("Enter Message to Decrypt: ")
            cipher.set_message(message)
            decrypted_message = cipher.pigcrypt_decrypt()
            console.print(f"Decrypted Message: [bold green]{decrypted_message}[/bold green]")
        elif choice == '3':
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")

#===================COLUMNAR TRANSPOSITION CIPHER MENU=========================#
#==============================================================================#
def columnartransposition_menu() -> None:
    cipher = ColumnarTranspositionCipher()
    while True:
        console.print("\n[bold cyan]Columnar Transposition Cipher Menu:[/bold cyan]")
        console.print("[1] Encrypt a message", style="bold green")
        console.print("[2] Decrypt a message", style="bold green")
        console.print("[3] Go back to main menu", style="bold red")
        
        choice = prompt("Please choose an option: ", style=style).strip()

        if choice == '1':
            message = input("Enter Message to Encrypt: ")
            key = input("Enter Key (unique alphabetic characters): ")
            cipher.set_message(message)
            cipher.set_key(key)
            encrypted_message = cipher.coltranspo_encrypt()
            console.print(f"Encrypted Message: [bold green]{encrypted_message}[/bold green]")
        elif choice == '2':
            message = input("Enter Ciphertext to Decrypt: ")
            key = input("Enter Key (unique alphabetic characters): ")
            cipher.set_message(message)
            cipher.set_key(key)
            decrypted_message = cipher.coltranspo_decrypt(message)
            console.print(f"Decrypted Message: [bold green]{decrypted_message}[/bold green]")
        elif choice == '3':
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")

#============================RSA MENU==========================================#
#==============================================================================#
def rsa_menu() -> None:
    cipher = RSACipher()
    while True:
        console.print("\n[bold cyan]RSA Cipher Menu:[/bold cyan]")
        console.print("[1] Encrypt a message", style="bold green")
        console.print("[2] Decrypt a message", style="bold green")
        console.print("[3] Display Public Key", style="bold yellow")
        console.print("[4] Go back to main menu", style="bold red")

        choice = prompt("Please choose an option: ", style=style).strip()

        if choice == '1':
            message = input("Enter Message to Encrypt: ")
            encrypted_message = cipher.encrypt(message)
            console.print(f"Encrypted Message: [bold green]{encrypted_message}[/bold green]")
        elif choice == '2':
            ciphertext = input("Enter Ciphertext to Decrypt (copy line by line to avoid errors): ")
            try:
                decrypted_message = cipher.decrypt(ciphertext)
                console.print(f"Decrypted Message: [bold green]{decrypted_message}[/bold green]")
            except Exception as e:
                console.print(f"Error during decryption: {e}", style="bold red")
        elif choice == '3':
            public_key = cipher.get_public_key()
            console.print(f"Public Key: [bold yellow]{public_key}[/bold yellow]")
        elif choice == '4':
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")
