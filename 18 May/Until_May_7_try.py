import datetime

# string format : nums,dictionary,list,Date
# https://www.youtube.com/watch?v=vTX3IwquFkc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=21
num = 3.1415926
dic = {'name': 'frank', 'age': 27}
lst = ['python', 'java']
dt = datetime.date.today()
str_formatting = 'the pi is {0:.2f},my name is {name}, i am {age} years old,i am learing {1} and {2},today is {3:%B %Y %d}'.format(num, *lst, dt, **dic)
# try:{name.upper()} ,Not Supported./AttributeError: 'str' object has no attribute 'upper()'
# "cant not use method call in ''.format(),only subscription (indexing by number or by unquoted (!) name), and attribute access is supported.but f'{name.upper()}' works.
# name = 'frank'
# print(f'{name.upper()}')
# print('{.upper()}'.format(name))

print(str_formatting)


# object sorting
from operator import itemgetter, attrgetter, methodcaller

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_tuples, key=itemgetter(1, 2)))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10), ]

print(sorted(student_objects, key=attrgetter('age')))
print(sorted(student_objects, key=attrgetter('grade', 'age')))

messages = ['critical!!!', 'hurry!', 'standby', 'immediate!!']
print(sorted(messages, key=methodcaller('count', '!')))

"""contextmanger"""
import os
import glob
import contextlib


@contextlib.contextmanager
def find_py(path):
    ori_path = os.getcwd()
    try:
        os.chdir(path)
        result = glob.glob('*.py')
        yield result
    finally:
        os.chdir(ori_path)


# with find_py('/Users/frankyoung/Documents/Python3/18 March') as f:
#     for pyfile in f:
#         print(pyfile)
class Find_Py:
    def __init__(self, path):
        self.path = path
        self.ori_path = os.getcwd()

    def __enter__(self):
        os.chdir(self.path)
        result = glob.glob('*.py')
        return result

    def __exit__(self, exc_type, exc_val, traceback):
        os.chdir(self.ori_path)


# with Find_Py('/Users/frankyoung/Documents/Python3/18 March') as f:
#     for pyf in f:
#         print(pyf)
# print(os.getcwd())


@contextlib.contextmanager
# Nick Coghlan
def suppress(*exceptions):
    try:
        yield
    except exceptions:
        pass


# decorator,scope,closure
# the LEGB rule , for accessing(say,print) and modifying(append) mutable var only.But not reasigning after referenced.UnboundLocalError: local variable referenced before assignment.
# <Thomas Ballinger - Finding closure with closures - PyCon 2016>"It turns out that Python analyzes function source code, even compiles it, when a function is defined. During this process it determines the scope of each variable. This determines the process that will be used to find the value of each variables, but does not actually look up this value yet."
# "the scope of a var is determined when function is defined , the value of a var is determined when the function is called".
# http://docs.python-guide.org/en/latest/writing/gotchas/
# Late Binding Closures
funcs = [lambda x: x * i for i in range(3)]  # by the way , i here is a local var.so i doesnt ni=ot exist in the global scope.if try to print i , 'NameError: name 'i' is not defined'
for func in funcs:
    print(func(2))
# 4,4,4
# you will get 2*2=4,2*2=4,2*2=4,because the three 'i's  are in the same scope,when the functions is called , i=2.so you get 4,4,4.
# Solution:use keyword args.'Python’s default arguments are evaluated once when the function is defined, not each time the function is called '
funcs = [lambda x, i=i: x * i for i in range(3)]
for func in funcs:
    print(func(2))
# 0,2,4
# or you can use generator expression, without keyword args.because generator look up the value as it goes.
funcs = (lambda x: x * i for i in range(3))
for func in funcs:
    print(func(2))
# 0,2,4
#
# function attribute, functions can have attributes.
# make a counter decorator
from functools import wraps


def counter(my_func):
    @wraps(my_func)
    def inner(*args, **kwargs):
        inner.count += 1
        return my_func(*args, **kwargs)
    inner.count = 0
    return inner


@counter
def i_tell_you_what():
    return 'i tell you what'


i_tell_you_what()
i_tell_you_what()
print(f'{i_tell_you_what.__name__} run {i_tell_you_what.count} times')

# make a cache with a default return dictionary as an arg


def cache_with_default(dct=None):
    if dct is None:
        dct = {}

    def cache(my_func):
        @wraps(my_func)
        def wrapper(*args):
            if args in dct:
                return dct[args]
            result = my_func(*args)
            dct[args] = result
            return result
        return wrapper
    return cache


@cache_with_default({(1,): 100})  # be careful, pass 1 as a tuple (1,) or it wont work.becaues the args will be (1,)
def times_two(x):
    return x + x


print(times_two(1))  # get 100 inside of 2 , because it was looked up in the dct


# Brett Slatkin - How to Be More Effective with Functions - PyCon 2015 - YouTube
# keword_only_args:forced to be clear.
def bobby(*, propane=True, charcoal=False):
    if propane:
        print('there you go')
    else:
        print('the hell you say')


