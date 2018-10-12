def mf(a, b):
    print(f'{a}{b}')


mf('a', 'b')
# mf(a='a','b') #SyntaxError: positional argument follows keyword argument
# mf('a', c='b')#TypeError: mf() got an unexpected keyword argument 'c'
# mf('a', a='b')#TypeError: mf() got multiple values for argument 'a'

mf('a', b='b')
mf(a='a', b='b')
# print(.1 + .7)

import math


class Circle:
    '''Advance Circle Tech'''
    # __slots__ = ['diameter']
    print('here def the class')
    version_number = '0.1'

    def __init__(self, radius):
        print('Circle__init__ runs')
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = 2 * radius

    def area(self):
        return math.pi * (self.__perimeter() / (2.0 * math.pi))**2

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    def __repr__(self):
        return '{}{}'.format(self.__class__.__name__, tuple(vars(self).values()))
    __perimeter = perimeter

    @classmethod
    def from_bbd(cls, bbd):
        raduis = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)


class Tire(Circle):
    def perimeter(self):
        return super().perimeter() * 2
        # return Circle.perimeter(self) * 2


# print(Circle.__doc__)
c_1 = Circle(1)
print(c_1.perimeter())
print(c_1.area())

t_1 = Tire(1)
print(t_1.perimeter())
print(t_1.area())
print(t_1)
cuts = [0.1, 0.7, 0.8]
rubber_sheets = [Circle(r) for r in cuts]
for rubber_sheet in rubber_sheets:
    print(rubber_sheet)
r_1 = Circle(0.1,)
print(r_1.area())
# print(dict.fromkeys(['john','frank']))
# print(dict.fromkeys('john'))
