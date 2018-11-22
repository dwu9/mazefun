import numpy as np
from random import randint
from PIL import Image
# Basic implementation of recursive division maze generation
# Credit to Wikipedia.org Maze Generation
# 1s will represent wall 0s will represent white space
Debug = True

class Chamber:
    def __init__(self, array, pos_x, pos_y):
        self.array = array
        self.x = array.shape[0]
        self.y = array.shape[1]
        self.pos_x = pos_x
        self.pos_y = pos_y

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




def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size))
    size = size - 1
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[size, :] = 1
    maze[:, size] = 1
    return maze


maze = Chamber(create_maze(500), 1, 1)
maze.divide()
print(maze.array)
# I need you to work on this image conversion:
image = Image.fromarray(maze.array, '1')
image.save('genmaze.png')
image.show()

