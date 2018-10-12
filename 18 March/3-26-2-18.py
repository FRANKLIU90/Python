# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         # self.fullname = f'{first.upper()} {last.upper()}'
#         self.email = f'{first}.{last}@gmail.com'

#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'

#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last


# emp_1 = Employee('frank', 'young', 50000)
# print(emp_1.fullname)
# emp_1.fullname = 'john doe'
# print(emp_1.fullname)
# import math


# class Circle:
#     ''' we are doing circles'''
#     version = '0.1'

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (self.radius**2) * math.pi
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):

        self.first = first
        self.last = last


emp_1 = Employee('frank', 'young')
print(emp_1.fullname)
emp_1.fullname = 'frank', 'yong '
