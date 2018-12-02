from time import sleep
import sys
import os
from ASCII_mazes import maze_animation

def print_bold(text):
    print('\033[1m' + text)
    print('\033[0m', end = '')


# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def one_at_a_time(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.05)


def print_header():
    # Credit to http://patorjk.com/software/taag/#p=display&f=Doom&t=MazeFun
    # for the ASCII Art
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
    print(welcome)
    sleep(1.5)
    for i in [title, subtitle, attribution]:
        print(i)

    sleep(1.5)
    description = "In this game you will have the choice of three different algorithms\n" \
                   "to generate a maze. The program will then teach you how the particular\n" \
                   "algorithm works and you will then play a game on a maze that has been\n" \
                   "randomly generated using that algorithm!\n"
    print()
    print(description)
    sleep(3)


def choose_algorithm():
    print("The three algorithms are: ")
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
    return choice


def learn(choice):
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
            sleep(1)
            print("The simple generator works a bit like minesweeper. First, it chooses a block and\n"
                  "looks at the number of walls around it. Based on this, it decides whether to\n"
                  "clear the block or leave it unchanged. Then it adds the surrounding unchecked\n"
                  "blocks to a list where it will perform the same check and clear process until\n"
                  "the list is empty.")
            print()
            while input("Press Enter to Continue") != '':
                pass
        elif choice == 2:
            print_bold("Recursive Division")
            sleep(1)
            print("Recursive division works by recursion - the process of breaking down the big\n"
                  "problem of generating a maze into a series of much more manageable, smaller\n"
                  "problems. You start with an empty field. You then cut it into two, to get\n"
                  "two smaller chambers. You then cut each of those two into even smaller chambers.\n"
                  "This is done until no more divisions can take place, and what you're left\n"
                  "with is a complete maze!")
            print()
            while input("Press Enter to View An Animation") != '':
                pass
            mazes = maze_animation()
            for i in mazes:
                os.system('clear')
                print(i)
                sleep(1.5)

        elif choice == 3:
            print_bold("Recursive Backtracker")
            sleep(1)
            one_at_a_time("Recursive backtracker works like a snake. It begins at a random point and starts\n"
                  "eating up cells on the grid randomly changing direction, until it hits a dead"
                  "end. Once that happens it traverses back until it finds a cell that does have\n"
                  "neighbours. Rinse and Repeat this process until all cells are visited, and\n"
                  "you have a Maze!")
            print()
            while input("Press Enter to Continue") != '':
                pass


def choose_difficulty():
    os.system('clear')
    difficulty = 0
    difficulty_list = ["Easy", "Hard"]
    while difficulty not in [1, 2, 3]:
        print_bold("Please choose a difficulty:" )
        sleep(0.5)
        print("1.Easy")
        sleep(0.5)
        print("2.Hard")
        sleep(0.5)
        difficulty = int(input("(1/2): "))
        if difficulty not in [1, 2, 3]:
            print("Please enter a valid input.")
        sleep(1)
    print("You have seleted: " + difficulty_list[difficulty - 1])
    sleep(1)
    return difficulty


def menu():
    print_header()
    algorithm = choose_algorithm()
    learn(algorithm)
    difficulty = choose_difficulty()
    print("Both WASD or the Directional Keypad can be used for movement!\n"
          "Your goal is to move the blue square to the end of the maze while avoiding\n"
          "the Flying Red Enemy Square.\n"
          "Goodluck!")
    sleep(1)
    print_bold("Press Enter to Begin the Game")
    while input() != '':
        pass
    return algorithm, difficulty
