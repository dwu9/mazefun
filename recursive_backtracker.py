# ----------------------------------------
# Name: Brendan Coutts and David Wu
# ID: 1528549 / 1528350
# CMPUT 274, Fall 2018
# Final Project: MazeFun
# ----------------------------------------

import numpy as np
from random import choice
import matplotlib.pyplot as pyplot


size = 39


def create_maze(size):
    # Function:
    #   Creates a starting array with a cells alternating with wall cells and
    #   path cells. On alternating rows.
    # Arguments:
    #   size: the size of the square maze to be created
    # Returns:
    #   maze: the array with the alternating pattern as described
    #   cell_list: a list containing the indices of all path cells
    maze = np.ones((size, size), dtype=bool)
    cell_list = []
    for i in range(1, size - 1, 2):
        for j in range(1, size - 1, 2):
            cell_list.append((i,j))
            maze[i][j] = 0
    return maze, cell_list


def draw_maze(maze):
    # Function:
    #   A function which creates a visual representation of the array using
    #   the pyplot module
    # Arguments:
    #   maze: the numpy array of boolean Trues and Falses
    # Returns:
    #   None, just displays the maze
    # Attribution: https://en.wikipedia.org/wiki/Maze_generation_algorithm
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.frameon = False
    pyplot.savefig("Maze.png", transparent=True)
    pyplot.show()


def get_neighbours(point, stack):
    # Function:
    #   Computes the neighbour cells of a path cell. It checked two cells in
    #   every direction to see if that is within the perimeter of the maze
    #   and has not already been visited
    # Arguments:
    #   point: a tuple indicating the position of the cell to be checked
    #   stack: the list of cells that have been visited already
    # Returns:
    #   neighbour_list: a list of the unvisited neighbour cells
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
    # Function:
    #   Checks to see if a cell has any neighbours
    # Arguments:
    #   point: a tuple indicating the position of the cell to be checked
    #   stack: the list of cells that have been visited already
    # Returns:
    #   Boolean T/F on weather or not a cell has an unvisited neighbour
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
    # Function:
    #   Eliminates the wall cell between two path cells to join them together
    # Arguments:
    #   maze: the numpy array representing the maze
    #   cell1: a tuple containing the starting cell
    #   cell2: a tuple containing the ending cell
    # Returns:
    #   maze: the altered array with the new joined path
    row = int((cell1[0] + cell2[0])/2)
    col = int((cell1[1] + cell2[1])/2)
    maze[row][col] = 0
    return maze


def rand_n(point, maze, stack):
    # Function:
    #   Chooses a random neighbour path cell and joins that cell to the
    #   argument cell
    # Arguments:
    #   point: a tuple indicating the position of the cell of interest
    #   maze: the numpy array representing the maze
    #   stack: the list of cells that have been visited already
    # Returns:
    #   maze: the numpy array with the new path
    #   next: the destination cell which will now become the next cell of interest
    neigh_list = get_neighbours(point, stack)
    if not neigh_list:
        return maze, None
    else:
        next = choice(neigh_list)
        maze = join_cells(maze, (point), next)
        return maze, next


def rand_point(maze, cell_list, stack):
    # Function:
    #   Chooses a random starting path cell to begin the process
    # Arguments:
    #   maze: the numpy array representing the maze
    #   cell_list: a list containing the indices of all possible starting cells
    #   stack: the list of cells that have been visited already
    # Returns:
    #   maze: the numpy array with the first path being drawn
    #   cell: a tuple containing the randomly slected starting cell
    #   next: a tuple containing the next cell
    #   cell_list: a list containing all the cells that are left to be visited
    cell = choice(cell_list)
    cell_list.remove(cell)
    maze, next = rand_n(cell, maze, stack)
    cell_list.remove(next)
    return maze, cell, next, cell_list


def recursive_backtracker():
    # Function:
    #   Creates a maze using the recursive backtracker algorithm
    # Arguments:
    #   None
    # Returns:
    #   maze: a numpy array of boolean T/F represented the completed maze
    stack = []
    maze, cell_list = create_maze(size)
    maze, cell, next, cell_list = rand_point(maze, cell_list, stack)
    stack.append(cell)
    stack.append(next)
    # The program runs until there are no cells left to be visited
    while cell_list:
        maze, next = rand_n(next, maze, stack)
        # If a cell has no neighbours the program iterates backwards through
        # the stack until it find one that does
        if next == None:
            for point in reversed(stack):
                if neighbour_flag(point, stack):
                    next = point
                    break
        else:
            stack.append(next)
            cell_list.remove(next)
    # Create the entrance and exit points for the maze game
    maze[0][2] = 0
    maze[1][2] = 0
    maze[size - 1][size - 5] = 0
    maze[size - 2][size - 5] = 0
    return maze
