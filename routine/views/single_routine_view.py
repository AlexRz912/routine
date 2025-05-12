from utils.input_utils import clear_terminal
from .view_utils import view_utils
import os

class SingleRoutine():
    def input_commands(self, scenario, command_list):
        clear_terminal()
        while True:
            self.play_routine(scenario, command_list)

    def play_routine(self, scenario, command_list):
        view_utils.prompt_scenario(scenario)
        command = self.get_command_and_clear_terminal()
        if self.quit_on_action(command, command_list):
            quit()
        view_utils.execute_command(command)

    def get_command_and_clear_terminal(self):
        command = input("q to quit :\n\n")
        clear_terminal()
        return command

    def quit_on_action(self, command, command_list):
        if command == "q":
            print("Here is a cheatsheet for this problem !:\n\n")
            view_utils.prompt_command_list(command_list)
            success = input("Did you successfully solved the described problem? (Y/n)\n").lower()
            self.prompt_success_status_message(success)
            return True
        return False

    def prompt_success_status_message(self, success):
        if success == "y":
            print("congrats")
        else:
            print("sad :'")
        quit()