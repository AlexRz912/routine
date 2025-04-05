from .routine_model import Routine
from .routines_queue import RoutinesQueue

from models.command_list_model import CommandList

from utils.file_system_utils import get_routine_location
from utils.input_utils import clear_terminal

import os

class RoutineController():
    def __init__(self, action, name=None):
        """ 
        Controller dispatches to the right functions based on action 
        """
        self.process_action(action, name)

    def process_action(self, act, name=None):
        if act == "add":
            self.command_list = CommandList()
            self.command_list.ask_for_commands()
            self.routine = Routine(self.command_list.command_list)
            self.__add_routine()

        else:
            routine_object = Routine()

            env_var = get_routine_location()

            self.routines = routine_object.json_load_routines(f"{env_var}/routines.json")

            for i, v in self.routines.items():
                print(f"name : {i}")
                print(f"description : {v['scenario']}\n")

            
            self.all_routines = RoutinesQueue(self.routines)
            self.__play_routine()

    def __add_routine(self):
        steps = [
            "ask_for_routine_name",
            "ask_for_routine_scenario",
            "create_routine",
            "json_add_new_routine"
        ]

        for step in steps:
            getattr(self.routine, step)()
            clear_terminal() if step != "json_add_new_routine" else None

    def __play_routine(self):
        # to externalise into routine view
        answer = input("choose a routine to play\n\n")
        clear_terminal()
        print(f"Name: {answer}")
        print(self.all_routines.routine_list[answer]["scenario"])
        input("\nPress any key to start playing :\n")

        self.__input_a_command(
            self.all_routines.routine_list[answer]["scenario"], 
            self.all_routines.routine_list[answer]["command_list"]
        )

    def __input_a_command(self, scenario, command_list):
        clear_terminal()
        while True:
            print(scenario)
            print("\n")
            command = input("q to quit :\n\n")
            clear_terminal()
            if command == "q":
                print("Here is a cheatsheet for this problem !:\n\n")
                for i in command_list:
                    print(i)
                print()
                success = input("Did you successfully solved the described problem? (Y/n)\n").lower()
                if success == "y":
                    print("congrats")
                else:
                    print("sad :'")
                break
            print()
            os.system(command)
            print()
            print()
