import os

def get_bash_history():
    history_file = os.path.expanduser("~/.bash_history")
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            lines = f.readlines()
            for line in lines[-20:]:
                print(line.strip())
    else:
        print("Le fichier .bash_history n'existe pas.")