# Maxwell Richard Tamer-Mahoney ID #: 201804029
# A random walk in Manhattan

import random

def goNorth(current_position):
    current_position[1] += 1

def goEast(current_position):
    current_position[0] += 1

def goSouth(current_position):
    current_position[1] -= 1

def goWest(current_position):
    current_position[0] -= 1

def manhattan(x, y):
    grid = [[0 for i in range(y)] for j in range(x)]
    current_position = [len(grid) // 2, len(grid[0]) // 2]
    while 0 <= current_position[0] < len(grid) and 0 <= current_position[1] < len(grid[0]):
        grid[current_position[0]][current_position[1]] += 1
        random.choice((goNorth, goEast, goSouth, goWest))(current_position)
    [print(k) for k in grid]

manhattan(5, 11)
