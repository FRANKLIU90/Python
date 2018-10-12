# message = 'hello world'
# message = message.replace('world', 'university')
# # print(message.upper())
# # print(help(str))
# nums = [5, 10, 15, 20, 25, 30]
# for index, num in enumerate(nums):
#     nums[index] = str(round(num / 5))
# # print(nums)
# d = {1: 3, 2: 4, 5: 1}
# result = sorted(d.keys(), key=d.get)
# x = d.popitem()
# print(d)
# print(x)
# print(result)

names = ['tom', 'john', 'alex', 'federer', 'eric clapton', 'young']

# result = {}
# for name in names:
#     key = len(name)
#     result[key] = result.get(key, []) + [name]

# print(result)
# from collections import defaultdict
# result = defaultdict(lambda: [])
# for name in names:
#     key = len(name)
#     result[key].append(name)
# print(result)

# result['hello']
# result['there']
# print(result)


# def add(a, b, *, c=5, d=6):
#     return a + b + c + d


# print(add(1, 1, c=1))

# def feb(a, b, n):
#     yield a
#     for x in range(n - 1):
#         a, b = b, b + a
#         yield a


# for x in feb(0, 1, 10):
#     print(x)
from functools import wraps


def counter(my_func):
    num = 1

    @wraps(my_func)
    def wrapper(*args):
        num = num + 1
        print(num)

        result = my_func(*args)
        return result
    return wrapper


@counter
def my_func():
    return 'a'


# my_func()


# def cache(func):
#     saved = {}

#     @wraps(func)
#     def wrapper(*args):
#         if args in saved:
#             return saved[args]
#         result = func(*args)
#         saved[args] = result
#         print(saved)
#         return result
#     return wrapper


# @cache
# def my_func(a, b):
#     return max(a, b)


# duo = my_func(1, 2)
# muo = my_func(2, 3)

# print(duo)
# print(muo)
