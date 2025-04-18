import numpy as np
from datetime import datetime, date

class IntervalCalc:
    def __init__(self, date: str, force: float):
        self.interval = self.__set_interval(date)

        self.initial_force = 2.0
        self.force = force
        
        self.force_multiplier_success = 1.6
        self.force_multiplier_failure = 0.8

    def calc_retention_rate(self, success: bool) -> float:
        if success == None:
            return 0.5

        if success == False:
            self.__handle_failure_on_card()
            return max(0.1, np.exp(-self.interval/self.force))
            
        # True
        self.__handle_success_on_card()
        return  max(0.1, np.exp(-self.interval/self.force))

    def __set_interval(self, date) -> int:
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = self.__get_today_date()
        return (today - converted_date).days

    def __get_today_date(self):
        return date.today()

    def __handle_success_on_card(self):
        if self.force == None:
            self.force = self.initial_force * self.force_multiplier_success
        else:
            self.force *= self.force_multiplier_success

    def __handle_failure_on_card(self):
        if self.force == None:
            self.force = self.initial_force * self.force_multiplier_failure
        else:
            self.force *= self.force_multiplier_failure
