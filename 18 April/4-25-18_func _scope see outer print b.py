from functools import wraps


def counter(my_func):

    # @wraps(my_func)
    def wrapper(*args, **kwargs):
        # wrapper.count = 0

        wrapper.count += 1
        # print(wrapper.count)
        return my_func(*args, **kwargs)
    wrapper.count = 0
    wrapper.c = 9
    return wrapper


@counter
def add_2(x):
    return x + 2


# z = map(add_2, range(5))
# print(list(z))
w = add_2(2)
print(add_2.count)
print(add_2.c)

# w = 8


# def fu():
#     print (w)


# # a = fu
# w = 0
# # a()
# fu()
def outer():
    b = 0

    def inner():
        print(b)  # 1
        print(b)  # 1
    b = 1
    return inner


outer()()


# def outer():
#     a = 0

#     def inner():
#         if a == 0:
#             a = 1
#         print(a)
#         a = 2
#         print(a)
#     return inner


outer()()
# https://youtu.be/E9wS6LdXM8Y 8:30 9:36 it is the value when we call,not define. def does analyze our code and determinds scope of each variable
wwwee = 0


def m(x):
    # print(wwwee)  # can not access and reassign
    wwwee = x
    print(wwwee)


print(wwwee)

m(4)


def tallest_building():
    buildings = {'Burj Khalifa': 828,
                 'Shanghai Tower': 632,
                 'Abraj Al-Bait': 601}

    def height(name):
        return buildings[name]

    return max(buildings.keys(), key=height)


a = tallest_building()
print(a)


for x in range(3):
    def z(y):
        return x * y
z = [lambda x: i * x for i in range(5)]
for multiplier in z:
    print (multiplier(2))
