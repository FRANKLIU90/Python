import math


class Circle:
    version = '0.1'

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return math.pi * 2 * self.radius

    def area(self):
        return self.__perimeter()**2 / (4 * math.pi)

    __perimeter = perimeter

    @property
    def radius(self):
        return self.diameter

    @radius.setter
    def radius(self, radius):
        diameter = 2 * radius
        self.diameter = diameter


class Tire(Circle):
    def perimeter(self):
        return super().perimeter() * 2
        # return Circle.perimeter(self) * 2


c = Circle(3)
t = Tire(2)
print(c.perimeter())
print(t.perimeter())
print(c.area())
print(c.__dict__)
