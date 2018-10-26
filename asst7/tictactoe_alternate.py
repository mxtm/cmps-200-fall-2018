# TIC TAC TOE game

import random

# function to print a tic-tao-toe grid stored as a list of 3 lists
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end = ' ')
        print()

# test the function print_grid

def check_win(grid, player):
    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            return True
    for i in range(3):
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            return True
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    elif grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
        return True
    return False

def get_user_pick(empty_cells, grid):
    print_grid(grid)
    userPick = input('Please select a cell: ')
    userRow, userColumn = int(userPick[0]), int(userPick[2])
    if (userRow, userColumn) in empty_cells:
        grid[userRow][userColumn] = 'x'
        empty_cells.remove((userRow, userColumn))
    else:
        get_user_pick(empty_cells, grid)

def computer_pick(empty_cells, grid):
    computerPick = random.choice(empty_cells)
    grid[computerPick[0]][computerPick[1]] = 'o'
    empty_cells.remove(computerPick)

def tictactoe():
    ''' Your code goes here
    '''
    g = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]

    empty_cells = []
    for i in range(3):
        for j in range(3):
            empty_cells.append((i, j))

    whoStarts = random.choice((0, 1))

    while True:
        if whoStarts == 0:
            get_user_pick(empty_cells, g)
            computer_pick(empty_cells, g)
        else:
            computer_pick(empty_cells, g)
            get_user_pick(empty_cells, g)

# start the game
tictactoe()
