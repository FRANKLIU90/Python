import requests


class Employee:
    raise_amt = 1.04
    # print('hello')

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        # print('ji')

    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first.upper()} {self.last.upper()}'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, string):
        return cls(*string.split('-'))

    def __repr__(self):
        return f'{self.__class__.__name__}{tuple(vars(self).values())}'

    def look_up(self, month):
        web = requests.get(f'http://company.com/{self.last}/{month}')
        if web.ok:
            return web.text
        return 'bad love'

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError('hell with it')
        return a / b


emp_1 = Employee.from_str('frank-young-50000')
# print(emp_1.fullname)
# print(emp_1)
# print(Employee.add(4, 6))
# Employee.set_raise_amt(1.10)
# Employee.divide(10, 0)
# print(Employee('hello', 'there', 60000)  Employee('hello', 'there', 60000))

# emp_a = Employee.from_str('hello-there-60000')
# print(emp_a)
# a, b, c = 'hello-there-60000'.split('-')
# print(Employee.raise_amt)
