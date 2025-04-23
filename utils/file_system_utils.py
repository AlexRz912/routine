import os

def get_routine_location():
    return os.getenv("ROUTINE")

def get_cards_location():
    return os.getenv("CARDS")
    
def get_zsh_history_file():
    return os.path.expanduser("~/.zsh_history")