from time import sleep
import sys
import os
from ASCII_mazes import maze_animation
# Credit to http://patorjk.com/software/taag/#p=display&f=Doom&t=MazeFun
# for the ASCII Art
def print_bold(text):
    print('\033[1m' + text)
    print('\033[0m', end = '')

# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def one_at_a_time(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.05)

title =""" \
      ___  ___             ______
       |  \/  |             |  ___|
       | .  . | __ _ _______| |_ _   _ _ __
       | |\/| |/ _` |_  / _ \  _| | | | '_ \\
       | |  | | (_| |/ /  __/ | | |_| | | | |
       \_|  |_/\__,_/___\___\_|  \__,_|_| |_| 
"""
welcome = "Welcome to: "
subtitle = "       An Instructional Maze Based game!"
attribution = "       By Brendan Coutts and David Wu"
os.system('clear')
for i in [welcome, title, subtitle, attribution]:
    print(i)
    sleep(1.5)

description = "In this game you will have the choice of three different algorithms\n" \
               "to generate a maze. The program will then teach you how the particular\n" \
               "algorithm works and you will then play a game on a maze that has been\n" \
               "randomly generated using that algorithm!\n"
print()
print(description)
sleep(5)
print("Three three algorithms are: ")
sleep(2)
choice_list = ["Simple Prim's Based Generator", "Recursive Division", "Recursive Backtracker"]
count = 0
for i in choice_list:
    count += 1
    print(str(count) + '. ' + i)
    sleep(1)

choice = 0
while choice not in [1, 2, 3]:
    choice = int(input("Please Select an Algorithm (1/2/3): "))
    if choice not in [1, 2, 3]:
        print("Please enter a valid choice (1/2/3)")
sleep(1)
print("You have selected " + choice_list[choice - 1])

learn = ''
sleep(1)
while learn not in ['y', 'n']:
    learn = input("Would you like to learn about the algorithm before playing the game? (y/n): ")
    if learn not in ['y', 'n']:
        print("Please enter a valid choice (y/n)")
if learn == 'y':
    learn_flag = True
elif learn == 'n':
    learn_flag = False



if learn_flag:
    os.system('clear')
    if choice == 1:
        # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
        print_bold("Simple Prim's Based Generator")
        print("[David explain here]")
    elif choice == 2:
        print_bold("Recursive Division")
        print("Recursive division works by recursion - the process of breaking down the big\n"
              "problem of generating a maze into a series of much more manageable, smaller problems\n"
              "You start with an empty array. You then cut it into two, to get two smaller chambers.\n"
              "You then cut each of those two into even smaller chamers. This is down until no more\n"
              "divisions can take place, and what you're left with is a complete maze!")
        if input("Press enter to view an animation") == '':
            mazes = maze_animation()
            for i in mazes:
                os.system('clear')
                print(i)
                sleep(1.5)

    elif choice == 3:
        os.system('clear')
        print_bold("Recursive Backtracker")
        one_at_a_time("Recursive backtracker works like a snake. It starts at a random point and starts\n"
              "eating up cells on the grid randomly changing direction, until it hits a dead end.\n"
              "Once that happens it traverses back until it finds a cell that does have neighbours.\n"
              "Rinse and Repeat this process until all cells are visited, and you have a Maze!")


os.system('clear')
print_bold("Press Enter to Begin the Game")
print("The controls are the WASD keys for movement!"
      "Your goal is to move your blue square to the end of the maze it to t")