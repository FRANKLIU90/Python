import itertools


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, b + a


w = fib()
z = itertools.islice(w, None, 20)

result = itertools.takewhile(lambda x: x < 400, z)
for x in result:
    print(x)
print(next(w))

u = itertools.repeat('xyz', 1)
# print(list(u))
# n = list(u)  # ['zzz', 'zzz']
# z = itertools.chain.from_iterable(itertools.repeat(itertools.repeat('zzz', 2), 3))
# print(list(u))
z = itertools.cycle(u)
e = next(z)
# print(e)
for x in e:
    print (x)
e = next(z)
for x in e:
    print (x)
e = next(z)
for x in e:
    print (x)
e = next(z)
for x in e:
    print (x)
e = next(z)
for x in e:
    print (x)
b = itertools.islice(itertools.count(), 7, 14)
c = itertools.accumulate(b)
print(list(c))
a = itertools.count()
b = itertools.dropwhile(lambda x: x < 10, a)
print(next(b))  # 10
print(next(a))  # 11
a = itertools.count()
b = itertools.takewhile(lambda x: x < 10, a)
print(next(b))  # 0
print(next(a))  # 1
for x in b:
    print (x)
print(next(a))
print('www')

# dropwhile is ablout what is left, so has the first broken value,
# and take while is ablout what has been took.no first broken value left for the original iterator.


def my_dropwhile(func, iterable):
    for x in iterable:
        if func(x):
            continue
        return itertools.chain([x], iterable)  # so i can keep the last x
        # return iterable


def k(x): return x < 10


i = itertools.islice(itertools.count(), 20)
m = my_dropwhile(k, i)
for x in m:
    print(x)

print('hhhhh')


def q():

    raise StopIteration


def my_takewhile(func, iterable):
    return (x if func(x) else q() for x in iterable)


def k(x): return x < 10


i = itertools.islice(itertools.count(), 20)

m = my_takewhile(k, i)
for x in m:
    print(x)
print(next(i))


# next(itertools.islice(itertools.count(), 1, 1)) #give you StopIteration


def z(x, y): return x + y

# see printed python 201 intro itertoools page 7.the difference between map and itermap and map with 2+ iterable.


# s = map(z, ((1, 2), (3, 4)))
# for x in s:
#     print(x)
z = sorted("bCAaCacAADBbB")
print(z)
print('ww')


def key(x): return x.islower()


m = sorted("bCAaCacAADBbB", key=key)

z = itertools.groupby(m, key)
for x, y in z:
    print(x, list(y))
    print()


# for x in list(itertools.groupby(range(10))):
#     print(list(x[1]))
z = list(itertools.groupby(range(10)))
w = itertools.groupby(range(10))
# print('f')
# a = next(w)
# print(['z'])
# print(print(list(a[1])))
# print('22')
# o = ((x, list(y)) for x, y in w)
# for x, y in o:
#     print(x, y)

w = itertools.islice(itertools.count(), 10)
a = itertools.groupby(w)
for x in a:
    print(list(x[1]))
# print(next(w))
a = range(10)
for x in a:
    print(x)
print('de')
for x in a:
    print(x)
c = itertools.groupby([1, 2, 3, 4, 5])
c = list(c)
print(c)
a = c[0]
print(a, list(a[1]))
input = [
    ('11013331', 'KAT'),
    ('9085267', 'NOT'),
    ('5238761', 'ETH'),
    ('5349618', 'ETH'),
    ('11788544', 'NOT'),
    ('962142', 'ETH'),
    ('7795297', 'ETH'),
    ('7341464', 'ETH'),
    ('9843236', 'KAT'),
    ('5594916', 'ETH'),
    ('1550003', 'ETH')
]
from operator import itemgetter
input = sorted(input, key=itemgetter(1))
print(input)
# print('zz')
# [('5238761', 'ETH'), ('5349618', 'ETH'), ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('5594916', 'ETH'), ('1550003', 'ETH'), ('11013331', 'KAT'), ('9843236', 'KAT'), ('9085267', 'NOT'), ('11788544', 'NOT')]

output = itertools.groupby(input, key=itemgetter(1))
outPut = [{'key': key, 'nums': [x[0] for x in items]} for key, items in output]
print(outPut)
import json
outPut = json.dumps(outPut, indent=2)
print(outPut)

