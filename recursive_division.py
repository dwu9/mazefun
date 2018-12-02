import numpy as np
from random import randint, getrandbits
import matplotlib.pyplot as pyplot
from math import floor, ceil


class Chamber:
    def __init__(self, min_row, max_row, min_col, max_col):
        self.min_row = min_row
        self.max_row = max_row
        self.min_col = min_col
        self.max_col = max_col

def orientation(chamber):
    min_row = chamber.min_row
    max_row = chamber.max_row
    min_col = chamber.min_col
    max_col = chamber.max_col
    if (max_row - min_row) > (max_col - min_col):
        direction = 'H'
    elif (max_row - min_row) < (max_col - min_col):
        direction = 'V'
    else:
        if bool(getrandbits(1)):
            direction = 'V'
        else:
            direction = 'H'
    return direction


def split(chamber, maze):
    min_row = chamber.min_row
    max_row = chamber.max_row
    min_col = chamber.min_col
    max_col = chamber.max_col
    if (max_row - min_row < 1) or (max_col - min_col < 1):
        return maze, None
    else:
        direction = orientation(chamber)
        if direction == 'V':
            value = ex_rand(min_col, max_col, 0)
            gap = in_rand(min_row, max_row, 1)
            maze = draw_line(maze, direction, value, min_row, max_row + 1, gap)
        elif direction == 'H':
            value = ex_rand(min_row, max_row, 0)
            gap = in_rand(min_col, max_col, 1)
            maze = draw_line(maze, direction, value, min_col, max_col + 1, gap)
        children = derive_children(direction, value, min_row, max_row, min_col, max_col)
        return maze, children

def derive_children(direction, value, min_row, max_row, min_col, max_col):
    children = []
    if direction == 'V':
        child_1 = Chamber(min_row, max_row, min_col, value - 1)
        child_2 = Chamber(min_row, max_row, value + 1, max_col)
    elif direction == 'H':
        child_1 = Chamber(min_row, value - 1, min_col, max_col)
        child_2 = Chamber(value + 1, max_row, min_col, max_col)
    children.append(child_1)
    children.append(child_2)
    return children

def ex_rand(min, max, parity):
    if min + 1 == max - 1:
        return min + 1
    elif min == max - 1:
        return min
    else:
        n = randint(min + 1, max - 1)
        if parity == 0:
            while n % 2 == 1:
                n = randint(min + 1, max - 1)
        elif parity == 1:
            while n % 2 == 0:
                n = randint(min + 1, max - 1)
        return n

def in_rand(min, max, parity):
    n = randint(min, max)
    if parity == 0:
        while n % 2 == 1:
            n = randint(min, max)
    elif parity == 1:
        while n % 2 == 0:
            n = randint(min, max)
    return n

def draw_line(array, direction, value, min, max, gap):
    if direction == "H":
        array[value, min:max] = 1
        array[value, gap] = 0
    elif direction == "V":
        array[min:max, value] = 1
        array[gap, value] = 0
    return array


def derive_first_children(direction, value, size):
    first_children = []
    if direction == 'V':
        child_1 = Chamber(0, size - 1, 0, value - 1)
        child_2 = Chamber(0, size - 1, value + 1, size - 1)
    elif direction == 'H':
        child_1 = Chamber(0, value - 1, 0, size - 1)
        child_2 = Chamber(value + 1, size - 1, 0, size - 1)
    first_children.append(child_1)
    first_children.append(child_2)
    return first_children

def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size), dtype=bool)
    if bool(getrandbits(1)):
        direction = 'V'
    else:
        direction = 'H'
    value = ex_rand(floor(0.25 * size) , ceil(0.75 * size), 0)
    gap = in_rand(0, size - 1, 1)
    draw_line(maze, direction, value, 0, size, gap)
    first_children = derive_first_children(direction, value, size)
    return maze, first_children

def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def create_boarders(maze):
    num_rows = maze.shape[0]
    num_cols = maze.shape[1]
    final_maze = np.ones((num_rows + 2, num_cols + 2), dtype=bool)
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            final_maze[i + 1][j + 1] = maze[i][j]
    return final_maze

def recurse(children_list, maze):
    sub_children = []
    for child in children_list:
        maze, sub_childs = split(child, maze)
        if sub_childs == None:
            pass
        else:
            for i in sub_childs:
                sub_children.append(i)
    if len(sub_children) != 0:
        return recurse(sub_children, maze)
    else:
        maze = np.delete(maze, (0), axis=0)
        maze = np.delete(maze, (0), axis=1)
        maze = create_boarders(maze)
        return maze

def recursive_division():
    maze, children_list = create_maze(38)
    maze = recurse(children_list, maze)
    maze[0][2] = 0
    maze[1][2] = 0
    maze[37][36] = 0
    maze[38][37] = 0

    return maze

'''
maze = recursive_division()
draw_maze(maze)
'''
