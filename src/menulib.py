'''
This Library will contain the sub-menu for each cipher algorithm. Sepearated from the main script in order keep things clean and modular
'''
from ceasarlib import *
from pigcryptlib import *
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

console = Console()
style = Style.from_dict({
    'prompt': 'bold #ffcc00',
})

def caesar_menu() -> None:
    while True:
        console.print("\n[bold cyan]Caesar Cipher Menu:[/bold cyan]")
        console.print("[1] Encrypt a message", style="bold green")
        console.print("[2] Decrypt a message", style="bold green")
        console.print("[3] Go back to main menu", style="bold red")
        
        choice = prompt("Please choose an option: ", style=style).strip()

        if choice == '1':
            M = input("Enter Message to Encrypt: ")
            K = get_caesar_key()
            C = caesar_encrypt(M, K)
            console.print(f"Encrypted Message: [bold green]{C}[/bold green]")
        elif choice == '2':
            C = input("Enter Message to Decrypt: ")
            K = get_caesar_key()
            DM = caesar_decrypt(C, K)
            console.print(f"Decrypted Message: [bold green]{DM}[/bold green]")
        elif choice == '3':
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")

def pigcrypt_menu() -> None:
    while True:
        console.print("\n[bold cyan]Pigcrypt Menu:[/bold cyan]")
        console.print("[1] Encrypt a message", style="bold green")
        console.print("[2] Decrypt a message", style="bold green")
        console.print("[3] Go back to main menu", style="bold red")
        
        choice = prompt("Please choose an option: ", style=style).strip()

        if choice == '1':
            M = input("Enter Message to Encrypt: ").upper()
            C = pigcrypt_encrypt(M)
            console.print(f"Encrypted Message: [bold green]{C}[/bold green]")
        elif choice == '2':
            C = input("Enter Message to Decrypt: ").upper()
            DM = pigcrypt_decrypt(C)
            console.print(f"Decrypted Message: [bold green]{DM}[/bold green]")
        elif choice == '3':
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")

