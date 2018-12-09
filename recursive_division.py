import numpy as np
from random import randint, getrandbits
import matplotlib.pyplot as pyplot
from math import floor, ceil


class Chamber:
    # Function:
    #   Defines one section of the maze after a division. Stores its min
    #   and max row and column values.
    # Arguments:
    #   min_row: the minimum row index
    #   max_row: the maximum row index
    #   min_col: the minimum column index
    #   max_col: the maximum column index
    # Returns: None, creates an instance of a column object
    def __init__(self, min_row, max_row, min_col, max_col):
        self.min_row = min_row
        self.max_row = max_row
        self.min_col = min_col
        self.max_col = max_col

def orientation(chamber):
    # Function:
    #   Computes the orientation of the chamber so the program knows in which
    #   direction the chamber should be divided
    # Arguments:
    #   chamber: a chamber object that is to be divided
    # Returns:
    #   direction:
    #       either 'V' for vertial or 'H' for horizontal
    min_row = chamber.min_row
    max_row = chamber.max_row
    min_col = chamber.min_col
    max_col = chamber.max_col
    if (max_row - min_row) > (max_col - min_col):
        direction = 'H'
    elif (max_row - min_row) < (max_col - min_col):
        direction = 'V'
    # If the chamber is a perfect square a direction is randomly chosen
    else:
        if bool(getrandbits(1)):
            direction = 'V'
        else:
            direction = 'H'
    return direction


def split(chamber, maze):
    # Function:
    #   Takes a chamber and splits it into two smaller children chambers
    # Arguments:
    #   chamber: a chamber object to be divded
    #   maze: the boolean array that represents the entire maze
    # Returns:
    #   maze: an edited version of the maze with the new wall
    #   children: a list of the two children chamber objects
    min_row = chamber.min_row
    max_row = chamber.max_row
    min_col = chamber.min_col
    max_col = chamber.max_col
    if (max_row - min_row < 1) or (max_col - min_col < 1):
        return maze, None
    else:
        direction = orientation(chamber)
        # A random even index is chosen to place the wall, and a random odd
        # index is chosen to create the gap in the wall
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
    # Function:
    #   Computes the min/max values of the children chamber objects
    # Arguments:
    #   direction: the orientation of the chamber
    #   value: the index of the new wall
    #   min_row: the minimum row index of the parent chamber
    #   max_row: the maximum row index of the parent chamber
    #   min_col: the minimum column index of the parent chamber
    #   max_col: the maximum column index of the parent chamber
    # Returns:
    #   children: the list of children objects
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
    # Function:
    #   An exclusive random function that computes random even or odd numbers
    # Arguments:
    #   min: the minimum value of the range
    #   max: the maximum value of the range
    #   parity: either 0 for even or 1 for odd
    # Returns:
    #   n: a pseudo-random even or odd number
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
    # Function:
    #   An inclusive random function that computes random even or odd numbers
    # Arguments:
    #   min: the minimum value of the range
    #   max: the maximum value of the range
    #   parity: either 0 for even or 1 for odd
    # Returns:
    #   n: a pseudo-random even or odd number
    n = randint(min, max)
    if parity == 0:
        while n % 2 == 1:
            n = randint(min, max)
    elif parity == 1:
        while n % 2 == 0:
            n = randint(min, max)
    return n

def draw_line(array, direction, value, min, max, gap):
    # Function:
    #   Draws a line on the maze array to create new walls
    # Arguments:
    #   array: the array representation of the maze oject
    #   direction: the orientation of the line
    #   value: the index of the line that needs to be drawn
    #   min: the min value of the opposite dimension of the line
    #   min: the max value of the opposite dimension of the line
    #   gap: the index of the gap in the wall
    # Returns:
    #   array: the altered maze array with the new wall
    if direction == "H":
        array[value, min:max] = 1
        array[value, gap] = 0
    elif direction == "V":
        array[min:max, value] = 1
        array[gap, value] = 0
    return array


def derive_first_children(direction, value, size):
    # Function:
    #   Computes the base case first children
    # Arguments:
    #   direction: the orientation of the first divide
    #   value: the index of the divide
    #   size: the dimension of the maze
    # Returns:
    #   first_children: the list containing the first two chamber objects
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
    # Function:
    #   Creates the array object which represents the maze, and makes the first
    #   division
    # Arguments:
    #   size: the size of the square maze to be created
    # Returns:
    #   maze: the array after the first division
    #   first_children: a list of the first two chamber objects
    # The maze is represented by a numpy array where False/0 represents a path
    # and True/1 represents a wall
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
    # Function:
    #   A function which creates a visual representation of the array using
    #   the pyplot module
    # Arguments:
    #   maze: the numpy array of boolean Trues and Falses
    # Returns:
    #   None, just displays the maze
    # Attribution: https://en.wikipedia.org/wiki/Maze_generation_algorithm
    #              under the example code
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def create_boarders(maze):
    # Function:
    #   Takes in a completed maze object and adds a boarder wall around
    #   the perimeter of the maze
    # Arguments:
    #   maze: the array representing the maze
    # Returns:
    #   final_maze: the complete maze with the added boarder
    num_rows = maze.shape[0]
    num_cols = maze.shape[1]
    final_maze = np.ones((num_rows + 2, num_cols + 2), dtype=bool)
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            final_maze[i + 1][j + 1] = maze[i][j]
    return final_maze

def recurse(children_list, maze):
    # Function:
    #   The recursive function which repeatedly divides the maze until it is
    #   no longer possible to further divide (i.e the dimension in either
    #   direction is less that 2
    # Arguments:
    #   children_list: the children to be divided
    #   maze: the array representation of the maze
    # Returns:
    #   maze: the completely divded maze
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
    # Function:
    #   Creates a square maze by the recursive division algorithm
    # Arguments:
    #   None
    # Returns:
    #   maze: the completed maze boolean array
    maze, children_list = create_maze(38)
    maze = recurse(children_list, maze)
    # Adds the entrance and exit for the beginning and end
    maze[0][2] = 0
    maze[1][2] = 0
    maze[37][36] = 0
    maze[38][37] = 0
    return maze
