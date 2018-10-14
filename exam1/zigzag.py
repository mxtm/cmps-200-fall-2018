import sys, turtle

n = int(sys.argv[1])
d = int(sys.argv[2])
theta = int(sys.argv[3])

def zigzag(n, d, theta):
    # (1)
    turtle.left(theta)
    turtle.forward(d)

    # (2)
    turtle.right(2 * theta)
    turtle.forward(2 * d)

    # (3)
    turtle.left(2 * theta)
    turtle.forward(d)

    # (4)
    turtle.right(theta)

def zzsquare(n, d, theta):
    for i in range(4):
        zigzag(n, d, theta)
        turtle.right(90)

zzsquare(n, d, theta)

turtle.done()
