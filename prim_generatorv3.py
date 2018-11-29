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
    start_row = rand.randint(1, row_index - 2)
    start_column = rand.randint(1, column_index - 2)
    frontier_list.append((start_row, start_column))
    checked_list.append((start_row, start_column))
    maze[start_row][start_column] = 0


def nearby_blocks(start_row, start_column):
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
    if direction not in frontier_list and direction not in checked_list and maze[direction] != 0:
        frontier_list.append(direction)


def prim_gen(maze, frontier_list, checked_list):
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row, start_column = rand.choice(frontier_list)
    top, bottom, left, right, upper_left, upper_right, lower_left, lower_right = nearby_blocks(start_row, start_column)
    cross = [maze[top], maze[bottom], maze[left], maze[right]]
    diagonals = [maze[upper_left], maze[upper_right], maze[lower_left], maze[lower_right]]
    if start_row in range(1, row_index - 1):
        if start_column in range(1, column_index - 1):
            # print(sorted(cross))
            if sorted(cross) == [0, 1, 1, 1] or sorted(cross) == [1, 1, 1, 1]:
                if sorted(diagonals) == [0, 1, 1, 1] or sorted(diagonals) == [1, 1, 1, 1]:
                    maze[start_row][start_column] = 0
                    if top not in frontier_list and top not in checked_list and maze[top] != 0:
                        frontier_list.append(top)
                    if bottom not in frontier_list and bottom not in checked_list and maze[bottom] != 0:
                        frontier_list.append(bottom)
                    if left not in frontier_list and left not in checked_list and maze[left] != 0:
                        frontier_list.append(left)
                    if right not in frontier_list and right not in checked_list and maze[right] != 0:
                        frontier_list.append(right)
        checked_list.append((start_row, start_column))


def main():
    maze = create_maze(30)
    frontier_list = []
    checked_list = []
    release_kraken(maze, frontier_list, checked_list)

    # while checked_list != frontier_list or run == 0:
    for i in range(0, 10000):
        prim_gen(maze, frontier_list, checked_list)
    maze = np.delete(maze, 29, 0)
    maze = np.delete(maze, 29, 1)
    maze[5][0] = 0
    maze[25][28] = 0
    maze[5][1] = 0
    maze[25][27] = 0
    draw_maze(maze)


main()
