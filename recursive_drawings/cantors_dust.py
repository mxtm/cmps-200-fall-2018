# Maxwell Richard Tamer-Mahoney ID #: 201804029

import turtle

def cantors_dust(n, length=400):
    if n == 0:
        turtle.forward(length)
    else:
        cantors_dust(n - 1, length / 3)
        turtle.penup()
        turtle.forward(length / 3)
        turtle.pendown()
        cantors_dust(n - 1, length / 3)

turtle.width(10)
cantors_dust(3)
turtle.done()
