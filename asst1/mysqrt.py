# Maxwell Richard Tamer Mahoney ID #: 201804029
# A relatively bad algorithm to calculate square roots
# Takes the number to find the sqrt of as CLI arg input

import sys
#import math (if cheating)

#def cheating_closest_square(n):
#    lower_square = int(math.sqrt(n)) 
#    higher_square = lower_square + 1
#    if n - lower_square ** 2 < higher_square ** 2 - n:
#        return lower_square
#    else:
#        return higher_square

def closest_square(n):
    higher_square = 1;
    while higher_square ** 2 < n:
        higher_square += 1
    lower_square = higher_square - 1
    if n - lower_square ** 2 < higher_square ** 2 - n:
        return lower_square
    else:
        return higher_square

def perfect_estimate(n, estimate=None):
    if estimate is None:
        estimate = closest_square(n)
    new_estimate = (n / estimate + estimate) / 2
    if new_estimate ** 2 - n > 0.00000001:
        return perfect_estimate(n, new_estimate)
    else:
        return new_estimate

print(perfect_estimate(int(sys.argv[1])))
