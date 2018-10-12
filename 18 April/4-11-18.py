# a = [1, 2, 3]
# b = a
# a = a.extend([4, 5])
# print(a)
# print(b)
# from functools import partial
# with open('3-22-18.py') as f:
#     a = iter(partial(f.read, 32), '')
#     for x in a:
#         print(x)
#     print(list(a))
import itertools
lst = [(0, 0), (2, 3), (4, 3), (5, 1)]

# print(list(itertools.accumulate(lst)))
# print(list(itertools.accumulate(list(*lst[0])))
a = (a for a, b in lst)
b = (b for a, b in lst)
c = zip(*lst)
print(iter(c) is iter(c))
# print(list(itertools.accumulate(lst, lambda x, y: (x[0] + y[0], x[1] + y[1]))))
# print(list(zip(itertools.accumulate(a), itertools.accumulate(b))))
print(list(c))
# print(list(zip(*lst)))
for x in c:
    print(x)

print('888')
c = [(0, 2, 4, 5), (0, 3, 3, 1)]
# itertools.starmap([(0, 2, 4, 5), (0, 3, 3, 1)])
# print(*lst
# print(list(zip(map(itertools.accumulate, zip(*lst)))))
# print((map(itertools.accumulate, zip(*lst))))
print(list(zip(*map(itertools.accumulate, c, (lambda x, y: x + y, lambda x, y: x - y)))))
a = list(zip(itertools.starmap(itertools.accumulate, [c])))
# print(list(itertools.accumulate([(0, 2, 4, 5), (0, 3, 3, 1)])))
# print(list(*map(itertools.accumulate, zip(*lst)))))
# for x in map(itertools.accumulate, c):
#     for y in x:
#         print(y)
# for x in a:
#     for y in x:
#         for z in y:
# #             print (z)
# import functools
# result = map(itertools.repeat, ('abe', 'cdu', 'iosadio'), (1, 3, 4))
# # print(list(*result))
# print(list(map(list, result)))
# print(list(map(lambda x, y: x if x > y else y if y > x else 0, (7, 2, 4), (2, 2, 5))))
# print(list('abe'))
# import operator
# vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
#             ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
#             ('Dodge', 'Charger'), ('Ford', 'GT')]
# s_vehicles = sorted(vehicles)
# print(s_vehicles)
# p = itertools.groupby(s_vehicles, key=operator.itemgetter(0))
# print([list(y) for x, y in p])

st = 'abbbcaa'
# st = list(st)
# print(st) ['a', 'b', 'b', 'b', 'c', 'a', 'a']
result = itertools.groupby(st)
for key, group in result:
    print(f'key is {key} , and the group is {list(group)}')
result = tuple((len(list(y)), x) for x, y in result)
print(result)

# c = itertools.groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, 1, ('persons', 'man', 'woman')])
# for x, y in c:
#     print(x, list(y))
lst = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), 'wombat', 'mongoose', 'malloo', 'camel']
for key, group in itertools.groupby(lst, lambda x: x[1]):
    print(key, list(group))
    # print()
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),
               'wombat', 'mongoose', 'malloo', 'camel']
c = itertools.groupby(list_things, key=lambda x: x[1])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)
print(list(itertools.product('ab', 'cd', 'ef')))


ls = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat']
result = itertools.combinations(ls, 2)
print([' '.join(n) for n in result])
result = map(pow, (1, 4), (2, 4))
print(list(result))
result = itertools.starmap(pow, [(1, 2), (4, 4)])
print(list(result))
result = map(pow, [(1, 2), (4, 4)])
# print(list(result))
for x in range(10)[::-1]:
    print(x)

# print(list(itertools.zip_longest('abbcs','wowowwowowow',fillvalue='zipz')))
result = itertools.zip_longest('abxscdcas', 'ssu', fillvalue="no match")
print(list(result))
c = [(0, 2, 4, 5), (0, 3, 3, 1)]
# itertools.starmap([(0, 2, 4, 5), (0, 3, 3, 1)])
# print(*lst
# print(list(zip(map(itertools.accumulate, zip(*lst)))))
# print((map(itertools.accumulate, zip(*lst))))
result = map(itertools.accumulate, c)
result = itertools.chain.from_iterable(result)
print(list(result))
result = [iter(range(9))]
for x in result:
    print(x)
w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
x = range(1, 13)
# print (list(zip(x, x)))
# e = int(len(w) / 2)

# print(list(zip(* ([iter(range(1, 13))] * 3))))
# # zip(*[iter(s)] * n)
# a = range(20)
# for x in a:
#     print(x)
# for x in a:
#     print(x)
print([iter(x)] * 3)
print([iter(x), iter(x), iter(x)])
# print([iter(x) + iter(x) + iter(x)])
print()
print([iter(w)] * 3)
print([iter(w), iter(w), iter(w)])
# print([iter(w), iter(w), iter(w)])
# print([iter(w), iter(w), iter(w), iter(w)])

# print([iter(w) + iter(w) + iter(w)])
lst = [1, ['3232'], 'b']
lst_2 = [1, ['3232'], 'b']
print(lst is lst_2)
print([id(x) for x in lst * 2])
a = ['3232']
b = ['3232']
print(a is b)
w = iter(a)
print(iter(w) == iter(w))

from collections import deque
m = 'ABCDEFG'
z = deque(m, None)
print(z)

a = iter(m)
# for x in a:
#     pass
# print(next(a, 'w'))
print(list(itertools.islice(a, 3, 3)))
print(next(a))
b = itertools.count()
c = itertools.islice(b, 2, 2)
print(next(b))
# def how_long(iterable):
#     return len(iterable)


# print(how_long(iter(m)))
def prepend(value, iterable):
    return itertools.chain([value], iterable)


b = itertools.islice(itertools.count(), 10, 50)
a = itertools.islice(b, 20)
# b = itertools.islice(a, 7, None)
# print(len(b))
# for x in b:
#     print(x)
# from itertools import tail
# for x in a:
#     print(x)
print('ww')
# for x in b:
#     print(x)
m = []
n = iter(m)
q = itertools.groupby(n)
for x in q:
    if x:
        print('t')
    else:
        print('f')

z = map(lambda x, u: x + u, (1, 2, 3), (4,))
for x in z:
    print(x)
a = ([1, 2, 3])
print(list(iter(a)) == list(iter(a)))
a = itertools.islice(itertools.count(), 20)


def consume(iterator, n):
    next(itertools.islice(iterator, n, n), None)


def nth(iterator, n):
    return next(itertools.islice(iterator, n, None), None)


# consume(a, 6)
# print(next(a))
print(nth(a, 66))
