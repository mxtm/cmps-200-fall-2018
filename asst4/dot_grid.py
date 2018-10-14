# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Dot grids but shorter

import turtle
import random

def drawSquare(sideLength):
    for i in range(4):
        turtle.forward(sideLength)
        turtle.right(90)

def drawRowSquares(n, sideLength):
    turtle.pendown()
    for i in range(n):
        drawSquare(sideLength)
        turtle.setx(turtle.xcor() + sideLength)
    
def drawGridSquares(n, sideLength):
    for i in range(n):
        drawRowSquares(n, sideLength)
        turtle.penup()
        turtle.goto(0, turtle.ycor() + sideLength)

def drawGridDots(n, sideLength, colors=None):
    for i in range(n):
        for j in range(n):
            turtle.goto(sideLength / 2 + sideLength * j,
                        sideLength * i - sideLength * 0.5)
            alternateBlackAndRedDots(j) if colors == None else pickRandomDot(colors)

def alternateBlackAndRedDots(j):
    turtle.dot(40, 'black') if j % 2 == 0 else turtle.dot(40, 'red')

def pickRandomDot(colors):
    turtle.dot(40, colors[random.randrange(0, len(colors))])

def dot_grid(n, length):
    drawGridSquares(n, length)
    drawGridDots(n, length)

def cdot_grid(n, length, colors):
    drawGridSquares(n, length)
    drawGridDots(n, length, colors)
    
if __name__ == "__main__":
    turtle.speed(0)
    cdot_grid(4, 100, ['black', 'blue', 'purple', 'pink', 'yellow', 'red'])
    #dot_grid(4, 100)
    turtle.done()
