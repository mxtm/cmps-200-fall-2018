# Maxwell Richard Tamer-Mahoney ID #: 201804029

import math

class Polygon:
    """A class that represents an n-sided polygon."""
    def __init__(self, n, s):
        """Constructs an instance of the class with n sides and an s length of
        each side."""
        self.n = n
        self.s = s
    def perimeter(self):
        """Returns the perimeter of the instance."""
        return self.n * self.s
    def area(self):
        """Returns the area of the instance."""
        return self.s ** 2 * self.n / (4 * math.tan(math.pi / self.n))

if __name__ == '__main__':
    square = Polygon(4, 10)
    print(square.perimeter(), square.area())
