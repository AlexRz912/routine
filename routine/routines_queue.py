from helpers.quit_helpers import no_routine_left_quit
from helpers.quit_helpers import user_quits

from spaced_reps.interval_calc import IntervalCalc
from .views.multiple_routine_view import MultipleRoutine

class RoutinesQueue:
    def __init__(self, routine_list):
        self.routine = None
        self.routine_list = routine_list
        
    def play_todays_routine(self):
        for i, routine in self.routine_list.items():
            self.routine = routine
            routine_view = MultipleRoutine()
            routine, quitting = routine_view.input_commands(routine)

            self.__check_quitting(routine, quitting)
            self.__update_routine_list(routine)
            
    def __check_quitting(self, routine, quitting):
        no_routine_left_quit(routine)
        user_quits(quitting)

    def __update_routine_list(routine):
        self.routine_list[i] = routine