try:
    bobby(True, False)
except Exception as e:
    print(e)  # bobby() takes 0 positional arguments but 2 were given
bobby(propane=True, charcoal=False)  # there you go

# what is generator?
# iter(foo) is iter(foo)
# base on the talk-->
# if iter(foo) is iter(foo):
#     now,then =itertools.tee(foo,2)
# customize iteration : "Brett Slatkin - How to Be More Effective with Functions - PyCon 2015 - YouTube" + "Loop like a native_ while, for, iterators, generators" ---->by using class __iter__ method
# http://nvie.com/posts/iterators-vs-generators/    : iter(iterable)-->iteration
# how to detect a generator
# how does generator function(yield) run?
lst = [1, 2, 3]
a = iter(lst)
b = iter(lst)
print(a is b)  # False
c = iter(a)
print(a is c)  # True
# so if iter(foo) is iter(foo), foo is a generator; is iter(foo) is not iter(foo), foo is a container. 'iter over a iterator returns itself.'


# how yield works

import contextlib


def HYW():
    print('hello')
    yield
    print('world')


a = HYW()  # Nothing happend, ! hello was not printed.
next(a)  # ---> now hello was printed. so when you call next, generator will run till it hits a yield

with contextlib.suppress(StopIteration):
    next(a)  # -----> world was printed, and then it hits the StopIteration


#  Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015
a = [1, 2, 3]
b = a
a += [4, 5]  # what happened here unline is "a.extend([4,5]) and a =a "
print(b)  # -->[1, 2, 3, 4, 5]

a = [1, 2, 3]
b = a
a = a + [4, 5]
print(b)  # -->[1, 2, 3]

a = [1, 2, 3]
b = a
a.extend([4, 5])
print(b)  # -->[1, 2, 3, 4, 5]

a = [1, 2, 3]
b = a
a = a.extend([4, 5])
print(a)  # None
print(b)  # [1, 2, 3, 4, 5]

a = [1, 2, 3]  # try to make a =[10,20,30]
for x in a:
    x = x * 10
print(a)  # [1, 2, 3] failed:) beacuse a[0]still is 1 . the right way ,a=[x*10 for x in a]

print('now')


def kwargs_only(*args, a=1):
    print(a)
    print(args)


"""
Circles, Inc.
"""


class Circle:  # python 3 is automatically a new style class. 2.7 needs to inherit (object)
    from math import pi
    """An advvanced circle analytics toolkit"""
    # don/t skip the elevator pitch ,your doc string.
    # what is inside a class is effectlly a module ,it is like the code run in its own module.

    print('i am defining a class')  # it will print only by defining it.
    # raymond also talked about you can open file or for loop with in the class.

    version = '0.1'  # class variable for shared data,while instance var for unique data. use str, or tuple
    print('dont use bi_floats , try:0.1+0.7,you will get ', 0.1 + 0.7)  # 0.7999999999999999

    def __init__(self, radius):
        # "__init__ " is not a constructor. is calling the class construct a instance.__init__ is 'poplulate' instance variable.
        # one thing is for sure, user is gonna make lots of instance, i mean a lot .
        print('i am running __init__')
        self.radius = radius

    def area(self):
        return self.radius**2 * pi
    # so far we are good to go, more method ? until user ask for it! before that,YAGNI:) Lean startup.


# First customer: Academia
# from random import random, seed
# seed(8675309)
# print 'Using Circuituous(tm) version', Circle.version
# n = 10
# circles = [Circle(random()) for i in xrange(n)]
# print 'The average area of', n, 'random circles'
# avg = sum([c.area() for c in circles]) / n
# print 'is %.1f' % avg
# print

    def perimeter(self):
        # new customer wants a perimeter method.
        return self.radius * 2 * pi

# Second customer: Rubber sheet company
# cuts = [0.1, 0.7, 0.8]
# circles = [Circle(r) for r in cuts]
# for c in circles:
#     print 'A circlet with with a radius of', c.radius
#     print 'has a perimeter of', c.perimeter()
#     print 'and a cold area of', c.area()
#     c.radius *= 1.1
#     print 'and a warm area of', c.area()
#     print


# this customer changed the attribute "c.radius *= 1.1"
"if it is a variable, it is gonna change, sooner or later"  # R.H

# If you expose an attribute, expect users to all kinds of interesting things with it.


# 3rd customer Tire
class Tire(Circle):
    'Tires are circles with a corrected perimeter'
    # again
    "if it is a variable, it is gonna change, sooner or later"  # R.H


def perimeter(self):
    'Circumference corrected for the rubber'
    return Circle.perimeter(self) * 1.25


# t = Tire(22)
# print 'A tire of radius', t.radius
# print 'has an inner area of', t.area()
# print 'and an odometer corrected perimeter of',
# print t.perimeter()
# print


# Next customer: Na;onal graphics company
# bbd = 25.1
# c = Circle(bbd_to_radius(bbd)
# print 'A circle with a bbd of 25.1'
# print 'has a radius of', c.radius
# print 'an an area of', c.area()
# print

