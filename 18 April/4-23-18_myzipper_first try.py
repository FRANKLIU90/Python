import itertools

# basiclly i am try to solve "zip_longest _without filled values "
# https://stackoverflow.com/questions/38054593/zip-longest-without-fillvalue
# but this wont work , because i def a new next, make it pass StopIteraton.but the problem is my_Next will still return None when it hit the StopIteration and pass. so bacislly this is a zip _longest.
# that means in order to make a true   'zip_longest _without filled
# values', I have to put is in the loop and when it hit the StopIteration
# just continue the loop:)


def my_next(iterator):
    try:
        return next(iterator)
    except StopIteration:
        pass


def zipper(*iterables):
    # this was iterators_map = map(iter, iterables) , no tuple ,and it doesnt
    # work! reason   'map is a iterator too:)' see down iter(map) is iter(map)
    iterators_map = tuple(map(iter, iterables))

    # print(next(iterators_map))
    result = tuple(map(my_next, iterators_map))
    while result:
        yield result
        # yield iterators_map
        result = tuple(map(my_next, iterators_map))
        # yield result


lists = [(11, 12, 13),
         (21, 22, 23, 24),
         (31, 32),
         (41, 42, 43, 44)]
result = zipper(*lists)
print(next(result))
# print(type(next(result)))
# print(x)
print(next(result))
# print(next(result))
print(next(result))
print(next(result))
print(next(result))
#
#


# ##########so map is a iterator too:)
z = map(iter, [(1, 3), (4, 6), (7, 9)])
print(type(z))
print(iter(z) is iter(z))
for x in z:
    print(x)
print('duudududu')
for x in z:
    print(x)


b = [1, 2, 3]
print(iter(b) is iter(b))  # False
print(iter([1, 2, 3]) is iter([1, 2, 3]))  # False

a = iter([1, 2, 3])
print(iter(a) is iter(a))  # True
a = iter([1, 2, 3])
print(iter(iter([1, 2, 3])) is iter(iter([1, 2, 3])))  # False
