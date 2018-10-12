from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.email = f'{radius}'

    def perimeter(self):
        return 2 * pi * self.radius

    a = perimeter
    # def a(self):
    #     return 2 * pi * self.radius

    @property
    def email(self):
        return f'{sefl.radius}'

    @email.setter
    def email(self, address):
        self.email = f'{address}'

    def b(self):
        return self.perimeter()


class Tire(Circle):
    def perimeter(self):
        return Circle.perimeter(self) * 2

    a = perimeter


c_1 = Circle(2)
t_1 = Tire(2)
# print(dir(Tire))
print(c_1.a())
print(c_1.b())
print(c_1.perimeter())
print(t_1.a())
print(t_1.b())
print(t_1.perimeter())
print(Circle.a)
print(Circle.perimeter)
print(Tire.a)
print(Tire.perimeter)
