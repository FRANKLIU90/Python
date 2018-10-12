from bs4 import BeautifulSoup
d = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
d = {a: b for b, a in d.items()}
# print(d)
# for x in list(d):
#     if x < 10:
#         del d[x]
# print(d)
# print(list(d))
# for x in d:
#     print({x}, end='')
# s = '{1} {2} {3}{4}{5}'.format(**d)
# c=d = {1: 'D', 2: 'B'}
# print('{1} {2}')

# print('{D}{B}{E}{A}'.format(**d))
d = [('b', 23), ('d', 17), ('c', 5), ('a', 2), ('e', 1)]

# from operator import itemgetter
# print(sorted(d, key=d.__getitem__(1)))
import random
# a = random.randint(1, 10)
# for i in range(10):
# print(random.randint(1, 10), end=',')

z = [10, 2, 8, 2, 3, 1, 9, 6, 6, 9]
print(z)

# from collections import Counter
# z = Counter(z)
# print(z)
# print(z.most_common(2))
# print(list(z.elements()))
# z = [10, 2, 8,9]
# print('{:07,},{:03},{:.3f},{}'.format(*z))
