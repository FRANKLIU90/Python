from datetime import date
import datetime
from functools import partial
# import datetime
# import time

# print(issubclass(datetime, time))


class Employee:
    raise_amount = 1.04
    version = '.1'

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)

    # def fullname(self):
    #     return f'{self.first.upper()} {self.last.upper()}'

    @property
    def fullname(self):
        return f'{self.first.upper()} {self.last.upper()}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        del self

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        #************for subclass usage ,string contains classname ex:'Developer-john-cale-60000-Java'
        cls_name, *args = emp_str.split('-')
        return cls(*args)
        # args = tuple(args)
        # print(cls)
        # print(args)
        # return cls(args)
        # return partial(cls, args)

    @staticmethod
    def is_workday(date):
        if not isinstance(date, datetime.date):
            return "date must be time type"
        elif date.weekday() == 5 or date.weekday() == 6:
            return False
        return True

    def __repr__(self):
        # return f"{self.__class__.__name__}('{self.first}','{self.last}',{self.pay})"
        #****************************************for subclass
        return "{}{} ".format(self.__class__.__name__, tuple(vars(self).values()))
        # return f"{self.__class__.__name__}({self._param})"


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, emps=None):
        super().__init__(first, last, pay)
        if emps:
            self.emps = emps
        else:
            self.emps = []

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def print(self):
        for emp in self.emps:
            print(emp)


deve_1 = Developer('frank', 'young', 50000, 'Python')
print(deve_1)
string_2 = 'Developer-john-abear-60000-Jave'
deve_2 = Developer.from_str(string_2)
print(deve_2)
# date = date.today()
print(Employee.is_workday('2'))

print(deve_2.fullname)

deve_2.fullname = 'Test User'
print(deve_2.email)

# del deve_2
# print(deve_2)
