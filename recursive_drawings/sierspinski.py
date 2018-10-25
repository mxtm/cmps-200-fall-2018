# Maxwell Richard Tamer-Mahoney ID #: 201804029

import turtle

def sierspinski(n, length=500):
    if n == 0:
        turtle.left(60)
        turtle.forward(length)

        turtle.right(120)
        turtle.forward(length)

        turtle.right(120)
        turtle.forward(length)

        turtle.right(180)

    else:
        sierspinski(n - 1, length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        sierspinski(n - 1, length / 2)
        turtle.left(60)
        turtle.back(length / 2)
        turtle.right(60)
        turtle.forward(length / 2)
        sierspinski(n - 1, length / 2)
        turtle.back(length / 2)

        

turtle.speed(0)
sierspinski(5)
turtle.done()
