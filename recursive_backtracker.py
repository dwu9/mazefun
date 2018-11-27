import numpy as np
from random import randint, getrandbits, choice
from PIL import Image
import matplotlib.pyplot as pyplot
from math import floor, ceil

size = 21

def create_maze(size):
    # Create a starting blank chamber
    maze = np.ones((size, size), dtype=bool)
    cell_list = []
    for i in range(1, size - 1, 2):
        for j in range(1, size - 1, 2):
            cell_list.append((i,j))
            maze[i][j] = 0
    return maze, cell_list

def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def get_neighbours(row, col):
    global size
    neighbour_list = []
    if not (row + 2) > (size - 1):
        neighbour_list.append((row + 2, col))
    if not (col + 2) > (size - 1):
        neighbour_list.append((row, col + 2))
    if not (col - 2) < 1:
        neighbour_list.append((row, col - 2))
    if not (row - 2) < 1:
        neighbour_list.append((row - 2, col))

    return neighbour_list

def join_cells(maze, cell1, cell2):
    row = int((cell1[0] + cell2[0])/2)
    col = int((cell1[1] + cell2[1])/2)
    print(row, col)
    maze[row][col] = 0
    return maze

def rand_n(row, col, maze):
    neigh_list = get_neighbours(row, col)
    n = choice(neigh_list)
    maze = join_cells(maze, (row, col), n)
    return maze


maze, cell_list = create_maze(size)
maze = rand_n(9, 9, maze)


draw_maze(maze)


stack = []