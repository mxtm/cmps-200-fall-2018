# Maxwell Richard Tamer-Mahoney ID #: 201804029

from segment import Segment

class Wsegment(Segment):
    def __init__(self, a, aWeight, b = None, bWeight = None):
        super().__init__(a, b)
        if bWeight == None:
            self.__leftWeight = 1
            self.__rightWeight = aWeight
        else:
            self.__leftWeight = aWeight
            self.__rightWeight = bWeight
        if self.leftWeight() < 0 or self.rightWeight() < 0:
            raise Exception('Weights must be positive!')

    def leftWeight(self):
        return self.__leftWeight

    def rightWeight(self):
        return self.__rightWeight

    def __str__(self):
        return '[{} (weight: {}) -- {} (weight: {})]'.format(self.left(), self.leftWeight(), self.right(), self.rightWeight())

    def centroid(self):
        return (self.left() * self.leftWeight() + self.right() * self.rightWeight()) / (self.leftWeight() + self.rightWeight())

    def __lt__(self, other):
        return self.centroid() < other.centroid()

"""
I don't get why this should be a function, but okay fine I'll do it
"""
def test():
    a = Wsegment(1, 2)
    b = Wsegment(1, 2, 3, 4)
    print(a, b)
    print(a.centroid(), b.centroid())
    try:
        c = Wsegment(1, -1, 2, 3)
    except Exception:
        print('An exception was thrown and I caught it!')
    print(a < b)

if __name__ == '__main__':
    test()
