import datetime
import pytz
import re
import sys
# yan = datetime.datetime(2012, 11, 23, 20, 30, 45)
# # b = datetime.datetime(2103, 2, 1, 1, 2, 3)
# # print(b)
# now = datetime.datetime.now(tz=pytz.timezone('US/Central'))
# yan = pytz.utc.localize(yan)
# print(yan)
# then = now.astimezone(pytz.utc)
# print(then)
# # print(sys.getsizeof(now))
# s = now.isoformat()
# print(sys.getsizeof(s))
# print(now)
# print(s)
# print((now - yan).total_seconds())
# wo = now.strftime('%B')
# print(wo)


# all_tz = pytz.all_timezones
# print(all_tz)
# all_tz = ' '.join(all_tz)
# pattern = re.compile(r'CST')
# matches = pattern.finditer(all_tz)
# for match in matches:
#     print(match)
# print('sss' in 'sssssss')
# for index, item in enumerate(all_tz):
#     if 'CST' in item:
#         print(index)
#         break
# print(all_tz[371])
# today = datetime.datetime.today().replace(tzinfo=pytz.timezone('US/Central'))
# today = datetime.datetime.today()
# now = datetime.datetime.now(tz=pytz.timezone('US/Central'))
# print(today)
# timezone = pytz.timezone('US/Central')
# today = timezone.localize(today)
# print(today)
# print(now)
# utcnow = datetime.datetime.utcnow()
# print(utcnow)
# classmethod always use cls for subclass
#__repr__ usage
#__from_string__usage, if string contain classname then: classname,*info=info_string.split(' ')


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @classmethod
    def from_str(cls, info_string):
        return cls(*info_string.split(' '))

    def __repr__(self):
        return f'{self.__class__.__name__}{tuple(vars(self).values())}'


emp_1 = Employee.from_str('frank young')
print(emp_1)


# cache decorator with default dict
# beware  use "()" in @cache_with_default() even when  no default args are passed in,  that make you go to the depper level into the wrapper func
from functools import wraps


def cache_with_default(saved=None):
    # cannot use mutable value for keyword args,use None for different my_func passed in, if only 1 my_func is gonna passed in, you dont need decorator, just pass the saved={},into cache level.see 'Transforming Code into Beautiful, Idiomatic Python'
    if saved == None:
        saved = {}

    def cache(my_func):
        @wraps(my_func)
        def wrapper(*args):
            if args in saved:
                print('return from saved dict')
                print(saved)
                return saved[args]
            result = my_func(*args)
            saved[args] = result
            print('return function called')
            print(saved)
            return result
        return wrapper
    return cache


@cache_with_default(saved={(1,): 123})
def my_func(a):
    return a**2


print(my_func(1))
# return from saved dict
# {(1,): 123}
# 123
print(my_func(2))
# return function called
# {(1,): 123, (2,): 4}
# 4
# [Finished in 0.1s]


# global can be accssed (print,modify(mutable) ), but cant not be used to re-assign


nums = [1, 2, 3]


def modify():
    print(nums)
    nums.append(4)


modify()  # [1, 2, 3, 1]


def re_assign():
    print(nums)
    nums += [5]
    # num=list.__iadd__(nums,[5]) this is modify first then re_assign,wont work for the assign part.


try:
    re_assign()
except Exception as e:

    print(e)  # local variable 'nums' referenced before assignment# csv.DictWriter fieldnames doesn't have to in order as the original DictReader, but all fieldnames have to be there.to modify del reader['keys']before write to writer


import csv

with open('Customer_Satisfaction.csv') as rf:
    reader = csv.DictReader(rf)
    print(reader.fieldnames)  # ['Year', 'Category', 'Satisfaction Rating']
    with open('Customer_Satisfaction_copy.csv', 'w') as wf:
        fieldnames = ['Category', 'Year']
        writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for line in reader:
            del line['Satisfaction Rating']
            writer.writerow(line)


nums = [1, 2, 3]
# print(type(iter(nums)))
# a = iter(nums)
# print(type(a))
# print(a is iter(nums))
# print(iter(nums)is iter(nums))
# print(id(iter(nums)) == id(iter(nums)))
print(nums.__iadd__([4, 5]))  # inplace and return the new value
print(nums)
print(nums.extend([7, 8]))  # inplace but no return value,so print None
print(nums)


m = [1, 2, 3]
n = m
m += [5]  # m=m.__iadd__(n) = list.__iadd__(m,n) inplace and return the new value,this is modify m and re_assign m ,m=m.because m is modified ,so n see the change
print(n)  # [1, 2, 3, 5]


m = [1, 2, 3]
n = m
m = m + [5]
print(n)  # [1,2,3] re_assign m , doen't effect n.

# https://nedbatchelder.com/text/names1.html


# Brett Slatkin - How to Be More Effective with Functions - PyCon 2015 - YouTube
import csv


def info_gen(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        for line in reader:
            del line['Year']
            yield line


class Info_Gen:
    def __init__(self, path):
        self.path = path
        print(self.path)

    def __iter__(self):
        return info_gen(self.path)  # important must be return!!! to a genator func ,i believe it is the scope reason, if not returned, values are not catched.


for line in Info_Gen('Customer_Satisfaction.csv'):
    print(line)
print('0done')
for line in Info_Gen('Customer_Satisfaction.csv'):
    print(line)
print('00done')

######
a = 1
def p():
    print(a)


a = 2
def w():
    print(a)


p() #2
w() #2
