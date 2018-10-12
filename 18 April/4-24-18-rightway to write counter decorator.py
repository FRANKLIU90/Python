# def outer(message):
#     print(locals())

#     def inner():
#         print(locals())
#         # print(globals())
#         return message
#     return inner


# result = outer('hello')
# result = result()
# print(result)
# answer = outer('answer')
# answer = answer()
# print(answer)
from functools import wraps


def count(wrapped):
    # inner.counter = 0
    # @wraps(wrapped)
    def inner(*args, **kwargs):
        inner.counter += 1
        # print(locals())
        # print(inner.counter)
        return wrapped(*args, **kwargs)
    inner.counter = 0

    return inner


# count.numer = 1


@count
def myfunc():
    pass


print(myfunc.__name__)

myfunc()
myfunc()
myfunc()
myfunc()
print(myfunc.__dict__)
# print(inner.counter)

from functools import wraps
import inspect
import wrapt


def cache(my_func):
    saved = {}

    @wraps(my_func)
    def wrapper(*args):
        if args in saved:
            return saved[args]
        result = my_func(*args)
        saved[args] = result
        return result
    return wrapper


@wrapt.decorator
def other_cache(my_func, instance, args, kwargs):
    return my_func(*args, **kwargs)

# @cache


@other_cache
def my_func(num):
    return num * 2


print(inspect.getargspec(my_func))
print(my_func.__name__)
