import numpy as np
from random import randint
from PIL import Image
# Basic implementation of recursive division maze generation
# Credit to Wikipedia.org Maze Generation
# 1s will represent wall 0s will represent white space
# All positions are measured from the top left corner (0,0)
Debug = True

class Chamber:
    def __init__(self, array, row, column):
        self.array = array
        self.x = array.shape[0]
        self.y = array.shape[1]
        if Debug:
            print(self.x, self.y)
        self.row = row
        self.column = column

    def divide(self):
        array = self.array
        x_line = randint(2, self.x-2)
        y_line = randint(2, self.y-2)
        if Debug:
            print("x_line " + str(x_line))
            print("y_line " + str(y_line))

        y_gap = randint(2, self.y-2)
        third_gap = randint(0,1)

        array[x_line, :] = 1
        array[:, y_line] = 1
        randomizer = randint(0, 1)
        if randomizer == 0:
            y_gap = randint(2, self.y - 2)
            x_gap1 = randint(2, self.x - 2)
            x_gap2 = randint(2, self.x - 2)
            for i in [x_gap1, x_gap2]:
                array[i, y_line] = 0
            array[x_line, y_gap] = 0
        else:
            x_gap = randint(2, self.x - 2)
            y_gap1 = randint(2, self.y - 2)
            y_gap2 = randint(2, self.y - 2)
            for i in [y_gap1, y_gap2]:
                array[x_line, i] = 0
            array[x_gap, y_line] = 0

        if Debug:
            print(maze.array)
        inner_arrays = []
        # Top left quadrant
        inner_arrays.append(Chamber(np.zeros((x_line, y_line)), self.row, self.column))
        # Top right quadrant
        inner_arrays.append(Chamber(np.zeros((x_line, self.y - y_line - 1)), self.row, self.column + y_line + 1))
        # Bottom left quadrant
        inner_arrays.append(Chamber(np.zeros((self.x - x_line, y_line)), self.row + x_line + 1, self.column))
        # Bottom right quadrant
        inner_arrays.append(Chamber(np.zeros((self.y - x_line - 1, self.y - y_line - 1)), self.row + x_line + 1, self.column + y_line + 1))
        if Debug:
            for i in inner_arrays:
                print(i.row, i.column)
                print(i.array)
        return inner_arrays



def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size, dtype=bool))


    return maze


def recurse(arraylist):
    inner_arrays = []
    for inner_maze in arraylist:
        if inner_maze.x > 2 and inner_maze.y > 2:
            children = inner_maze.divide()
            for i in children:
                inner_arrays.append(children)
        else:
            inner_arrays.append(inner_maze)
    """
    if inner_arrays == arraylist:
        return arraylist
    else:
        recurse(inner_arrays)
    """
    return inner_arrays

def combine_arrays(maze, inner_arrays):
    for matrix in inner_arrays:
        rows = matrix.x - 1
        columns = matrix.y - 1
        startrow = matrix.row
        startcolumn = matrix.column
        matrix = matrix.array
        for i in range(startrow, startrow + rows):
            for j in range(startcolumn, startcolumn + columns):
                maze[i][j] = matrix[i-startrow][j-startcolumn]
    return maze

def create_boarder(array):
    # Change this to append and create a boarder
    size = 0
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[size, :] = 1
    maze[:, size] = 1

maze = Chamber(create_maze(20), 0, 0)
#print(maze.array)
inner_arrays = maze.divide()
# children = recurse(inner_arrays)
# print(children)
# new_maze = combine_arrays(maze.array, children)


# I need you to work on this image conversion:
#image = Image.fromarray(maze.array, '1')
#image.save('genmaze.png')
#image.show()

