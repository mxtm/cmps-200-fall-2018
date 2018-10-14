# Maxwell Richard Tamer Mahoney ID #: 201804029
# Accepts number of sides and the length of each side, drawing an n-sided
# polygon.
import sys, turtle

sides = int(sys.argv[1])
sideLength = int(sys.argv[2])

for i in range(sides):
    turtle.forward(sideLength)
    turtle.left(360 / sides)

turtle.done()
