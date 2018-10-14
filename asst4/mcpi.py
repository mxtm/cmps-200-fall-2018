# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Implementation of a Monte Carlo simulation to estimate pi

import sys
import random

n = sys.argv[1]

def mc_pi_estimate(n):
    inTheCircle = 0
    for i in range(n):
        myPointX = random.uniform(0, 1)
        myPointY = random.uniform(0, 1)
        if myPointX ** 2 + myPointY ** 2 <= 1:
            inTheCircle += 1
    return inTheCircle / n * 4

print(mc_pi_estimate(int(n)))

""" As the number of generated points (n) checked if they are in the circle
increases, the returned value gets closer and closer to pi, as of course, the
only way to get the "actual" value would be infinitely many points.
"""
