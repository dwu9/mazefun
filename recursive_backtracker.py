import numpy as np
from random import randint, getrandbits, choice
from PIL import Image
import matplotlib.pyplot as pyplot
from math import floor, ceil
import time

size = 51

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
    pyplot.frameon = False
    pyplot.savefig("Maze.png", transparent=True)
    pyplot.show()


def get_neighbours(point, stack):
    global size
    row = point[0]
    col = point[1]
    neighbour_list = []
    if (not (row + 2) > (size - 1)) and ((row + 2, col) not in stack):
        neighbour_list.append((row + 2, col))
    if (not (col + 2) > (size - 1)) and ((row, col + 2) not in stack):
        neighbour_list.append((row, col + 2))
    if (not (col - 2) < 1) and ((row, col - 2) not in stack):
        neighbour_list.append((row, col - 2))
    if (not (row - 2) < 1) and ((row - 2, col) not in stack):
        neighbour_list.append((row - 2, col))

    return neighbour_list

def neighbour_flag(point, stack):
    global size
    row = point[0]
    col = point[1]
    f1, f2, f3, f4 = True, True, True, True
    neighbour_list = []
    if (row + 2) > (size - 1) or (row + 2, col) in stack:
        f1 = False
    if (col + 2) > (size - 1) or (row, col + 2) in stack:
        f2 = False
    if (col - 2) < 1 or (row, col - 2) in stack:
        f3 = False
    if (row - 2) < 1 or (row - 2, col) in stack:
        f4 = False
    return (f1 or f2 or f3 or f4)


def join_cells(maze, cell1, cell2):
    row = int((cell1[0] + cell2[0])/2)
    col = int((cell1[1] + cell2[1])/2)
    maze[row][col] = 0
    return maze

def rand_n(point, maze, stack):
    neigh_list = get_neighbours(point, stack)
    if not neigh_list:
        return maze, None
    else:
        next = choice(neigh_list)
        maze = join_cells(maze, (point), next)
        return maze, next

def rand_point(maze, cell_list, stack):
    cell = choice(cell_list)
    cell_list.remove(cell)
    maze, next = rand_n(cell, maze, stack)
    cell_list.remove(next)
    return maze, cell, next, cell_list

t0 = time.time()
stack = []
maze, cell_list = create_maze(size)
maze, cell, next, cell_list = rand_point(maze, cell_list, stack)
stack.append(cell)
stack.append(next)

while cell_list:
    maze, next = rand_n(next, maze, stack)
    if next == None:
        for point in reversed(stack):
            if neighbour_flag(point, stack):
                next = point
                break
    else:
        stack.append(next)
        cell_list.remove(next)
t1 = time.time()
print("It took " + str(t1-t0) + "s")

draw_maze(maze)