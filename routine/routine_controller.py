from .routine_model import Routine
from .routines_queue import RoutinesQueue

from .views.single_routine_view import SingleRoutine
from .command_list_model import CommandList

from spaced_reps.interval_calc import IntervalCalc

from utils.file_system_utils import get_cards_location
from utils.input_utils import clear_terminal

import os

class RoutineController():
    def __init__(self, action, name=None):
        """ 
        Controller dispatches to the right functions based on action 
        """
        self.process_action(action, name)

    def process_action(self, act, name=None):


        # let's say if/elif are functions in and of themselves
        # who the fuck said process action was a gigantic piece of code smell??? yea right ;)

        filename = f"{get_cards_location()}/routines.json"


        # add routine
        if act == "add":

            self.command_list = CommandList()
            self.command_list.ask_for_commands()

            self.routine = Routine(self.command_list.command_list)

            
            self.__add_routine(filename)
        
        

        # play a routine
        elif act == "play":

            self.routine = Routine()
            self.routines = self.routine.json_load_routines(filename)

            for i, v in self.routines.items():
                print(f"name : {i}")
                print(f"description : {v['scenario']}\n")

            self.all_routines = RoutinesQueue(self.routines)
            self.__play_routine()


        ## update retention rate of routines
        elif act == "update_retention_rate":
            self.routine = Routine()
            
            self.routines = self.routine.json_load_routines(filename)
            self.__daily_retention_rate_update(filename)


        elif act == "play_all_routines":

            self.routine = Routine()
            self.all_routines = self.routine.json_load_routines(filename)
            todays_routine = self.routine.json_load_routines(filename)

            for i, routine in self.all_routines.items():
                if routine["retention_rate"] > 0.5:
                    todays_routine.pop(i, None)

            self.routines_queue = RoutinesQueue(todays_routine)
            self.routines_queue.play_todays_routine()

            for i, routine in self.all_routines.items():
                if i in todays_routine:
                    self.all_routines[i] = todays_routine[i]
            self.routine.update_routine(self.all_routines, filename)


    def __add_routine(self, filename):
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

        #self.__input_a_command(
        #    self.all_routines.routine_list[answer]["scenario"], 
        #    self.all_routines.routine_list[answer]["command_list"]
        #)
        self.view = SingleRoutine()
        self.view.input_commands(
            self.all_routines.routine_list[answer]["scenario"], 
            self.all_routines.routine_list[answer]["command_list"]
        )

    def __daily_retention_rate_update(self, filename):
        
        for key, routine in self.routines.items():
            if routine["last_revision_date"] == None:
                calc = IntervalCalc(
                    routine["creation_date"], 
                    routine["force"]
                )
            else:
                calc = IntervalCalc(
                    routine["last_revision_date"],
                    routine["force"]
                )
            routine["retention_rate"] = calc.calc_retention_rate(routine["success"])
            
        self.routine.json_update_routine_retention_rate(self.routines, filename)