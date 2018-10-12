# mydict = {'carl': 40,
#           'alan': 2,
#           'bob': 1,
#           'danny': 3}
# x = {s: y for (s, y) in mydict.items()}
# # x = sorted(x)

# # print(x)
# from operator import itemgetter

# # x = sorted()
# z = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
# e = sorted(z.items())
# print(e)
# w = {a: b for a, b in e}
# print(w)
# # regular unsorted dictionary
# from collections import OrderedDict
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# print(sorted(d.items(), key=lambda t: t[0]))
# # dictionary sorted by key
# print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
# dictionary sorted by value
#     # OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# >> >  # dictionary sorted by length of the key string
# >> > OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
# OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
# nums = [1, 2, 3]
# a = list(enumerate(sorted(nums, reverse=True)))
# print(a)
# from functools import reduce
# z = reduce(lambda x, y: 10 * x[0] + x[1] + 10 * y[0] + y[1], a)
nums = [1, 2, 3, 4, 6, 5, 4, 3, 21]
import itertools
result = itertools.dropwhile(lambda x: x < 6, nums)
# print(list(result))
# from operator import div
import operator
import time
# time.sleep(10000)
l = [(1, 3), (2, 4), (4, 6)]
# M = (division(*args)for args in l)
# print(list(M))
# n = itertools.starmap(operator.div, l)
# print(list(n))

# print(dir(operator))
# i = 1
# for x in itertools.cycle([1]):

#     print(x)

#     i += 1
#     if i > 10000000:
#         break
# a = itertools.cycle('abcde')
# for i in range(100):
#     print(next(a))
# a = itertools.accumulate(range(10))
# for x in a:
#     print(x)
# a = [6, 5, 4, 3, 21]
# z = itertools.compress(a, ['', 'a', [], [1], {}])
# for x in z:
#     print(x)
# w = itertools.zip_longest(a, z)
# print(list(w))
# q = itertools.repeat(iter(a), 3)
# for x in q:
#     print(list(x))
from functools import reduce
l = [6, 5, 4, 3, 2, 1]
q = (x for x in l)
i = zip(l, q)
w = itertools.chain.from_iterable(i)
# print(list(w))
a = reduce(lambda x, y: 10 * x + y, list(w))
print(a)

# print(l * 2)
# a = itertools.cycle(range(200))
# b = itertools.islice(a, 400)
# for x in b:
#     print(x)
