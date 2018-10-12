import itertools
from operator import itemgetter
from itertools import groupby
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

input = sorted(input, key=itemgetter(1))
result = groupby(input, key=itemgetter(1))
# for key, iteritems in result:
# print(key, '->', list(items))
print([{'key': key, 'items': [x for x, y in iteritems]}for key, iteritems in result])
# https://stackoverflow.com/questions/3749512/python-group-by


lst = [1, 5, 5]
# lst.sort()
result = groupby(lst)
for key, iteritems in result:
    print(key, '-->', list(iteritems))


# dic = {1: 2, 3: 4}
# print(2 in dic.values())
from itertools import repeat
a = repeat('abc', 2)
# print(list(a))
# print(len(a))
