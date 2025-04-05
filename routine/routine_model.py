import json
import os
from logs import logs
from parsers.json_parsers import jsonParsers

class Routine():
    """ """
    def __init__(self, command_list=None) -> None:
        self.command_list = command_list 
        self.json_parser = jsonParsers()

    def ask_for_routine_name(self) -> None:
        print("Provide a name for this routine :\n")
        self.routine_name = input()

    def ask_for_routine_scenario(self) -> None:
        print("Provide a scenario for this routine :\n")
        self.routine_scenario = input()

    def create_routine(self) -> None:
        self.new_routine = {
            "scenario": self.routine_scenario,
            "command_list": self.command_list
        }

    def json_add_new_routine(self) -> None:
        env_var = os.getenv("ROUTINE")
        filename = f"{env_var}/routines.json"

        content = self.json_load_routines(filename)
        content[self.routine_name] = self.new_routine

        self.json_parser.parse(filename,"w", content)
        
    def json_load_routines(self, filename) -> dict:
        return self.json_parser.parse(filename, "r", None) 

    
