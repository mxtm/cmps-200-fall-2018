# Maxwell Richard Tamer-Mahoney ID #: 201804029

import turtle

def square(x, y, d):
    # Go to the x, y specified center point and raise the pen so we can get to
    # the side still
    turtle.penup()
    turtle.goto(x, y)
    # Move to the side we need to start drawing
    turtle.forward(d / 2)
    # Start heading north
    turtle.left(90)
    # Pen back down
    turtle.pendown()

    # Half of the right side
    turtle.forward(d / 2)
    # Turn to begin the top side
    turtle.left(90)
    # Draw three sides normally
    for i in range(3):
        turtle.forward(d)
        turtle.left(90)
    # Finish the other half of the right side
    turtle.forward(d / 2)

def squares(x, y, d, n):
    # If n == 0, we do nothing.
    if n == 0:
        return None
    # If n == 1, just pass everything straight to the square function.
    elif n == 1:
        square(x, y, d)
    else:
        # Otherwise, first draw our main square
        squares(x, y, d, n - 1)
        # And squares centered on the corners
        squares(x - d / 2, y + d / 2, d / 2, n - 1)
        squares(x + d / 2, y + d / 2, d / 2, n - 1)
        squares(x - d / 2, y - d / 2, d / 2, n - 1)
        squares(x + d / 2, y - d / 2, d / 2, n - 1)
        # All the way through this we're calling with n changed to n - 1 so
        # that we reach our base case and keep drawing any necessary smaller
        # squares to make up a more complex design

squares(0, 0, 200, 3)
turtle.done()
