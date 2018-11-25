import numpy as np
from random import randint, getrandbits
from PIL import Image
import matplotlib.pyplot as pyplot
from math import floor, ceil

# Basic implementation of recursive division maze generation
# Credit to Wikipedia.org Maze Generation
# 1s will represent wall 0s will represent white space
# All positions are measured from the top left corner (0,0)
Debug = False

class Chamber:
    def __init__(self, array, row, column):
        self.array = array
        self.num_rows = array.shape[0] - 1
        self.num_columns = array.shape[1] - 1
        if Debug:
            print(self.num_rows, self.num_columns)
        self.row_pos = row
        self.col_pos = column


    def divide(self, maze):
        # Separate these conditions
        if self.array.shape[0] <= 2 or self.array.shape[1] <= 2:
            return maze, None
        else:
            row_flag = True
            col_flag = True
            # Change row wall to divide in half
            array = self.array
            #row_wall = randint(1, self.num_rows-1)
            if bool(getrandbits(1)):
                row_wall = floor((self.num_rows / 2))
            else:
                row_wall = ceil((self.num_rows / 2))
            array[row_wall,:] = 1
            #col_wall = randint(1, self.num_columns-1)
            if bool(getrandbits(1)):
                col_wall = floor((self.num_rows / 2))
            else:
                col_wall = ceil((self.num_rows / 2))
            array[:, col_wall] = 1
            row_gap1 = randint(0, col_wall - 1)
            array[row_wall, row_gap1] = 0
            col_gap1 = randint(0, row_wall - 1)
            array[col_gap1, col_wall] = 0
            if bool(getrandbits(1)):
                row_gap2 = randint(col_wall + 1, self.num_columns)
                array[row_wall, row_gap2] = 0
            else:
                col_gap2 =randint(row_wall + 1, self.num_rows)
                array[col_gap2, col_wall] = 0
            self.array = array

            maze = combine_arrays(maze, self)

            children_list = []
            child_1 = Chamber((np.zeros((row_wall, col_wall), dtype=bool)), self.row_pos, self.col_pos)
            child_2 = Chamber(np.zeros((row_wall, self.num_columns - col_wall), dtype=bool), self.row_pos,
                              self.col_pos + col_wall + 1)
            child_3 = Chamber(np.zeros((self.num_rows - row_wall, col_wall), dtype=bool), self.row_pos + row_wall + 1,
                              self.col_pos)
            child_4 = Chamber(np.zeros((self.num_rows - row_wall, self.num_columns - col_wall), dtype=bool),
                              self.row_pos + row_wall + 1, self.col_pos + col_wall + 1)
            children_list.append(child_1)
            children_list.append(child_2)
            children_list.append(child_3)
            children_list.append(child_4)
            return maze, children_list




def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size), dtype=bool)
    return maze

# This function runs corretly and will split once
def split_children(children_list, maze):
    sub_children = []
    for child in children_list:
        # If we have one that fails maze is defined to be None and that screws
        # up future calls of this function FIX
        maze, sub_childs = child.divide(maze)
        if sub_childs == None:
            # This means that this chamber of the maze cannot be divided any further
            pass
        else:
            for i in sub_childs:
                sub_children.append(i)
    return maze, sub_children


def recurse(children_list, maze):
    sub_children = []
    for child in children_list:
        maze, sub_childs = child.divide(maze)
        if sub_childs == None:
            pass
        else:
            for i in sub_childs:
                sub_children.append(i)
    if len(sub_children) != 0:
        # TODO fix recursive logic so that the returned value carries through
        maze = recurse(sub_children, maze)
    else:
        print(maze.array)
        maze = create_boarder(maze)
        print(maze.array)
        pyplot.figure(figsize=(10, 10))
        pyplot.imshow(maze.array, cmap=pyplot.cm.binary, interpolation='nearest')
        pyplot.xticks([]), pyplot.yticks([])
        pyplot.show()
        return maze


def combine_arrays(maze, sub_child):
    num_rows = sub_child.num_rows
    num_col = sub_child.num_columns
    start_row = sub_child.row_pos
    start_col = sub_child.col_pos
    matrix = sub_child.array
    for i in range(0, num_rows + 1):
        for j in range(0, num_col + 1):
            maze.array[i + start_row][j + start_col] = matrix[i][j]
    return maze

def create_boarder(maze):
    # Change this to append and create a boarder
    array = maze.array
    maze.row_pos = 1
    maze.col_pos = 1
    print(array.shape[0], array.shape[1])
    num_rows = array.shape[0] + 2
    num_cols = array.shape[1] + 2

    expanded_array = np.ones((num_rows, num_cols), dtype=bool)
    complete_maze = Chamber(expanded_array, 0, 0)
    complete_maze = combine_arrays(complete_maze, maze)
    return complete_maze


maze = Chamber(create_maze(50), 0, 0)
maze, children = maze.divide(maze)
maze = recurse(children, maze)
# maze, sub_children = split_children(children, maze)
# maze = combine_arrays(maze, sub_children)



# Credit Wikipedia use of PyPlot
"""
pyplot.figure(figsize=(10, 10))
pyplot.imshow(maze.array, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
"""
#print(maze.array)