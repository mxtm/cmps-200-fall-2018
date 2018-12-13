# Maxwell Richard Tamer-Mahoney ID #: 201804029

import os, time

class Maze:

    CURRENT_POSITION = 'S'
    OBSTACLE = '+'
    TRIED = '.'
    PART_OF_PATH = 'O'
    DEAD_END = '-'

    def __init__(self, maze_filename):
        self.__maze = []
        with open(maze_filename, 'r') as file:
            for line in file:
                self.__maze.append([char for char in line if char != '\n'])
        self.__current_row, self.__current_col = -1, -1
        for row in range(self.mazeRows()):
            for col in range(self.mazeColumns()):
                if self.__maze[row][col] == Maze.CURRENT_POSITION:
                    self.__current_row, self.__current_col = row, col 
                    break

    def mazeRows(self):
        return len(self.__maze)

    def mazeColumns(self):
        return len(self.__maze[0])

    def drawMaze(self):
        clear()
        for row in self.__maze:
            print(''.join(row))

    def getPosition(self):
        return (self.__current_row, self.__current_col)

    def getRow(self):
        return self.__current_row

    def getCol(self):
        return self.__current_col

    def updatePosition(self, row, col, val=None):
        if val:
            self.__maze[self.getRow()][self.getCol()] = val
        else:
            self.__maze[self.getRow()][self.getCol()] = ' '

        self.__maze[row][col] = Maze.CURRENT_POSITION
        self.__current_row, self.__current_col = row, col

        self.drawMaze()

    def isExit(self, row, col):
        return any((row == 0,
                   col == 0,
                   row == self.mazeRows() - 1,
                   col == self.mazeColumns() - 1))

    def __getitem__(self, row):
        return self.__maze[row]

def solveMaze(maze, start_row, start_col):
    if maze[start_row][start_col] == Maze.OBSTACLE:
        return False
    if maze[start_row][start_col] == Maze.TRIED:
        return False
    if maze.isExit(start_row, start_col):
        maze.updatePosition(start_row, start_col, Maze.PART_OF_PATH)
        return True

    maze.updatePosition(start_row, start_col, Maze.TRIED)

    found = solveMaze(maze, start_row - 1, start_col) or solveMaze(maze, start_row + 1, start_col) or solveMaze(maze, start_row, start_col - 1) or solveMaze(maze, start_row, start_col + 1)
                
    if found:
        maze.updatePosition(start_row, start_col, Maze.PART_OF_PATH)
    else:
        maze.updatePosition(start_row, start_col, Maze.DEAD_END)
    return found

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    maze = Maze('maze2.txt')
    maze.drawMaze()
    solveMaze(maze, maze.getRow(), maze.getCol())
