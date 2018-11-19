# Maxwell Richard Tamer-Mahoney ID #: 201804029

from polygon import Polygon
import math

class Square(Polygon):
    def __init__(self, l):
        super(Square, self).__init__(4, l)

    def area(self):
        return self.s ** 2

class Triangle(Polygon):
    def __init__(self, l):
        super(Triangle, self).__init__(3, l)

    def area(self):
        return self.s ** 2 * math.sqrt(3) / 4

if __name__ == '__main__':
    s = Square(100)
    print(s.perimeter())
    print(s.area())

    t = Triangle(100)
    print(t.perimeter())
    print(t.area())
