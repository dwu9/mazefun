# ----------------------------------------
# Name: Brendan Coutts and David Wu
# ID: 1528549 / 1528350
# CMPUT 274, Fall 2018
# Final Project: MazeFun
# ----------------------------------------
import sys
from startmenu import menu


def command_line():
    # Creates the optional command line arguments that allow the user to skip the
    # terminal menu interface and proceed directly to the game
    # The command goes "python3 mazefun.py <algorithm> <difficulty>
    # Where algorithm is 1, 2, 3 for simple generator, recursive division, and
    # recursive backtracker respectively, and difficult is either 1 for easy or
    # 2 for hard
    algorithm = 0
    difficulty = 0
    if len(sys.argv) == 3:
        if int(sys.argv[1]) in [1, 2, 3]:
            algorithm = int(sys.argv[1])
        if int(sys.argv[2]) in [1, 2]:
            difficulty = int(sys.argv[2])
    return algorithm, difficulty


def main():
    algorithm, difficulty = command_line()
    if not (algorithm and difficulty):
        algorithm, difficulty = menu()

    # Set the spped of the player and the enemy based on the inputs
    if difficulty == 1:
        p_speed = 3
        e_speed = 1

    elif difficulty == 2:
        p_speed = 3
        e_speed = 2

    # Start the pygame game. It is imported here so the game does not boot up
    # in the background while the start menu is running
    from game import run_maze
    run_maze(algorithm, p_speed, e_speed)

main()