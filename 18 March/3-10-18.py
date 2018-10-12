class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first.upper()} {self.last.upper()}'

    # @fullname.setter
    # def fullname(self, name):
    #     first, last = name.split(' ')
    #     self.first = first
    #     self.last = last


emp_1 = Employee('frank', 'young', 50000)
print(emp_1.email)
print(emp_1.fullname())
# print(vars(emp_1))

# emp_1.fullname = 'john doe'
# print(vars(emp_1))
