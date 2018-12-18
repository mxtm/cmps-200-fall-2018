# Maxwell Richard Tamer-Mahoney ID #: 201804029

import math

class Disk:
    def __init__(self, radius, x=0.0, y=0.0):
        self.__radius = float(radius)
        self.__x = float(x)
        self.__y = float(y)
    def radius(self):
        return self.__radius
    def x(self):
        return self.__x
    def y(self):
        return self.__y
    def distance_between_center(self, other):
        return math.sqrt((other.x() - self.x()) ** 2 + (other.y() - self.y()) ** 2)
    def intersect(self, other):
        return self.distance_between_center(other) < self.radius() + other.radius()
    def leftmost_x(self):
        return self.x() - self.radius()
    def __str__(self):
        return '<Disk of radius {} at ({}, {})>'.format(self.radius(), self.x(), self.y())
    def __lt__(self, other):
        return self.leftmost_x() < other.leftmost_x()

if __name__ == '__main__':
    d1 = Disk(1, 2, 4)
    d2 = Disk(0.5)
    print(d1)
    print(d1.leftmost_x(), d2.leftmost_x())
    print(d1 < d2)
