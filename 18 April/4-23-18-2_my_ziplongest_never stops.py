# problem is it never stops

import itertools


def zipper(*iterables):

    iterators = tuple(map(iter, iterables))
    result = tuple(map(next, iterators, itertools.repeat(None)))
    print(locals())

    while result:
        yield result
        result = tuple(map(next, iterators, itertools.repeat(None)))


lists = [(11, 12, 13),
         (21, 22, 23, 24),
         (31, 32),
         (41, 42, 43, 44)]
result = zipper(*lists)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
