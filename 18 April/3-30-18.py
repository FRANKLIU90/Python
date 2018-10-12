# import calendar
# import datetime
# balance = 5000
# payment = 500
# dpr = (12.99 * 0.01) / 365
# today = datetime.date.today()
# days_in_month = calendar.monthrange(today.year, today.month)[1]
# days_in_month = days_in_month - today.day
# payday = today + datetime.timedelta(days=days_in_month + 1)
# while balance > 0:
#     interest = balance * days_in_month * dpr
#     balance += interest
#     balance -= payment
#     if balance < 0:
#         balance = 0
#     print(payday, '---', f'{balance:.2f}')
#     days_in_month = calendar.monthrange(payday.year, payday.month)[1]
#     payday = payday + datetime.timedelta(days=days_in_month)
# import random
# nums = range(1, 101)
# random.shuffle(list(nums))
# print(list(nums))
# print(list(nums) is list(nums))

# import itertools
# nums = sorted(nums, key=lambda x: x // 3)
# results = itertools.groupby(nums, lambda x: x // 3)
# for x, y in results:
#     print(x, list(y))

# from collections import namedtuple
# colors = namedtuple('colors', ['red', 'green', 'blue'])

# a = colors(255, 254, 0)
# print(a)
# print(blind_in
# import sys
# # print(sys.path)
# import itertools
# # a=count()
# b = itertools.islice(itertools.count(), 10)

# a = reversed(b)
# print(a)


# m = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# # print "dict['Name']: ", dict['Name']
# print({a: m[a] for a in sorted(m)})
# print({a: b for a, b in sorted(m.items())})
# from operator import attrgetter, itemgetter, methodcaller
# from functools import partial
# with open('*3-12-18-classOPP.py') as f:

#     print(''.join(list(iter(partial(f.read, 20), ''))))

# from functools import partial
# with open('/Users/frankyoung/Downloads/638068528.jpg', 'rb') as rf:

#     with open('my_my.jpg', 'wb') as wf:
#         for line in rf:

#             wf.write(line)
# x = str()
# print(x)
a = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
words = ['sight', 'It', 'first', 'love', 'was', 'at']
# ist = sorted(ist, key=len)
# result = {}
# for num in ist:
#     key = len(num)
#     result[key] = result.get(key, []) + [num]
# print(result)

# import itertools
# # ist = sorted(ist, key=len)
# result = itertools.groupby(ist, len)
# for x, y in result:
#     print(x, list(y))
# result = {}
# for word in words:
#     key = len(word)
#     # result[1].append(1)
#     result[key] = result.get(key, []) + [word]
# print(result)
# from collections import defaultdict
# result = defaultdict(list)
# # for x in range(10):
# #     result[x]
# # print(result)
# for word in words:
#     key = len(word)
#     result[key] += [word]

# print(result)
# doctest.testmod()
# from collections import namedtuple
# color = namedtuple('color', ['red', 'blue', 'green'])
# a = color(234, 435, 4)
# print(a)
import os
print(os.getcwd())
