from spaced_reps.interval_calc import IntervalCalc
from utils.input_utils import clear_terminal
from datetime import date
import os
import time

class RoutinesQueue:
    def __init__(self, routine_list):
        self.routine = None
        self.routine_list = routine_list
        
    def play_todays_routine(self):
        for i, routine in self.routine_list.items():
            self.routine = routine
            routine = self.__input_a_command(routine)
            self.routine_list[i] = self.routine
            if routine == False:
                break

        
    def __input_a_command(self, routine):
        clear_terminal()
        while True:
            print(routine["scenario"])
            print("\n")
            command = input("n to get to next routine, q to quit all routine:\n\n")
            clear_terminal()
            if command == "q":
                return False
            if command == "n":
                print("Here is a cheatsheet for this problem !:\n\n")
                for i in routine["command_list"]:
                    print(i)
                print()
                success = input("Did you successfully solved the described problem ? (Y/n) (press any other key for next routine)\n").lower()

                calc = IntervalCalc(str(date.today()), routine["force"])
                routine["last_revision_date"] = str(date.today())

                if success == "y":
                    print("congrats")
                    routine["success"] = True
                    routine["retention_rate"] = calc.calc_retention_rate(routine["success"])
                    routine["force"] = calc.force
                    return routine
                elif success == "n":
                    print("sad :'")
                    routine["success"] = False
                    routine["retention_rate"] = calc.calc_retention_rate(routine["success"])
                    routine["force"] = calc.force
                    return routine
                else:
                    break
            print()
            os.system(command)
            print()
            print()