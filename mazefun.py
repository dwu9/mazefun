# ----------------------------------------
# Name: Brendan Coutts and David Wu
# ID: 1528549 / 1528350
# CMPUT 274, Fall 2018
# Final Project: MazeFun
# ----------------------------------------
import sys
from startmenu import menu
algorithm = 0
difficulty = 0

if len(sys.argv) == 3:
    if int(sys.argv[1]) in [1, 2, 3]:
        algorithm = int(sys.argv[1])
    if int(sys.argv[2]) in [1, 2]:
        difficulty = int(sys.argv[2])

if not (algorithm and difficulty):
    algorithm, difficulty = menu()

if difficulty == 1:
    p_speed = 3
    e_speed = 1

elif difficulty == 2:
    p_speed = 3
    e_speed = 2

from game import run_maze
run_maze(algorithm, p_speed, e_speed)
