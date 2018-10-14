# Maxwell Richard Tamer-Mahoney ID #: 201804029
# n-sided polygons with side colors picked from a list

import turtle
import random

def cpolygon(n, size, colors):
    turtle.width(5)
    for i in range(1, n + 1):
        turtle.color(colors[random.randrange(0, len(colors))])
        turtle.forward(size)
        turtle.left(360/n)
    turtle.done()

cpolygon(8, 200, ['black', 'blue', 'red', 'orange', 'green', 'grey'])
