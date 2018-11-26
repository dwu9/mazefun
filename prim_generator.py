import numpy as np
from random import randint, getrandbits
from PIL import Image
import matplotlib.pyplot as pyplot
from math import floor, ceil

def create_maze(size):
    maze = np.ones((size, size), dtype=bool)
    return maze

def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def random_cell(maze, path_list, wall_list):
    num_rows = maze.shape[0] - 1
    num_cols = maze.shape[1] - 1
    rand_row = randint(0, num_rows)
    rand_col = randint(0, num_cols)
    maze[rand_row, rand_col] = 0
    wall_1 = (rand_row, rand_col + 1)
    wall_2 = (rand_row + 1, rand_col)
    wall_3 = (rand_row, rand_col - 1)
    wall_4 = (rand_row - 1, rand_col)
    for i in maze
    path_list.append((rand_row, rand_column))
    return maze, wall_list, path_list



# Start with a grid full of walls.
maze = create_maze(20)
path_list = []
wall_list = []
# Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
maze, wall_list, path_list = random_cell(maze, path_list, wall_list)

draw_maze(maze)

# While there are walls in the list:
# Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
# Make the wall a passage and mark the unvisited cell as part of the maze.
# Add the neighboring walls of the cell to the wall list.
# Remove the wall from the list.




