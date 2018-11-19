# Maxwell Richard Tamer-Mahoney ID #: 201804029

class Segment:
    def __init__(self, a, b=None):
        if b == None:
            self.__left = 0
            self.__right = float(a)
        else:
            self.__left = float(a)
            self.__right = float(b)
        if self.left() > self.right():
            raise Exception('The left must be before the right!')

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def mid_point(self):
        return (self.left() + self.right()) / 2

    def contains(self, x):
        return self.left() <= x <= self.right() 

    def overlaps(self, other):
        return self.contains(other.left()) or self.contains(other.right())

    def __lt__(self, other):
        return self.mid_point() < other.mid_point()

    def __str__(self):
        return '[{} -- {}]'.format(self.left(), self.right())

if __name__ == '__main__':
    segA = Segment(10)
    segB = Segment(8, 18)
    print(segA, segB)
    print(segA.overlaps(segB))
    print(segB.overlaps(segA))
    print(segA.mid_point())
    print(segB.mid_point())
    print(segA.contains(6))
    print(segA.contains(10.01))
    print(segB.contains(10.03))
    print(segB.contains(7.99))
    Segment(-1)
