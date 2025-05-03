import os
import re


from utils.file_system_utils import get_zsh_history_file
from utils.terminal_utils import check_shell
from utils.terminal_utils import get_bash_history
from parsers.json_parsers import jsonParsers

class CommandList:
    """  """
    def __init__(self):
        self.command_list = []
        self.__prompt_history()

    def __prompt_history(self):
        if (check_shell() == "/bin/zsh"):
            history_file = get_zsh_history_file()
            json_parser = jsonParsers()
            json_parser.parse_binary(history_file, "shell")
        elif (check_shell() == "/bin/bash"):
            history_file = get_bash_history()
        
    def ask_for_commands(self):
        commands = input("provide a comma separated list for commands to add to the routine :\n")
        self.__add_provided_commands(commands)

    def __add_provided_commands(self, commands):
        commands_list = commands.split(",")
        for command in commands_list:
            clean_command = command.strip()
            if clean_command:
                self.__add_command_to_list(clean_command)
    
    def __add_command_to_list(self, command):
        self.command_list.append(command)