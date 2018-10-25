# Maxwell Richard Tamer-Mahoney ID #: 201804029

import turtle

def square_snowflake(n, side=200, filled=True):
    if not filled:
        turtle.penup()
        turtle.forward(side)
        turtle.pendown()
    else:
        if n == 0:
            turtle.begin_fill()
            turtle.forward(side)
            turtle.right(90)
            turtle.forward(side)
            turtle.right(90)
            turtle.forward(side)
            turtle.right(90)
            turtle.forward(side)
            turtle.right(90)
            turtle.end_fill()
            turtle.forward(side)
        else:
            square_snowflake(n - 1, side / 3)
            square_snowflake(n - 1, side / 3, False)
            square_snowflake(n - 1, side / 3)

            turtle.penup()
            turtle.right(90)
            turtle.forward(side / 3)
            turtle.left(90)
            turtle.back(side)
            turtle.pendown()

            square_snowflake(n - 1, side / 3, False)
            square_snowflake(n - 1, side / 3)
            square_snowflake(n - 1, side / 3, False)

            turtle.penup()
            turtle.right(90)
            turtle.forward(side / 3)
            turtle.left(90)
            turtle.back(side)
            turtle.pendown()

            square_snowflake(n - 1, side / 3)
            square_snowflake(n - 1, side / 3, False)
            square_snowflake(n - 1, side / 3)

            turtle.penup()
            turtle.left(90)
            turtle.forward(side * (2 / 3))
            turtle.right(90)
            turtle.pendown()


turtle.tracer(0)
#turtle.speed(0)
square_snowflake(4)
turtle.done()
