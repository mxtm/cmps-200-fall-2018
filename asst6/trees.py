# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Recursive tree

import turtle

def tree(n, length=100, width=20):
    if length == 100:
        turtle.forward(length)
    turtle.width(width * (1/2))
    turtle.left(60)
    turtle.forward(length * (2/3))
    if n > 1:
        tree(n - 1, length / 2, width * (1 / 3))
    turtle.width(width * (1/2))
    turtle.back(length * (2/3))
    turtle.right(60)
    turtle.forward(length * (1/3))
    if n > 1:
        tree(n - 1, length / 2, width * (1 / 3))
    turtle.width(width * (1/2))
    turtle.back(length * (1/3))
    turtle.right(50)
    turtle.forward(length * (2/3))
    if n > 1:
        tree(n - 1, length / 2, width * (1 / 3))
    turtle.width(width * (1/2))
    turtle.back(length * (2/3))
    turtle.left(50)

turtle.hideturtle()
turtle.tracer(0)
turtle.width(10)
turtle.setheading(90) 
tree(8)
turtle.done()