# c = Circle(bbd_to_radius(bbd)) -------> this is Baaaad!
'USE Alternative Constructor'
print(dict.fromkeys(['name', 'age', 'language']))
#{'name': None, 'age': None, 'language': None}

# /lets go back and add the alternative constructor

import math


class Circle:

    'An advanced circle analytic toolkit'
    version = '0.3'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    # classmethod make sure you use cls , for the subclass usage
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0)
        # return Circle(radius) NONO!
        # classmethod make sure you use cls , for the subclass usage
        return cls(radius)


c = Circle.from_bbd(25.1)
# print 'A circle with a bbd of 25.1'
# print 'has a radius of', c.radius
# print 'an an area of', c.area()
# print

# New customer request: add a func
# use staticmethod ,a giveaway is your func does not need 'self' or 'cls'. you use staticmethod for the findability of your func.


class Circle(object):
    'An advanced circle analytic toolkit'
    version = '0.4'

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    # attach functions to classes to increase the findability of your func.
    # a giveaway is your func does not need 'self' or 'cls'.
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


# Government request: ISO-11110: "you need to use perimeter to calc the area" ,like this:

# class Circle(object):
#     'An advanced circle analytic toolkit'
#     version = '0.5b'
#     def __init__(self, radius):
#             self.radius = radius
#     def area(self):
#         p = self.perimeter()
#         r = p / math.pi / 2.0 return math.pi * r ** 2.0
#     def perimeter(self):
#         return 2.0 * math.pi * self.radius


# that wasnot too bad,really?
# the Tire subclass update the perimeter, now you broke their code.

# class Tire(Circle):
#     'Tires are circles with an odometer corrected perimeter'
# def perimeter(self):
# 'Circumference corrected for the rubber' return Circle.perimeter(self) * 1.25


'so what to do?'  # normally 'self' means you or your children.in this case. self.perimeter(). means if tire class has this method.it will not look up to the mother class.So you want to make 'self' means you Only ------>local reference.
# the idea is to  use classname+methodname.
# __perimeter---> Name mangling into---> '_(class.__name__)__perimeter'


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    # make local refernce perimeter
    __perimeter = perimeter

    # see Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015
    # a=3
    # b=a
    # a=4
    # print(b)---->3

    def area(self):
        p = self.__perimeter()
        r = p / (2 * math.pi)
        return math.pi * r**2


# Government request: ISO-22220
# •  You’re not allowed to store the radius
# •  You must store the diameter instead!

# we get to keep the api the same. still i accept radius in __init__, but diameter will be stored instead.


# it breaks our entire class!
#" I just wish everytime i use dot for look up,            it will magiclly trans into a get method call ()"
#" I just wish everytime I set a radius(even in __init__) ,it will magiclly trasn in to s set radius call,--store the diameter."
# yes, this is the @property .But dont do it just for it.dot look up and '=' assign is much easier."if you find yourself design a setter and getter,you probably doing it wrong"
# property is for "after the fact , that you dont need to change any existing code.and add on the property"


# User request: Many circles
# n = 10000000
# seed(8675309)
# print 'Using Circuituous(tm) version', Circle.version
# circles = [Circle(random()) for i in xrange(n)]
# print 'The average area of', n, 'random circles'
# avg = sum([c.area() for c in circles]) / n
# print 'is %.1f' % avg
# print
# I sense a major memory problem.
# Circle instances are over 300 bytes each!

'Flyweight design paUern: Slots'
# save this for the last.you cant add new attr ,you cant access the dictinary no more.no vars() or .__dict__.
# "from the user view, there are no changes at all"_R.H
# dont worry ,subclass does not inherit the slots


class Circle(object):

    'An advanced circle analytic toolkit'
# flyweight design pattern suppresses
# the instance dictionary
    __slots__ = ['diameter']
    version = '0.7'

    def __init__(self, radius):

        self.radius = radius

    @property  # convert dotted access to method calls
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


"""Summary: Toolset for New - Style Classes
1.  Inherit from object().
2.  Instance variables for informa
on unique to an instance.
3.  Class variables for data shared among all instances.
4.  Regular methods need “self” to operate on instance data.
5.  Thread local calls use the double underscore. Gives subclasses the freedom to override methods without breaking other methods.
6.  Class methods implement alterna
ve constructors. They need “cls” so they can create subclass instances as well.
7.  Sta
c methods aUach func
ons to classes. They don’t need either “self” or “cls”. Sta
c methods improve discoverability and require context to be specified.
8.  A property() lets geUer and seUer methods be invoked automa
cally by aUribute access. This allows Python classes to freely expose their instance variables.
9.  The “__slots__” variable implements the Flyweight Design PaUern by suppressing instance dic
onaries."""
nums = [1, 2, 3]
print(nums.__iadd__([4, 5]))  # inplace and return the new value
print(nums)
print(nums.extend([7, 8]))  # inplace but no return value,so print None
print(nums)

dct = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
dct.pop('matthew')
print(dct)
