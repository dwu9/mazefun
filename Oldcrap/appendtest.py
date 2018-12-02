import numpy as np

def create_boarders(maze):
    num_rows = maze.shape[0]
    num_cols = maze.shape[1]
    final_maze = np.ones((num_rows + 2, num_cols + 2), dtype=bool)
    for i in range(0, num_rows):
        for j in range(0, num_col + 1):
            final_maze.array[i + 1][j + 1] = maze[i][j]
    return final_maze

def draw_maze(maze):
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(maze, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

maze = np.zeros((5, 5), dtype=bool)
np.insert(maze, -1, 5)
