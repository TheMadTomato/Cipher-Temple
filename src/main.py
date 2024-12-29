#==============================================================================#
#==============================================================================#
'''
#==============================================================================#
The Main Menu Application it will only contain the main menu linking to further
sub-menus. Right now there is no fancy UI, just an attempt at a cool menu look
using pyfiglet and others.
#==============================================================================#
Developers:
----------------------------
Paul Estephan       12220605
Peter Chalhoub      12220336
Raymond Haddad      12050174
Matieu Abou Jawde   12210606
----------------------------
Version 2.0.0
----------------------------
'''
#=================================IMPORTS======================================#
#==============================================================================#
from menulib import caesar_menu, pigcrypt_menu, columnartransposition_menu, rsa_menu
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from utils import clear_term

#=============================INITSTYLE========================================#
#==============================================================================#
console = Console()
style = Style.from_dict({
    'prompt': 'bold #ffcc00',
})

#==============================MAINMENUDISPLAY=================================#
#==============================================================================#
def main_menu() -> None:
    figlet = Figlet(font='slant')
    cipher_temple_title = figlet.renderText('Cipher Temple')
    
    while True:
        clear_term()
        console.print(Panel(cipher_temple_title, style="bold cyan"))
        
        console.print("[1] Caesar Cipher", style="bold green")
        console.print("[2] Pigcrypt Cipher", style="bold green")
        console.print("[3] Columnar Transposition Cipher", style="bold green")
        console.print("[4] RSA Cipher", style="bold green")
        console.print("[5] Perform Caesar Cipher Attack", style="bold yellow")
        console.print("[6] Exit", style="bold red")
        
        choice = prompt("Please choose an option: ", style=style).strip()
        
        if choice == '1':
            caesar_menu()
        elif choice == '2':
            pigcrypt_menu()
        elif choice == '3':
            columnartransposition_menu()
        elif choice == '4':
            rsa_menu()
        elif choice == '5':
            console.print("Performing Caesar Cipher Attack...", style="bold yellow")
            caesar_menu()  # Includes attack as an option
        elif choice == '6':
            console.print("Exiting the program. Goodbye!", style="bold red")
            clear_term()
            break
        else:
            console.print("Invalid choice, please try again.", style="bold red")

#==================================MAIN========================================#
#==============================================================================#
if __name__ == "__main__":
    main_menu()
