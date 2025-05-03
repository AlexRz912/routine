import subprocess
import os

def check_shell():
    result = subprocess.run("echo $SHELL", shell=True, capture_output=True, text=True)
    shell_path = result.stdout.strip()
    return shell_path

def get_bash_history():
    history_file = os.path.expanduser("~/.bash_history")
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            lines = f.readlines()
            for line in lines[-20:]:
                print(line.strip())
    else:
        print("Le fichier .bash_history n'existe pas.")