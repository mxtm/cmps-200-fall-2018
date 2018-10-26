# Maxwell Richard Tamer-Mahoney ID #: 201804029
# TIC TAC TOE game

import random, itertools

# function to print a tic-tao-toe grid stored as a list of 3 lists
# I wrote my own function because I didn't like the given one
def print_grid(grid):
    print('  0 1 2')
    [print('{} {} {} {}'.format(i, grid[i][0], grid[i][1], grid[i][2])) for i in range(0, 3)]

def check_win(grid, player):
    wins = (
        # Horizontal
        all([i == player for i in grid[0]]),
        all([i == player for i in grid[1]]),
        all([i == player for i in grid[2]]),
        # Vertical
        all([grid[i][0] == player for i in range(0, 3)]),
        all([grid[i][1] == player for i in range(0, 3)]),
        all([grid[i][2] == player for i in range(0, 3)]),
        # Diagonal
        grid[0][0] == player and grid[1][1] == player and grid[2][2] == player,
        grid[2][0] == player and grid[1][1] == player and grid[0][2] == player
    )
    return any(wins)

def get_user_pick(empty_cells, grid):
    print_grid(grid)
    pickedCell = input('Enter a cell, row first, column second, indices beginning at 0: ')
    parsedCell = (int(pickedCell[0]), int(pickedCell[2]))
    if (parsedCell[0], parsedCell[1]) in empty_cells:
        grid[parsedCell[0]][parsedCell[1]] = 'x'
        empty_cells.remove((parsedCell[0], parsedCell[1]))
    else:
        print('Your pick was invalid.')
        get_user_pick(empty_cells, grid)


def computer_pick(empty_cells, grid):
    pickedCell = random.choice(empty_cells)
    grid[pickedCell[0]][pickedCell[1]] = 'o'
    empty_cells.remove((pickedCell[0], pickedCell[1]))

def tictactoe(empty_cells, grid):
    gameEnded = False

    #The first pick is random
    turn = itertools.cycle(random.choice((
                                        (get_user_pick, computer_pick),
                                        (computer_pick, get_user_pick)
                                        )))

    while not gameEnded:
        next(turn)(empty_cells, grid)
        if check_win(grid, 'x'):
            print('You have won!')
            print_grid(grid)
            gameEnded = True
        elif check_win(grid, 'o'):
            print('The computer has defeated you!')
            print_grid(grid)
            gameEnded = True
        elif len(empty_cells) == 0:
            print('There has been a tie.')
            print_grid(grid)
            gameEnded = True


empty_cells = [(i, j) for i in range(0, 3) for j in range(0, 3)]
grid = [['_' for i in range(0, 3)] for i in range(0, 3)]

# start the game
tictactoe(empty_cells, grid)
