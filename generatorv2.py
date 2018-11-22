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



    def divide(self):
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

        children_list = []
        child_1 = Chamber(np.array((row_wall, col_wall), dtype=bool), self.row_pos, self.col_pos)
        child_2 = Chamber(np.array((row_wall, self.num_columns - col_wall), dtype=bool), self.row_pos,
                          self.column_pos + col_wall + 1)
        child_3 = Chamber(np.array((self.num_rows - row_wall, col_wall), dtype=bool), self.row_pos + row_wall + 1,
                          self.column_pos)
        child_4 = Chamber(np.array((self.num_rows - row_wall, self.num_columns - col_wall), dtype=bool),
                          self.row_pos + row_wall + 1, self.column_pos + col_wall + 1)
        children_list.append(child_1)
        children_list.append(child_2)
        children_list.append(child_3)
        children_list.append(child_4)
        return children_list
        return children




def create_maze(size):
    # Create a starting blank chamber
    maze = np.zeros((size, size), dtype=bool)
    return maze


def split_children(children_list):
    all_sub_children = []
    for child in children_list:
        sub_children = child.divide()
        for i in sub_children:
            all_sub_children.append(i)
    return all_sub_children


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

def combine_arrays(maze, inner_arrays):
    for matrix in inner_arrays:
        rows = matrix.x - 1
        columns = matrix.y - 1
        startrow = matrix.row
        startcolumn = matrix.column
        matrix = matrix.array
        for i in range(startrow, startrow + rows):
            for j in range(startcolumn, startcolumn + columns):
                maze[i][j] = matrix[i-startrow][j-startcolumn]
    return maze

def create_boarder(array):
    # Change this to append and create a boarder
    size = 0
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[size, :] = 1
    maze[:, size] = 1



maze = Chamber(create_maze(100), 0, 0)
children = maze.divide()
if Debug:
    print(children)
print(maze.array)
sub_children = split_children(children)



# Credit Wikipedia use of PyPlot
pyplot.figure(figsize=(10, 10))
pyplot.imshow(maze.array, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
#print(maze.array)
# inner_arrays = maze.divide()
# children = recurse(inner_arrays)
# print(children)
# new_maze = combine_arrays(maze.array, children)


# I need you to work on this image conversion:
#image = Image.fromarray(maze.array, '1')
#image.save('genmaze.png')
#image.show()

