from spaced_reps.interval_calc import IntervalCalc
from utils.input_utils import clear_terminal
from .view_utils import view_utils

from datetime import date
import time


class MultipleRoutine():
    def input_commands(self, routine):
        clear_terminal()
        while True:
            routine_updated_or_bool, quitting = self.play_routine(routine)
            if isinstance(routine_updated_or_bool, dict) or quitting == True:
                return routine, quitting

    def play_routine(self, routine):
        view_utils.prompt_scenario(routine["scenario"])
        command = self.get_choice_and_clear_terminal()
        if self.check_quitting(command):
            return None, True

        status = self.check_next(command, routine["command_list"])
        if status:
            return self.update_interval_on_success(status, routine), False
        view_utils.execute_command(command)
        return None, False

    def get_choice_and_clear_terminal(self):
        command = input("n to get to next routine, q to quit all routine:\n\n")
        clear_terminal()
        return command
        
    def check_quitting(self, command):
        if command.lower() == "q":
            return True

    def check_next(self, command, command_list):
        if command == "n":
            print("Here is a cheatsheet for this problem !:\n\n")
            view_utils.prompt_command_list(command_list)
            success = input("Did you successfully solved the described problem ? (Y/n) (press any other key for next routine\n").lower()
            if not success:
                return True
            return success
        return None

    def update_interval_on_success(self, status, routine):
        calc = IntervalCalc(str(date.today()), routine["force"])
        routine["last_revision_date"] = str(date.today())
        if status == "y":
            print("congrats")
            time.sleep(1)
            routine["success"] = True
            routine["retention_rate"] = calc.calc_retention_rate(routine["success"])
            routine["force"] = calc.force
            return routine
        elif status == "n":
            print("sad :'")
            time.sleep(1)
            routine["success"] = False
            routine["retention_rate"] = calc.calc_retention_rate(routine["success"])
            routine["force"] = calc.force
            return routine
        else:
            return routine
        
            
