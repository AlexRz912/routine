import os

def get_routine_location():
    return os.getenv("ROUTINE")

def get_zsh_history_file():
    return os.path.expanduser("~/.zsh_history")