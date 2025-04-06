import numpy as np
from datetime import datetime, date

class IntervalCalc:
    def __init__(self, date: str, force: float=None):
        self.interval = self.__set_interval(date)

        self.initial_force = 2.0
        self.force = force
        
        self.force_multiplier_success = 1.6
        self.force_multiplier_failure = 0.5

        self.critical_threshold = 0.5

    def calc_retention_rate(self, success: bool =False) -> float:
        if success == False:
            self.__handle_failure_on_card()
            return np.exp(-self.interval/self.force)

        self.__handle_success_on_card()
        return  np.exp(-self.interval/self.force)

    def __set_interval(self, date):
        print(date)
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()
        print(converted_date)
        today = self.__get_today_date()
        return (today - converted_date).days

    def __get_today_date(self):
        return date.today()

    def __handle_success_on_card(self):
        force = self.__handle_new_card()
        force *= self.force_multiplier_success
        print(force)
        self.force = force

    def __handle_failure_on_card(self):
        force = self.__handle_new_card()
        force *= self.force_multiplier_failure
        print(force)
        self.force = force

    def __handle_new_card(self):
        if self.force == None:
            print("donc self force devient self.initial_force")
            return self.initial_force
        else:
            return self.force
