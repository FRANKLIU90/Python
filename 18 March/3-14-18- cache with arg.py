# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# a = enumerate(nums)
# print(next(a))
# print(iter(a)is iter(a))
# for index, num in enumerate(nums):
#     print(enumerate(nums))
#     if num % 2 == 0:
#         del nums[index]
# a = enumerate(nums)
# b = enumerate(nums)
# print(iter(enumerate(nums))is iter(enumerate(nums)))

# print(nums)


# d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
# for x in d.keys():
#     if x == 'rachel':
#         del d[x]
# for x in d:
# a = d.keys()
# print(iter(a) is iter(a))
# print(next(a))
# for x in d:
#     if d[x] == 'green':
#         del d[x]


# with open('march_try_except.py', 'r+') as f:
#     for linenum, line in enumerate(f, start=1):
#         if line == '# class Employee:':
#             del line[linenum]

# names=['alpha', 'bravo', 'charlie', 'delta']

# d=dict.fromkeys(names)
# print(d)

from functools import wraps


def pre_dict_cache(saved=None):
    if not saved:
        saved = {}

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


# def cache(my_func):
#     saved = {}

#     @wraps(my_func)
#     def wrapper(*args):
#         if args in saved:
#             print(saved)
#             return saved[args]
#         result = my_func(*args)
#         saved[args] = result
#         print(saved)
#         return result
#     return wrapper


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
