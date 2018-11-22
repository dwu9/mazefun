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
        self.row = row
        self.column = column

    def divide(self):
        array = self.array
        x_line = randint(1, self.x-1)
        y_line = randint(1, self.y-1)
        if Debug:
            print(x_line)
            print(y_line)
        x_gap = randint(1, self.x-1)
        y_gap = randint(1, self.y-1)
        array[x_line, :] = 1
        array[:, y_line] = 1
        array[x_line, y_gap] = 0
        array[x_gap, y_line] = 0
        inner_arrays = []
        # Top left quadrant
        inner_arrays.append(np.array(x_line - 2, y_line - 2), self.row + 1, self.column + 1)
        # Top right quadrant
        inner_arrays.append(np.array(x_line - 2, self.size - y_line - 2), self.row + 1, self.column + y_line + 1)
        # Bottom left quadrant
        inner_arrays.append(np.array(self.size - x_line - 2, y_line - 2), self.row + x_line + 1, self.pos_y + 1)
        # Bottom right quadrant
        inner_arrays.append(np.array(x_line - 2, y_line - 2))




def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size))
    size = size - 1
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[size, :] = 1
    maze[:, size] = 1
    return maze


maze = Chamber(create_maze(20), 0, 0)
maze.divide()
print(maze.array)
# I need you to work on this image conversion:
image = Image.fromarray(maze.array, '1')
image.save('genmaze.png')
#image.show()

