import math


class Circle:
    print('class circle')

    def __init__(self, radius):
        self.radius = radius
        print('init circle')

    def perimeter(self):
        return 4 * self.radius

    def area(self):
        a = self.__perimeter()
        s = (a / 4)**2
        return s
    __perimeter = perimeter

    def pint(self):
        print('jiji')
    _pint = pint


class Tire(Circle):
    def perimeter(self):
        return Circle.perimeter(self) * 2

    # __perimeter = perimeter


c_1 = Circle(2)
c_2 = Circle(4)
# c_1._pint()

# print(dir(c_1))
# print(dir(Circle))
# print('+++++')
# print(dir(Tire))

t_1 = Tire(3)
# print(t_1.perimeter())
# print(t_1._Tire__perimeter())
# print(t_1.area())
print(vars(c_1))
d = {'radius': 2}
print({b: a for a, b in d.items()})
# print(class(t1).__name__)
