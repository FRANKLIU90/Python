import inspect


def a(b):
    def c(d):
        print(c.__code__.co_freevars)
        print(c.__code__.co_names)
        print(c.__code__.co_freevars)
        # print('z')
        pass
    return c


# print(inspect.getargspec(a))
z = a(2)
print(a.__code__.co_varnames)
print(a.__code__.co_names)
print(a.__code__.co_freevars)
# a(1)(2)
print('ww')
print(z.__code__.co_varnames)

print(z.__code__.co_names)
print(z.__code__.co_freevars)
z(6)

formatters = {}
colors = ['red', 'green', 'blue']
for color in colors:
    def in_color(s):
        return ('<span style="color:' +
                color + '">' + s + '</span>')
    formatters[color] = in_color


print(formatters['green']('hello'))
i = 0
z = [i + 1 for i in range(10)]
print(i)


def append_to(element, to=[]):
    to.append(element)
    return to


my_list = append_to(12)
print(my_list)

my_other_list = append_to(42, to=[1, ])
print(my_other_list)


def create_multipliers():
    multipliers = []

    i = 0

    def multiplier_1(x):
        return i * x
    multipliers.append(multiplier_1)

    i = 1

    def multiplier_2(x):
        return i * x
    multipliers.append(multiplier_2)

    return multipliers


z = create_multipliers()

for x in z:
    print(x)
# def create_multipliers():
#     return [partial(mul, i) for i in range(5)]
result = [lambda x, i=i: i * x for i in range(5)]
for x in result:
    print(x(2))
