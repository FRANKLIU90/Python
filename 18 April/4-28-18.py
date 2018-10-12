colors = ['red', 'green', 'red', 'blue', 'green', 'red']
from collections import Counter
result = Counter()
for color in colors:
    result[color] += 1
print(result)
print(result.most_common)


def x():
    print('hello')
    yield
    print('there')


z = x()
next(z)
next(z)
