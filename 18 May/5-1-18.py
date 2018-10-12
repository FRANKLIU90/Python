class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'

    def fullname(self):
        return f'{self.first.upper()} {self.last.upper()}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('frank', 'young', 50000)
print(emp_1.fullname())
print(emp_1.pay)
# emp_1.apply_raise()
Employee.apply_raise(emp_1)
print(emp_1.pay)
print(vars(emp_1))
