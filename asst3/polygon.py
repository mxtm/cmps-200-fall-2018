# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Draw n-sided alternating color polygons
import turtle

def cpolygon(n, size):
    for i in range(1, n + 1):
        turtle.forward(size)
        turtle.left(360/n)
        if i % 2 == 0:
            turtle.color('black')
        else:
            turtle.color('red')
    turtle.done()

cpolygon(4, 100)
