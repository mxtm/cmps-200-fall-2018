# Maxwell Richard Tamer-Mahoney ID #: 201804029

import sys, random
from fraction import Fraction

n = int(sys.argv[1])

randomFractions = [Fraction(random.randint(0, 20), random.randint(1, 20)) for i in range(n)]

randomFractions.sort()

[print(x) for x in randomFractions]
