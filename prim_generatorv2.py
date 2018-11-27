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

import numpy as np
import random as rand
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


def prim_gen(maze, frontier_list, checked_list):  # Path_list is a list of tuples (x, y)
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    if not frontier_list:  # Checks if path_list is empty
        start_row = rand.randint(0, row_index)
        start_column = rand.randint(0, column_index)
    else:
        start_row, start_column = rand.choice(frontier_list)

    # frontier_list.append((start_row, start_column))
    top = (start_row + 1, start_column)
    bottom = (start_row - 1, start_column)
    left = (start_row, start_column - 1)
    right = (start_row, start_column + 1)
    upper_right = (start_row + 1, start_column + 1)
    upper_left = (start_row + 1, start_column - 1)
    lower_right = (start_row - 1, start_column + 1)
    lower_left = (start_row - 1, start_column - 1)
    direction_list = [top, bottom, left, right]
    cross = [maze[top], maze[bottom], maze[left], maze[right], maze[upper_left], maze[upper_right], maze[lower_left], maze[lower_right]]
    if start_row in range(1, row_index - 1):
        if start_column in range(1, column_index - 1):
            print(sorted(cross))
            if sorted(cross) == [False, False, True, True, True, True, True, True] or sorted(cross) == [False, True, True, True, True, True, True, True] or sorted(cross) == [True, True, True, True, True, True, True, True]:
                maze[start_row][start_column] = 0
                if top not in frontier_list and top not in checked_list:
                    frontier_list.append(top)
                if bottom not in frontier_list and top not in checked_list:
                    frontier_list.append(bottom)
                if left not in frontier_list and top not in checked_list:
                    frontier_list.append(left)
                if right not in frontier_list and top not in checked_list:
                    frontier_list.append(right)
            else:
                print('WALL!')
        # frontier_list.remove((start_row, start_column))
        checked_list.append((start_row, start_column))
    return maze, frontier_list, checked_list


# Start with a grid full of walls.
maze = create_maze(40)
frontier_list = []
wall_list = []
checked_list = []
maze, frontier_list, checked_list = prim_gen(maze, frontier_list, checked_list)
for i in range(0, 250):
    prim_gen(maze,frontier_list, checked_list)

draw_maze(maze)





