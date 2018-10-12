from datetime import date
import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first.upper()} {self.last.upper()}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True

    def __repr__(self):
        # return f"{self.__class__.__name__}('{self.first}','{self.last}',{self.pay})"
        return "{}{} ".format(self.__class__.__name__, tuple(vars(self).values()))
        # return f"{self.__class__.__name__}({self._param})"


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, emps=None):
        super().__init__(first, last, pay)
        if emps == None:
            self.emps = []
        else:
            self.emps = emps

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def print(self):
        for emp in self.emps:
            print(emp)


deve_1 = Developer('frank', 'young', 50000, 'Python')
print(deve_1)
