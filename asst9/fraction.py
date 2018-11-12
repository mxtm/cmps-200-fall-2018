class Fraction:
    """A class that represents a fraction."""
    def __init__(self, numerator, denominator=1):
        """Constructs an instance of the class with the specified numerator and
        denominator. If the denominator is not specified, it defaults to 1."""
        self.numerator = numerator
        self.denominator = denominator
    def __mul__(self, other):
        """Returns a new instance of the class that is the multiplied version
        of two fractions, simplified."""
        result = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        result.simplify()
        return result

    def __add__(self, other):
        """Returns a new instance of the class that is two fractions added,
        simplified."""
        result = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        result.simplify()
        return result

    def __eq__(self, other):
        """Returns a boolean indicating if two instances have an equal value."""
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __lt__(self, other):
        """Returns a boolean indicating if this instance is less than
        another."""
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __str__(self):
        """Returns a string representation of the instance."""
        return '{}/{}'.format(self.numerator, self.denominator)

    def gcd(x, y):
        """Calculate the greatest common divisor of x and y, in order to
        simplify an instance."""
        while x != y:
            if x > y:
                x = x - y
            elif x < y:
                y = y -x
        return x

    def simplify(self):
        """Simplifies an instance by calculating the greatest common divisor
        and dividing the numerator and denominator by the GCD."""
        divisor = Fraction.gcd(self.numerator, self.denominator)
        self.numerator /= divisor
        self.denominator /= divisor

if __name__ == '__main__':
    x = Fraction(1, 2)
    y = Fraction(1, 2)
    z = x * y
    print('Is 1/2 * 1/2 less than 1/2?:', z < x and z < y)
    print('Is 1/2 + 1/2 equal to 1/1?:', x + y == Fraction(1, 1))
    print('String representations of my fractions', x, y, z)
    a = Fraction(4, 8)
    b = Fraction(2, 8)
    print('Result of 4/8 + 2/8:', a + b)
    c = Fraction(1, 10)
    d = Fraction(2, 10)
    print('Result of 1/10 * 2/10:', c * d)
