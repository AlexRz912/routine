from jobs.models.routine_model import Routine
from jobs.models.command_list_model import CommandList
from utils.input_utils import clear_terminal

commands = CommandList()
commands.ask_for_commands()

routine = Routine(commands.command_list)

def add_routine():
    steps = [
        "ask_for_routine_name",
        "ask_for_routine_scenario",
        "create_routine",
        "json_add_new_routine"
    ]

    for step in steps:
        getattr(routine, step)()
        clear_terminal() if step != "json_add_new_routine" else None

add_routine()
