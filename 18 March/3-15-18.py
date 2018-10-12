from contextlib import contextmanager
from operator import methodcaller
from operator import itemgetter


# colors = ['rez', 'greren', 'rurrd', 'yelrrrrlow']

# result = sorted(colors, key=itemgetter(0, 1))
# print(result)
# @contextmanager
# def ignored(*exceptions):
#     try:
#         yield
#     except exceptions:
#         print (exceptions)


# with ignored(NameError):
#     d.keys()
# print(iter(a) is iter(a))
# print(next(a))
# # for x in d:
# def create_multipliers():
#     return [lambda x: i * x for i in range(5)]


# def make_func():
#     for i in range(5):
#         yield lambda x: x * i


# for func in make_func():
#     result = func(2)
#     print(result)


# def create_multipliers():
#     return [lambda x, i=i: i * x for i in range(5)]
# # for multiplier in create_multipliers():
# #     print(multiplier)


# for multiplier in create_multipliers():
#     print(multiplier(2))

# print(create_multipliers())


def greeting(mes):
    def say():
        return mes
    return say


a = greeting('hello')
b = greeting('ball')

for x in [a, b]:
    print(x())
