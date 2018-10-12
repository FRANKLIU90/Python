# def mac(a=[]):

#     a.append(1)
#     return a


# m = mac()
# print(m)
# n = mac()
# print(n)
# def greeting(message):

#     def inner():
#         return message
#     return inner


# a = greeting('hello')
# b = greeting('hi')
# print(a())
# print(b())

# for x in range(5):
#     pass
# print(x)

# def create_multipliers():
#     multipliers = []

#     for i in range(2):
#         def multiplier(x):
#             return i * x
#         multipliers.append(multiplier)

#     return multipliers


def create_multipliers():
    multipliers = []

    i = 1

    def multiplier(x):
        return i * x
    multipliers.append(multiplier)

    i = 2

    def multiplier(x):
        return i * x
    multipliers.append(multiplier)

    return multipliers


for multiplier in create_multipliers():
    print(multiplier(2))
# dsa

from contextlib import suppress
# print(NameError == (NameError,))
from contextlib import contextmanager


# @contextmanager
# def ignored(exceptions):
#     try:
#         yield
#     except exceptions:
#         pass


# print b
# with ignored(NameError):
#     # sdaf = 3333s
#     PRINT(A)
# try:

#     print(A)
# except Exception:
#     pass
# import sys
# with open('help.txt', 'w') as f:
#     oldstout = sys.stdout
#     print(oldstout)
# def mac(nums=[]):

#     nums.append(1)
#     print(nums)


# mac()
# mac()
# mac()
from functools import wraps


def pre_dict_cache(saved={}):#if you put {} for a default value, all cache share the same saved , that is not what you want.so this is wrong way to do it.
    # if not saved:
    #     saved = {}

    def cache(my_func):
        @wraps(my_func)
        def wrapper(*args):
            if args in saved:
                print(saved)
                return saved[args]
            result = my_func(*args)
            saved[args] = result
            print(saved)
            return result
        return wrapper
    return cache


@pre_dict_cache()
def joe(x):
    return 'mmm'


@pre_dict_cache()
def John(x):
    return 'h22h'


@pre_dict_cache()
def my_func(x):
    return 'H20'


my_func('joe')
joe('w')
John('ji')
