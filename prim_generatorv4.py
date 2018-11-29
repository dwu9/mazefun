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


def release_kraken(maze, frontier_list):
    row_index = maze.shape[0] - 1
    column_index = maze.shape[1] - 1
    start_row = rand.randint(0, row_index)
    start_column = rand.randint(0, column_index)
    frontier_list.append((start_row, start_column))


def far_neighbours(start_row, start_column, n):
    far_neighbour_list = []
    if start_row + n <= maze_size - 1:
        far_top = (start_row + n, start_column)
    else:
        far_top = None
    far_neighbour_list.append(far_top)
    if start_column + n <= maze_size - 1:
        far_right = (start_row, start_column + n)
    else:
        far_right = None
    far_neighbour_list.append(far_right)
    if start_column - n >= 1:
        far_left = (start_row, start_column - n)
    else:
        far_left = None
    far_neighbour_list.append(far_left)
    if start_row - n >= 1:
        far_bottom = (start_row - 2, start_column)
    else:
        far_bottom = None
    far_neighbour_list.append(far_bottom)
    return far_neighbour_list, far_top, far_right, far_left, far_bottom


def frontier_prep(maze, frontier_list, checked_list, direction):
    if direction not in frontier_list and direction not in checked_list and maze[direction] != 0:
        frontier_list.append(direction)


def prim_gen(maze, frontier_list):
    start_row, start_column = rand.choice(frontier_list)
    far_neighbours_list, far_top, far_right, far_left, far_bottom = far_neighbours(start_row, start_column, 2)
    neighbours_list, top, right, left, bottom = far_neighbours(start_row, start_column, 1)

    while far_neighbours_list:
        '''
        print(far_neighbours_list)
        print('Far left is ' + str(far_left))
        print('Far right is ' + str(far_right))
        print('Far top is ' + str(far_top))
        print('Far bottom is ' + str(far_bottom))
        '''
        if far_top is not None:
            if maze[far_top] == 1:
                maze[top] = 0
                neighbours_list1, top1, right1, left1, bottom1 = far_neighbours(far_top, 1)
                for i in neighbours_list1:
                    if i is not None:
                        frontier_list.append(i)
        far_neighbours_list.remove(far_top)

        if far_right is not None:
            if maze[far_right] == 1:
                maze[right] = 0
                neighbours_list2, top2, right2, left2, bottom2 = far_neighbours(far_right, 1)
                for i in neighbours_list2:
                    if i is not None:
                        frontier_list.append(i)
        far_neighbours_list.remove(far_right)

        if far_left is not None:
            if maze[far_left] == 1:
                maze[left] = 0
                neighbours_list3, top3, right3, left3, bottom3 = far_neighbours(far_left, 1)
                for i in neighbours_list3:
                    if i is not None:
                        frontier_list.append(i)
        far_neighbours_list.remove(far_left)

        if far_bottom is not None:
            if maze[far_bottom] == 1:
                maze[bottom] = 0
                neighbours_list4, top4, right4, left4, bottom4 = far_neighbours(far_bottom, 1)
                for i in neighbours_list4:
                    if i is not None:
                        frontier_list.append(i)
        far_neighbours_list.remove(far_bottom)

    frontier_list.remove((start_row, start_column))



def main():
    maze = create_maze(maze_size)
    frontier_list = []
    run = 0
    release_kraken(maze, frontier_list)

    # while checked_list != frontier_list or run == 0:
    for i in range(0, 20):
        prim_gen(maze, frontier_list)
        run += 1
        #draw_maze(maze)
    draw_maze(maze)
    #print(run)


main()
