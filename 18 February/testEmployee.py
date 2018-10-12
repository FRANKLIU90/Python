class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{.first}.{.last}@gmail.com'.format(self, self)

    @property
    def fullname(self):
        return f'{self.first.upper()} {self.last.upper()}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)


# emp_1 = Employee('lou', 'reed', 60000)
# print(emp_1.fullname)
# emp_1.fullname = 'john lennon'
# print(emp_1.fullname)

# print(emp_1)
