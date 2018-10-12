# from datetime import datetime
# from functools import partial
# import itertools
# print(itertools.__doc__)

# def count(x, *, z=0):
#     result = 0
#     for n in x:
#         if n == z:
#             result += 1
#         return result


# m = partial(count, z='r')
# print(m('rez'))


# class Employee:
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f'{first}.{last}@gmail.com'

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_str(cls, string):
#         first, last, pay = string.split('-')
#         return cls(first, last, pay)

#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.isoweekday() == 7:
#             return False
#         return True


# emp_1 = Employee('frank', 'young', 50000)
# Employee.set_raise_amt(1.10)
# emp_1.apply_raise()
# # print(emp_1.pay)
# es = 'eddie-jones-60000'
# emp_2 = Employee.from_str(es)
# print(emp_2.pay)

# day = datetime(2018, 3, 11)
# print(day.weekday())
# # print(Employee.is_workday(day))


# def append(number, number_list=[]):
#     number_list.append(number)
#     print(number_list)
#     return number_list


# def append_1(number):
#     number_list = []
#     number_list.append(number)
#     print(number_list)
#     return number_list


# append(1)
# append(2)
# append_1(1)
# append_1(2)
# print(1.__add__(2))

# print(int.__add__(1, 2))
# a = 'Developer-john-cale-60000-Java'
# print(a.split('-'))


# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = int(pay)

#     @classmethod
#     def from_str(cls, string):

#         return cls(*string.split('-'))

#     def __repr__(self):
#         return f'{self.__class__.__name__}{tuple(self.__dict__.values())}'


# string = 'john-cale-60000'

# m = Employee.from_str(string)
# print(m)
# names = ['raymond', 'rachel', 'matthew']
# colors = ['red', 'green', 'blue', 'yellow']
# # names += colors
# # for x in names:
# #     print(x)
# a = zip(names, colors)
# # print(next(a))
# # print(list(zip(names, colors)))
# print(iter(a)is iter(a))
# colors = ['rez', 'greren', 'rurrd', 'yelrrrrlow']
# from operator import itemgetter
# from operator import methodcaller
# print(sorted(colors, key=itemgetter(0, 2)))


# print(sorted(colors, key=methodcaller('find', 'r')))


# names = ['raymond', 'rachel', 'matthew']
# colors = ['red', 'green', 'blue', 'yellow']
# dic = dict(zip(names, colors))
# print(list(dic))

# from collections import defaultdict
# result = defaultdict(int)
# for x in names:
#     result[x] += 1
# print(result)
# print(result.items())


# def make_func():
#     for i in range(5):
#         yield lambda x: x * i


# def make_func():
#     return (lambda x: i * x for i in range(5))


# def make_func():
#     return [lambda x: i * x for i in range(5)]


# for func in make_func():
#     result = func(2)
#     print(result)

# for func in list(make_func()):
#     result = func(2)
#     print(result)

# def ft(message):
#     mes = message
#     i = 0

#     def Jo():
#         print(mes, i)
#     yield Jo
#     mes = message.upper()

#     i = 1

#     def Jo():
#         print(mes, i)
#     yield Jo


# x = ft('hello')
# x = [x for x in x]

# y = ft('football')
# for func in x:
#     func()
# for func in y:
#     func()


# i = 1

# print(id(1))


# def f1(x): return x * i


# i = 2


# def f2(x): return x * i


# i = 3

# print(id(i))


# def f3(x): return x * i


# print(id(i))
# i = 4


# def f4(x): return x * i


# # u = [f1, f2, f3, f4]

# print(f1(2))


# def message(mes):
#     def say():
#         return mes
#     return say


# mes = 'fufu'
# a = message(mes)
# mes = 'pupu'
# b = message(mes)
# print(a())
# print(b())

class Employee:
    __slots__ = ['first', 'last', 'pay', 'email']
    print('class caleed')
    # a = 'A'
    # print(a)

    def __init__(self, first, last, pay):
        print('init called')
        self.first = first
        self.last = last
        self.pay = pay
        print('beforre fullname meth')
        self.fullname = f'{first.upper()} {last.upper()}'
        print('after fullname method ')
        # print(self.first)
        self.email = f'{self.first}.{self.last}@gmail.com'
        print('init_finised')

    @property
    def fullname(self):
        print('Getter called')
        return f'{self.first} {self.last}'
        print('getter finied ,but wont run')

    @fullname.setter
    def fullname(self, name):
        print('Setter called')
        first, last = name.split(' ')
        self.first = first
        self.last = last
        print('setter finished')


print('npthong')
emp_1 = Employee('frank', 'young', 50000)
print('1 is fne')
emp_2 = Employee('joe', 'hsi', 90000)
print('1 is fne')

# print('inited')
print('oook')
print(emp_1.fullname)
print(emp_1.email)
emp_1.fullname = 'john doe'
print(emp_1.fullname)


class test:
    print('hoho')

    def __init__(self, a, b):
        self.x = (a, b)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        a, b = value
        self._x = "Get this from {} and make a dataframe like {}".format(a, b)


# print(dir(test))
t = test(42, 'foo')
print(t.x)
# 'Get this from 42 and make a dataframe like foo'

# print(di(5))

# def di(x):
#     return 'a'


class testDec:
    print('jojo')

    @property
    def x(self):
        print('called getter')
        return self._x

    @x.setter
    def x(self, value):
        print('called setter')
        self._x = value


t = testDec()
# t.x
t.x = 5
for x in range(0, 10, 2):
    print(x)


class Circle:
    __slots__ = ['diameter']
    # 'An advanced circle analytic toolkit'
    version = '0.6'
    #

    def __init__(self, radius):
        self.radius = radius

    @property  # convert dotted access to method calls def radius(self):
    def radius(self):       # 'Radius of a circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


class m(Circle):
    pass


n = m(1)
n.weo = 3
a = Circle(6)
print(dir(a))

a.radius = 0.5
# a.www = 1
# print(a.__dict__)
print(dir(m))
print('uuu')
print(n.__dict__)
print(m.__dict__)
print(n.__slots__)
# print(emp_1.__dict__.keys())
