import numpy as np
from random import randint, getrandbits
from PIL import Image
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
        direcction = 'H'
    elif (max_row - min_row) < (max_col - min_col):
        direction = 'V'
    else:
        if bool(getrandbits(1)):
            direction = 'V'
        else:
            direction = 'H'
    return direction


def split(chamber, maze):
    direction = orientation(chamber)
    min_row = chamber.min_row
    max_row = chamber.max_row
    min_col = chamber.min_col
    max_col = chamber.max_col
    if direction == 'V':
        value = ex_rand(min_col, max_col)
        gap = in_rand(min_row, max_row)
        draw_line(maze, direction, value, min_row, max_row, gap)
    elif direction == 'H':
        value = ex_rand(min_row, max_row)
        gap = in_rand(min_row, max_row)
        draw_line(maze, direction, value, min_col, max_col, gap)
    return maze

def ex_rand(min, max):
    return randint(min + 1, max - 1)

def in_rand(min,max):
    return randint(min, max)

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
        child_1 = Chamber(0, size, 0, value - 1)
        child_2 = Chamber(0, size, value + 1, size)
    elif direction == 'H':
        child_1 = Chamber(0, value - 1, 0, size)
        child_2 = Chamber(value + 1, size, 0, size)
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
    value = ex_rand(floor(0.25 * size) , ceil(0.75 * size))
    gap = in_rand(0, size - 1)
    draw_line(maze, direction, value, 0, size, gap)
    first_children = derive_first_children(direction, value, size)
    return maze, first_children

def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()


maze, first_children = create_maze(20)
draw_maze(maze)

for child in first_children:
    print(child.min_row, child.max_row, child.min_col, child.max_col)
    maze = split(child, maze)

draw_maze(maze)