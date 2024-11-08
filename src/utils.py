from os import system, name

def clear_term() -> None:
    system('cls' if name == 'nt' else 'clear')


