from .routine_model import Routine
from .routines_queue import RoutinesQueue

from ..models.command_list_model import CommandList
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
            # create a routine object
            routine_object = Routine()

            # to externalise in a utility function
            env_var = os.getenv("ROUTINE")


            # json loads to externalise in a json parser class
            self.routines = routine_object.json_load_routines(f"{env_var}/jobs/routines.json")


            # to externalise in routine_views, list function
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
        input("\nPress any key to start:\n")

        return

