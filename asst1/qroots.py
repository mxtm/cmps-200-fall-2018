# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Find the (real) roots of a quadratic
# a, b, c given as CLI arguments

import sys, math

a, b, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    roots = [(-b + math.sqrt(discriminant))/(2*a), (-b - math.sqrt(discriminant))/(2*a)]
    print(str(roots[0]) + ' ' + str(roots[1]))
    
else:
    print("No real roots exist.")
