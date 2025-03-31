import re
import os

def clear_terminal():
    """ pure util as they come lol """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_history():
    history_file = os.path.expanduser("~/.zsh_history")
    try:
        with open(history_file, "rb") as f:
            history_data = f.read().decode("latin-1")
            history_lines = history_data.split("\n")
            # Supprimer tout avant et y compris le premier `;`
            clean_lines = [re.sub(r"^.*?;", "", line) for line in history_lines]
            return "\n".join(clean_lines[-20:]).strip()
    except FileNotFoundError:
        return "Fichier .zsh_history non trouvé."
    except Exception as e:
        return f"Erreur : {e}"
