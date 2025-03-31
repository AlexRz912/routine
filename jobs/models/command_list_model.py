import os
import re

class CommandList:
    """  """
    def __init__(self):
        self.command_list = []
        self.__get_history()

    def __get_history(self):
        history_file = os.path.expanduser("~/.zsh_history")

        try:
            with open(history_file, "rb") as f:
                history_data = f.read().decode("latin-1")
                history_lines = history_data.split("\n")
                clean_lines = [re.sub(r"^.*?;", "", line) for line in history_lines]
                print("\n".join(clean_lines[-20:]).strip())
                print()
        except FileNotFoundError:
            return "Fichier .zsh_history non trouvé."
        except Exception as e:
            return f"Erreur : {e}"

    def ask_for_commands(self):
        print("provide a comma separated list for commands to add to the routine :\n")
        commands = input()
        self.__add_provided_commands(commands)

    def __add_provided_commands(self, commands):
        commands_list = commands.split(",")
        for command in commands_list:
            clean_command = command.strip()
            if clean_command:
                self.__add_command_to_list(clean_command)
    
    def __add_command_to_list(self, command):
        self.command_list.append(command)