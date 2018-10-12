import math


class Circle:
    '''advance circle tech'''

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    @classmethod
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)


class Tire(Circle):
    def perimeter(self):
        return Circle.perimeter(self) * 1.25
