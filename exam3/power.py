# Maxwell Richard Tamer-Mahoney ID #: 201804029

from polynom import Polynom

def power1(p, d):
    # A fun iterative version of raising a polynomial to a power.
    result = p
    # We use d - 2 instead of d - 1 because we are initializing our result to p already
    for i in range(d - 2):
        # Multiply result variable by itself!
        result *= result
    return result

def power2(p, d):
    # A more fun recursive version of raising a polynomial to a power.
    if d == 1:
        # A polynomial raised to power 1 is itself
        return p
    else:
        # Otherwise, get the polynomial to the desired power / 2
        x = power2(p, d / 2)
        # Multiply this by itself to get the desired result
        return x * x

p1 = Polynom([(1, 0), (1, 1)])
print(p1)
print(power1(p1, 4))
print(power2(p1, 4))
