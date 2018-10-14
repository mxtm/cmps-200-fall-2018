# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Cute dot grids

import turtle
import random

def dot_grid(n, length):
    drawBaseOfGrid(n, length)
    returnToGridStart(n, length)
    dotTheGrid(n, length)

def cdot_grid(n, length, colors):
    drawBaseOfGrid(n, length)
    returnToGridStart(n, length)
    dotTheGrid(n, length, colors)

def returnToGridStart(n, length):
    turtle.penup()
    turtle.back(length)
    turtle.left(90)
    turtle.forward(length * n)
    turtle.right(90)

def toNextRow(n, length):
    turtle.penup()
    turtle.back(length * n)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)

def drawBaseOfGrid(n, length):
    for i in range(n):
        for j in range(n):
            for k in range(4):
                turtle.right(90)
                turtle.forward(length)
            turtle.penup()
            turtle.forward(length)
            turtle.pendown()
        toNextRow(n, length)
        turtle.pendown()

def alternateBlackAndRed(j):
    if j % 2 == 0:
        turtle.dot(40, 'black')
    else:
        turtle.dot(40, 'red')

def pickRandomDot(colors):
    turtle.dot(40, colors[random.randrange(0, len(colors))])

def dotTheGrid(n, length, colors=None):
    turtle.penup()
    turtle.right(90) 
    turtle.forward(length / 2)
    turtle.left(90)
    for i in range(n):
        for j in range(n):
            turtle.forward(length / 2)
            if colors == None:
                alternateBlackAndRed(j)
            else:
                pickRandomDot(colors)
            turtle.forward(length / 2)
        toNextRow(n, length)

turtle.speed(0)
cdot_grid(4, 100, ['black', 'blue', 'purple', 'pink', 'yellow', 'red'])
#dot_grid(4, 100)
turtle.done()
