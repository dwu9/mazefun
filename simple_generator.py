# ----------------------------------------
# Name: Brendan Coutts and David Wu
# ID: 1528549 / 1528350
# CMPUT 274, Fall 2018
# Final Project: MazeFun
# ----------------------------------------

import numpy as np
import random as rand
import matplotlib.pyplot as pp

maze_size = 40  # Size of the maze is square of this dimension


def create_maze(size):
    # Function: Initializes matrix of given size, fills it with Trues representing walls
    # Arguments:
    #   size: size of the matrix, x by y
    # Returns:
    #   maze: Matrix of size filled with trues
    maze = np.ones((size, size), dtype=bool)
    return maze


def draw_maze(maze):
    # Function: Draws maze from matrix using pyplot, used for testing algorithm; True is black, False is white
    # Arguments:
    #   maze: Two dimensional matrix of trues and falses
    # Returns: None, draws maze
    pp.figure(figsize=(10, 10))
    pp.imshow(maze, cmap=pp.cm.binary, interpolation='nearest')
    pp.xticks([]), pp.yticks([])
    pp.show()


def release_kraken(maze, frontier_list, checked_list):
    # Function: Picks random starting point that is within the bounds of the maze
    # Arguments:
    #   maze: Matrix of trues and falses
    #   frontier_list: List of matrix indices that should be checked
    #   checked_list: list of matrix indicies that have already been checked
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    # Picks random point on maze
    start_row = rand.randint(1, row_index - 2)
    start_column = rand.randint(1, column_index - 2)
    frontier_list.append((start_row, start_column))  # Appends all surrounding squares to frontier_list
    checked_list.append((start_row, start_column))  # Appends self to checked_list
    maze[start_row][start_column] = 0  # Clears "wall" from starting square


def nearby_blocks(start_row, start_column):
    # Function: Finds indices of all surrounding items in a matrix from a given starting spot
    # Arguments:
    #   start_row, start_column: Index of point whose surroundings will be checked
    # Returns: Indices of all 8 blocks surrounding checked point
    top = (start_row + 1, start_column)
    bottom = (start_row - 1, start_column)
    left = (start_row, start_column - 1)
    right = (start_row, start_column + 1)
    upper_right = (start_row + 1, start_column + 1)
    upper_left = (start_row + 1, start_column - 1)
    lower_right = (start_row - 1, start_column + 1)
    lower_left = (start_row - 1, start_column - 1)
    return top, bottom, left, right, upper_left, upper_right, lower_left, lower_right


def frontier_prep(maze, frontier_list, checked_list, direction):
    # Function: Checks if a block is already queued to be checked or has already  been checked
    #           appends to frontier_list if otherwise
    # Arguments:
    #   frontier_list: List of matrix indices that should be checked
    #   checked_list: list of matrix indices that have already been checked
    #   direction: index of block that will be checked
    # Returns: None, edits frontier_list and checked_list
    # Algorithm loosely based on prim's described by link below
    # http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
    if direction not in frontier_list and direction not in checked_list and maze[direction] != 0:
        frontier_list.append(direction)


def simple_gen(maze, frontier_list, checked_list):
    # Function: Main algorithmic loop that will clear out a path from a maze full of walls
    # Arguments:
    #   maze: Matrix of trues and false
    #   frontier_list: List of matrix indices that should be checked
    #   checked_list: list of matrix indices that have already been checked
    # Returns: None, edits frontier_list, checked_list, and maze
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row, start_column = rand.choice(frontier_list)  # Picks a random point from the frontier_list to check
    top, bottom, left, right, upper_left, upper_right, lower_left, lower_right = nearby_blocks(start_row, start_column)
    cross = [maze[top], maze[bottom], maze[left], maze[right]]  # Cardinal directions from start point
    diagonals = [maze[upper_left], maze[upper_right], maze[lower_left], maze[lower_right]]  # Diagonals from point
    # Algorithm checks number of walls around a point, deletes wall if there are more than 2 walls around it
    if start_row in range(1, row_index - 1):
        if start_column in range(1, column_index - 1):
            if sorted(cross) == [0, 1, 1, 1] or sorted(cross) == [1, 1, 1, 1]:
                if sorted(diagonals) == [0, 1, 1, 1] or sorted(diagonals) == [1, 1, 1, 1]:
                    maze[start_row][start_column] = 0
                    # Checks if points are within bounds of maze, edges of maze are not checked
                    for direction in [top, left, right, bottom]:
                        if direction[0] != 0 and direction[0] != maze_size - 2 and direction[1] != maze_size - 2:
                            frontier_prep(maze, frontier_list, checked_list, direction)
        checked_list.append((start_row, start_column))
        frontier_list.remove((start_row, start_column))


def simple_generator():
    # Function: Main generation loop, creates maze using algorithm
    # Arguments: None
    # Returns:
    #   maze: Matrix of trues and false

    # Initializes maze before algorithm starts
    maze = create_maze(maze_size)
    frontier_list = []
    checked_list = []
    release_kraken(maze, frontier_list, checked_list)
    run = 0  # Run variable used for checking how many times program loops, for testing and debugging
    # Generation loop that runs algorithm
    while frontier_list:
        simple_gen(maze, frontier_list, checked_list)
        run += 1
        # draw_maze(maze) used to debug
    # Creates spawn points on maze
    maze = np.delete(maze, maze_size - 1, 0)
    maze = np.delete(maze, maze_size - 1, 1)
    maze[0][2] = 0
    maze[1][2] = 0
    maze[maze_size - 2][maze_size - 5] = 0
    maze[maze_size - 3][maze_size - 5] = 0
    # draw_maze(maze)
    return maze