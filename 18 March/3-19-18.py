import itertools
from functools import partial
# a = itertools.cycle('abcde')
# c = itertools.islice(a, 0, 8)
# print(list(c))
# b = itertools.count()
# c = zip(a, b)

# z = iter(c.__next__, ('e', 9))
# for u in z:
#     print(u)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# a = itertools.repeat('abcde', 3)
# now, then = itertools.tee(a)
# b = itertools.chain.from_iterable(then)

# print(list(now))
# print(list(b))


# def fib():
#     a = 0
#     b = 1
#     while True:
#         if a % 2 == 0:
#             yield a
#         a, b = b, a + b


# f, t = itertools.tee(fib())

# result = itertools.takewhile(lambda x: x < 400000, f)
# print(list(result))


# def mm():
#     raise StopIteration


# r = (x if x < 400000 else mm() for x in t)
# print(list(r))


# x = itertools.compress('hsuisoahsua', itertools.cycle([0, 1]))
# # print(list(x))

# print(list(itertools.takewhile(lambda x: x < 400000 and x > 10, fib())))
# print('')
# a = itertools.chain.from_iterable([['ABC', 'DEF'], [1, 2, 3, 3, 4, 56]])
# print(list(a))
# j = ['ABC', 'DEF']
# w = itertools.chain.from_iterable(j)
# print(list(w))


# def xi(a, b):
#     return a * b * 0


# c = itertools.accumulate([2, 2, 3, 4, 5], xi)
# print(list(c))


# q = itertools.islice(itertools.count(), 0, 100)
# # w = q.copy()
# q, z = itertools.tee(q)

# w = list(z)
# print(w)
# # [0, 3, 6, 9, 12, 15, 18]

# r = itertools.groupby(q, key=lambda x: x // 3)
# # print(next(r))
# f = {x: list(y) for x, y in r}
# # print( < itertools._grouper object at 0x101b70be0)
# print(f)
# for x in range(1, 102, 10):
#     print(x)
# m = itertools.islice(itertools.count(), 10)
# for x in m:
#     print(x)
# from functools import reduce
# a = reduce(lambda x, y: x * y, range(1, 6))
# print(a)
# x = itertools.chain.from_iterable([[1], [2], [3, [1, 2]]])
# print(list(x))
import json
import itertools
from operator import itemgetter
with open('new_states.json') as f:
    data = json.load(f)

xdata = json.dumps(data, indent=2)
# for x in data['states']:
#     name=x['name']
#     abbr=x['abbreviation']

# print(data['states'][0])

# going = ((x['name'], x['abbreviation']) for x in data['states'])
# result = itertools.groupby(going, key=lambda x: x[1][0])
# print({x: list(y) for x, y in result})

names = ['raymond', 'rachel', 'mathew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
# for x in names:
#     print(x)
# names = sorted(names, key=len)
names.sort(key=len)
result = itertools.groupby(names, key=len)
print({x: list(y) for x, y in result})
# for z in y:
#     print(z)
#     print('oooooooo')
# for x in result:
#     print(x[0])
for x, y in result:
    print('\n')
    print(x)
    for z in y:
        print(z)
#         print('uuuuuuu')
