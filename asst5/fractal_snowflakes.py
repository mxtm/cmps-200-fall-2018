# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Fractal snowflakes

import turtle

def fractal(order, length):
    if order == 0:
        turtle.forward(length)
    else:
        fractal(order - 1, length / 3)
        turtle.left(60)
        fractal(order - 1, length / 3)
        turtle.right(120)
        fractal(order - 1, length / 3)
        turtle.left(60)
        fractal(order - 1, length / 3)

def snowflake(order, length):
    fractal(order, length)
    turtle.right(120)
    fractal(order, length)
    turtle.right(120)
    fractal(order, length)

"""turtle.penup()
turtle.goto(-800, 0)
turtle.pendown()
"""
turtle.speed(0)
#snowflake(5, 400)
fractal(5, 1000)
turtle.done()
