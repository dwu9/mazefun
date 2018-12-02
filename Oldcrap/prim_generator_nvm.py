import numpy as np
from random import randint, getrandbits, choice
from PIL import Image
import matplotlib.pyplot as pyplot
from math import floor, ceil
import time

size = 10

def create_maze(size):
    # Create a starting blank chamber
    maze = np.ones((size, size), dtype=bool)
    cell_list = []
    for i in range(1, size - 1, 1):
        for j in range(1, size - 1):
            if (i+j) % 2 == 0:
                cell_list.append((i,j))
                maze[i][j] = 0
    return maze, cell_list

def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.frameon = False
    pyplot.savefig("Maze.png", transparent=True)
    pyplot.show()

def get_walls(point):
    row = point[0]
    col = point[1]
    global size
    walls = []
    if not (row + 1) > (size - 2):
        walls.append((row + 1, col))
    if not (col + 1) > (size - 2):
        walls.append((row, col + 1))
    if not (col - 1) < 1:
        walls.append((row, col - 1))
    if not (row - 1) < 1:
        walls.append((row - 1, col))
    return walls

def get_neighbours(point):
    global size
    row = point[0]
    col = point[1]
    neighbour_list = []
    if (not (row + 2) > (size - 1)):
        neighbour_list.append((row + 2, col))
    if (not (col + 2) > (size - 1)):
        neighbour_list.append((row, col + 2))
    if (not (col - 2) < 1):
        neighbour_list.append((row, col - 2))
    if (not (row - 2) < 1):
        neighbour_list.append((row - 2, col))
    return neighbour_list

print(get_neighbours((1,1)))
maze, cell_list = create_maze(size)
draw_maze(maze)
