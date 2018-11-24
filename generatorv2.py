import numpy as np
from random import randint
from PIL import Image
import matplotlib.pyplot as pyplot

# Basic implementation of recursive division maze generation
# Credit to Wikipedia.org Maze Generation
# 1s will represent wall 0s will represent white space
# All positions are measured from the top left corner (0,0)
Debug = True

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
        if self.num_rows <= 1 or self.num_columns <= 1:
            return None, None
        else:
            array = self.array
            row_wall = randint(1, self.num_rows-1)
            array[row_wall,:] = 1
            col_wall = randint(1, self.num_columns-1)
            array[:, col_wall] = 1
            row_gap1 = randint(0, col_wall - 1)
            array[row_wall, row_gap1] = 0
            row_gap2 = randint(col_wall + 1, self.num_columns)
            array[row_wall, row_gap2] = 0
            col_gap1 = randint(0, row_wall - 1)
            array[col_gap1, col_wall] = 0
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


def split_children(children_list, maze):
    sub_children = []
    for child in children_list:
        maze, sub_childs = child.divide(maze)
        if maze == None:
            pass
        else:
            for i in sub_childs:
                sub_children.append(i)
    return maze, sub_children


def recurse(arraylist):
    inner_arrays = []
    for inner_maze in arraylist:
        if inner_maze.x > 2 and inner_maze.y > 2:
            children = inner_maze.divide()
            for i in children:
                inner_arrays.append(children)
        else:
            inner_arrays.append(inner_maze)
    """
    if inner_arrays == arraylist:
        return arraylist
    else:
        recurse(inner_arrays)
    """
    return inner_arrays

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

def create_boarder(array):
    # Change this to append and create a boarder
    size = 0
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[size, :] = 1
    maze[:, size] = 1



maze = Chamber(create_maze(50), 0, 0)
maze, children = maze.divide(maze)
if Debug:
    print(children)
print(maze.array)
maze, sub_children = split_children(children, maze)
# maze = combine_arrays(maze, sub_children)



# Credit Wikipedia use of PyPlot
pyplot.figure(figsize=(10, 10))
pyplot.imshow(maze.array, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
print(maze.array)

