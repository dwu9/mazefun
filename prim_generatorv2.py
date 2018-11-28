import numpy as np
import random as rand
import matplotlib.pyplot as pyplot
import sys


def create_maze(size):
    maze = np.ones((size, size), dtype=bool)
    return maze


def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()


def release_kraken(maze, frontier_list, checked_list):
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row = rand.randint(1, row_index - 1)
    start_column = rand.randint(1, column_index - 1)
    frontier_list.append((start_row, start_column))
    checked_list.append((start_row, start_column))
    maze[start_row][start_column] = 0


def prim_gen(maze, frontier_list, checked_list):
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row, start_column = rand.choice(frontier_list)
    top = (start_row + 1, start_column)
    bottom = (start_row - 1, start_column)
    left = (start_row, start_column - 1)
    right = (start_row, start_column + 1)
    upper_right = (start_row + 1, start_column + 1)
    upper_left = (start_row + 1, start_column - 1)
    lower_right = (start_row - 1, start_column + 1)
    lower_left = (start_row - 1, start_column - 1)
    try:
        cross = [maze[top], maze[bottom], maze[left], maze[right], maze[upper_left], maze[upper_right], maze[lower_left], maze[lower_right]]
    except IndexError:
        print('ERROR')
        print(start_row, start_column)
        sys.exit(-1)
    if start_row in range(1, row_index - 1):
        if start_column in range(1, column_index - 1):
            # print(sorted(cross))
            if sorted(cross) == [False, False, True, True, True, True, True, True] or sorted(cross) == [False, True, True, True, True, True, True, True] or sorted(cross) == [True, True, True, True, True, True, True, True]:
                maze[start_row][start_column] = 0
                if top not in frontier_list and top not in checked_list:
                    frontier_list.append(top)
                if bottom not in frontier_list and bottom not in checked_list:
                    frontier_list.append(bottom)
                if left not in frontier_list and left not in checked_list:
                    frontier_list.append(left)
                if right not in frontier_list and right not in checked_list:
                    frontier_list.append(right)
        checked_list.append((start_row, start_column))


maze = create_maze(30)
frontier_list = []
checked_list = []
release_kraken(maze, frontier_list, checked_list)

# while checked_list != frontier_list or run == 0:
for i in range(0, 20000):
    prim_gen(maze, frontier_list, checked_list)
maze = np.delete(maze, 29, 0)
maze = np.delete(maze, 29, 1)
maze[10][0] = 0
maze[10][28] = 0
maze[11][0] = 0
maze[11][28] = 0
draw_maze(maze)