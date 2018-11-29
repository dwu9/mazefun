import numpy as np
import random as rand
import matplotlib.pyplot as pp

maze_size = 40


def create_maze(size):
    maze = np.ones((size, size), dtype=bool)
    return maze


def draw_maze(maze):
    pp.figure(figsize=(10, 10))
    pp.imshow(maze, cmap=pp.cm.binary, interpolation='nearest')
    pp.xticks([]), pp.yticks([])
    pp.show()


def release_kraken(maze, frontier_list, checked_list):
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row = rand.randint(1, row_index - 2)
    start_column = rand.randint(1, column_index - 2)
    frontier_list.append((start_row, start_column))
    checked_list.append((start_row, start_column))
    maze[start_row][start_column] = 0


def nearby_blocks(start_row, start_column):
    global size
    for i in [top, bottom, left, right, upper_left, upper_right, lower_left, lower_right]:
        i = None
    if (start_row + 2) < size - 1:
        top = (start_row + 2, start_column)
    if (start_row - 2) > 0:
        bottom = (start_row - 2, start_column)
    if (start_column - 2) > 0:
        left = (start_row, start_column - 2)
    if (start_column + 2) < size - 1:
        right = (start_row, start_column + 2)
    return top, bottom, left, right


def frontier_prep(maze, frontier_list, checked_list, direction):
    if direction not in frontier_list and direction not in checked_list and maze[direction] != 0:
        frontier_list.append(direction)


def prim_gen(maze, frontier_list, checked_list):
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row, start_column = rand.choice(frontier_list)
    top, bottom, left, right, upper_left, upper_right, lower_left, lower_right = nearby_blocks(start_row, start_column)
    cross = [maze[top], maze[bottom], maze[left], maze[right]]
    if start_row in range(1, row_index - 2):
        if start_column in range(1, column_index - 2):
            if sorted(cross) == [0, 1, 1, 1] or sorted(cross) == [1, 1, 1, 1]:
                maze[start_row][start_column] = 0
                for direction in [top, left, right, bottom]:
                    if direction[0] != 0 and direction[0] != maze_size - 2 and direction[1] != maze_size - 2:
                        frontier_prep(maze, frontier_list, checked_list, direction)
        checked_list.append((start_row, start_column))
        frontier_list.remove((start_row, start_column))


def main():
    maze = create_maze(maze_size)
    frontier_list = []
    checked_list = []
    release_kraken(maze, frontier_list, checked_list)
    run = 0

    # while checked_list != frontier_list or run == 0:
    while frontier_list:
        prim_gen(maze, frontier_list, checked_list)
        run += 1
        #draw_maze(maze)
    maze = np.delete(maze, maze_size - 1, 0)
    maze = np.delete(maze, maze_size - 1, 1)
    maze[5][0] = 0
    maze[maze_size - 5][maze_size - 2] = 0
    maze[5][1] = 0
    maze[maze_size - 5][maze_size - 3] = 0
    draw_maze(maze)
    print(run)


main()