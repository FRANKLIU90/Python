def counter(my_func):

    # @wraps(my_func)
    def wrapper(*args, **kwargs):
        # wrapper.count = 0

        counter.count += 1
        # print(counter.count)
        return my_func(*args, **kwargs)

    # wrapper()
    # wrapper.count = 0
    # wrapper.c = 9
    counter.count = 3
    return wrapper


counter.count = 0


@counter
def p():
    return 3


print(id(counter))
print(id(p))
# print(id(wrapper))
# counter(p)
z = p()
z = p()
z = p()
print(counter.count)
from itertools import count
# print(count.__code__)
import inspect
print(inspect.getsource(counter))


def outer():
    a = 0

    def inner():
        if a == 0:
            a = 1
        print(a)
        a = 2
        print(a)
    return inner


outer()()
