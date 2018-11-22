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
        x_gap = randint(2, self.x-2)
        y_gap = randint(2, self.y-2)
        array[x_line, :] = 1
        array[:, y_line] = 1
        array[x_line, y_gap] = 0
        array[x_gap, y_line] = 0
        if Debug:
            print(maze.array)
        inner_arrays = []
        # Top left quadrant
        inner_arrays.append(Chamber(np.zeros((x_line - 1, y_line - 1)), self.row + 1, self.column + 1))
        # Top right quadrant
        inner_arrays.append(Chamber(np.zeros((x_line - 1, self.y - y_line - 2)), self.row + 1, self.column + y_line + 1))
        # Bottom left quadrant
        inner_arrays.append(Chamber(np.zeros((self.x - x_line - 2, y_line - 2)), self.row + x_line + 1, self.column + 1))
        # Bottom right quadrant
        inner_arrays.append(Chamber(np.zeros((y_line - 2, x_line - 2, )), self.row + x_line + 1, self.column + y_line + 1))
        if Debug:
            for i in inner_arrays:
                print(i.array)
        return inner_arrays



def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size))


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

def combine_arrays:


def create_boarder(array):
    # Change this to append and create a boarder

    maze[0, :] = 1
    maze[:, 0] = 1
    maze[size, :] = 1
    maze[:, size] = 1

maze = Chamber(create_maze(20), 0, 0)
#print(maze.array)
inner_arrays = maze.divide()
children = recurse(inner_arrays)
# I need you to work on this image conversion:
#image = Image.fromarray(maze.array, '1')
#image.save('genmaze.png')
#image.show()

