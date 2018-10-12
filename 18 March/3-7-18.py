import csv
from functools import partial
from itertools import islice


def stop():
    raise StopIteration


with open('new_names.csv') as rf:
    reader = csv.reader(rf)
    next(reader)
    next(reader)
    names = [(line[0], line[1]) for line in reader]
names = ((first, last) if first != 'No Reward' else stop() for first, last in names)
# names = islice(names, ('No Reward', 'Description: (None for No Reward)'))
# No Reward,Description: (None for No Reward)
# print(names.index(('NO REWARD', 'DESCRIPTION: (NONE FOR NO REWARD)'))
# names = (x for x in names)
# names = iter(partial(next, iter(names)), ('No Reward', 'Description: (None for No Reward)'))
# for first, last in names:
#     print(first, last)
# print(names.index(('No Reward', 'Description: (None for No Reward)')))
# names = names[:30]
for first, last in names:
    print(first, last)