for x, y in output:
    print(x, list(y))
print(())

#???????????
ls = [1, 5, 5]
z = itertools.groupby(ls)
# print(list(z))
a = list(z)  # z has been consumed here
for x, y in a:
    print(list(y))

ls = [1, 5, 5]
z = itertools.groupby(ls)
for x, y in z:
    pass
print(list(y))


input = [
    ('11013331', 'KAT'),
    ('9085267', 'NOT'),
    ('5238761', 'ETH'),
    ('5349618', 'ETH'),
    ('11788544', 'NOT'),
    ('962142', 'ETH'),
    ('7795297', 'ETH'),
    ('7341464', 'ETH'),
    ('9843236', 'KAT'),
    ('5594916', 'ETH'),
    ('1550003', 'ETH')
]

sort_input = sorted(input, key=itemgetter(1))
# print(sort_input)
# [('5238761', 'ETH'), ('5349618', 'ETH'), ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('5594916', 'ETH'), ('1550003', 'ETH'), ('11013331', 'KAT'), ('9843236', 'KAT'), ('9085267', 'NOT'), ('11788544', 'NOT')]
result = itertools.groupby(sort_input, key=itemgetter(1))
result = [{'key': key, 'value': [nums for nums, u in value]} for key, value in result]
print(result)
c = itertools.groupby([1, 2, 3, 4, 5])
# print({x: list(y) for x, y in c})
# print(list(y))
z = range(101)
result = itertools.groupby(z, lambda x: x // 6)
# for key, items in result:
#     print({key: list(items)})
print([tuple(items)for key, items in result])
z = list(itertools.zip_longest(*[iter(z)] * 4))
z[-1] = tuple(n for n in z[-1] if n)
print(z)
u = range(100)
# print(tuple(u))
# print(tuple(x for x in u))
# print((u))
# print(type())
a = [(1, 2, 3), (4, 5, 6, None), (7, 8, 9), (10, 11, 12), (13, 14, None)]
# itertools.chain.from_iterable(())
z = [(11, 12, 13),
     (21, 22, 23, 24),
     (31, 32),
     (41, 42, 43, 44), ]


# def zipper(*iterables):
#     for iterable in iterables:use itemgetter?
from contextlib import suppress


# def zipper(*iterables):
#     iterators = map(iter, iterables)
#     # while True:
#     with suppress(StopIteration):
#         yield map(next, iterators)
from functools import partial


def zipper(*iterators):
    n = len(iterators)
    # return iter(partial(map(next, iterators, (None) * n)), (None,) * n)
    return iter(partial(map, next, iterators, (None, ) * n), (None,) * n)
    # result = map(next, iterators, (None,) * n)
    # Result = tuple(result)
    # while not Result == (None,) * n:
    #     result = map(next, iterators, (None,) * n)
    #     Result = tuple(result)
    #     yield Reselt


# z = map(iter, z)
# w = zipper(*z)
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(w)
# print(list(next(w)))
# # print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# print(list(next(w)))
# for x in w:
#     print(list(x))
# if (None):
#     print(True)
# print((1,) * 3)
'!!!!!!!!!!!!!!my zipper'


def zipper_2(*iterators):
    result = tuple(map(next, iterators))

    while result:
        print('after while ,before yield')
        yield result
        with suppress(StopIteration):
            print('after suppress ,before map')
            result = map(next, iterators)
        print('after new  map result')
        result = tuple(result)


z = map(iter, z)
s = zipper_2(*z)
for x in s:
    print(x)
# next(s)
# w = iter([0])
# with suppress(StopIteration):
#     a = next(w)
#     print(a)
#     print('z')
# with suppress(StopIteration):
#     a = next(w)
# # print(a)
# print('z')


def my_next(iterator):
    try:
        return next(iterator)
    except StopIteration:
        pass


def zipper(*iterables):
    iterators = map(iter, iterables)
    # print(next(iterators))
    result = tuple(map(my_next, iterators))
    while result:
        yield result
        result = tuple(map(my_next, iterators))


lists = [(11, 12, 13),
         (21, 22, 23, 24),
         (31, 32),
         (41, 42, 43, 44)]
result = zipper(*lists)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
a = iter([1, 2, 3, 4])
b = my_next(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
