import json

from logs import logs
from json_parser import json_parser

class Routine():
    """ """
    def __init__(self, command_list) -> None:
        self.command_list = command_list 

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
        filename = "./jobs/routines.json"

        content = self.json_load_routines()
        content[self.routine_name] = self.new_routine

        json_parser.parse(filename,"w", content)
        
    def json_load_routines(self) -> dict: 
        filename = "./jobs/routines.json"
        return json_parser.parse(filename, "r", None)    