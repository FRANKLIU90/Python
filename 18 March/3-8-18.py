from functools import partial
import itertools


def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, b + a


def stop():
    raise StopIteration


results = (x if x < 4000000 else stop() for x in fib() if x % 2 == 0)
words = results

now, later = itertools.tee(words)
for x in now:
    print(x)
for x in later:
    print(x)
print('a')
for x in now:
    print(x)


# from itertools import islice
# from itertools import count
# a = count(4000000)
# result = islice(fib(), a)
# for x in result:
#     print(x)


# bad_cred = stop()

# count = itertools.count()
# results = (x if x < 200 else stop() for x in count)
# print(list(results))
# for x in iter(partial(next, fib()), ):
#     print(x)

# for x in fib():
#     print(x)
# results = (x for x in fib() if x % 2 == 0)
# for result in results:
#     print(result)
# # def mygen():
#     for i in range(100):
#         if i == 10:
#             break
#         yield i


# for x in mygen():
#     print(x)

# nums = list(range(1, 21))
# result = (x if x % 2 else 'a' for x in nums)
# print(list(result))
# l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
# [x+1 if  for x in l]
