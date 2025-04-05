import re

def prompt_clean_zsh_history_output(file):
    history_data = file.read().decode("latin-1")
    history_lines = history_data.split("\n")
    
    clean_lines = [re.sub(r"^.*?;", "", line) for line in history_lines]
    print("\n".join(clean_lines[-20:]).strip())