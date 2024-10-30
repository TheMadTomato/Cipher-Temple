from os import system, name

def clear_term():
    system('cls' if name == 'nt' else 'clear')


