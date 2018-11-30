from time import sleep
import os
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
for i in [welcome, title, subtitle, attribution]:
    print(i)
    sleep(2)

description = "In this game you will have the choice of three different algorithms\n" \
               "to generate a maze. The program will then teach you how the particular\n" \
               "algorithm works and you will then play a game on a maze that has been\n" \
               "randomly generated using that algorithm!\n"
print()
print(description)
sleep(5)
print()
print("Three three algorithms are: ")
sleep(2)
choice_list = ["Simple Prim's Based Generator", "Recursive Division", "Recursive Backtracker"]
count = 0
for i in choice_list:
    count += 1
    print(str(count) + '. ' + i)
    sleep(2)

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
