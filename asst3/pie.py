import math
import turtle

def draw_pie(n, r):
    """Draws a pie divided into radial segments.
    n: number of segments
    r: length of the radial spokes
    """
    for i in range(n):
        isosceles(r, 360/n/2)
        turtle.left(360/n)


def isosceles(r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    r: length of the equal legs
    angle: half of peak angle, in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    turtle.right(angle)
    turtle.forward(r)
    turtle.left(90+angle)
    turtle.forward(2*y)
    turtle.left(90+angle)
    turtle.forward(r)
    turtle.left(180-angle)

# draw a hexagonal (6-sided) pie
size = 100
draw_pie(6, size)

# wait for user to close the window
turtle.done()
