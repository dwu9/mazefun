import pygame as pg
import numpy as np
from random import randint, getrandbits, choice
from PIL import Image
import matplotlib.pyplot as pyplot
from math import floor, ceil
import time
from recursive_backtracker import recursive_backtracker


class Wall:
    def __init__(self, x, y, rect):
        self.image = pg.display.get_surface()
        self.rect = rect
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 20, 20])


class Player(pg.sprite.Sprite):
    def __init__(self, image, speed, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = x
        self.y = y

    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))


def enemy_function(screen, enemy_object, player_object):
    player_rect = player_object.rect
    player_position = player_x, player_y = player_rect.x, player_rect.y
    enemy_rect = enemy_object.rect
    enemy_position = enemy_x, enemy_y = enemy_rect.x, enemy_rect.y
    relative_x = (player_x - enemy_x)
    relative_y = (player_y - enemy_y)
    if relative_x < 0:
        increment_x = -enemy_object.speed
    elif relative_x > 0:
        increment_x = enemy_object.speed
    elif relative_x == 0:
        increment_x = 0
    if relative_y < 0:
        increment_y = -enemy_object.speed
    elif relative_y > 0:
        increment_y = enemy_object.speed
    elif relative_y == 0:
        increment_y = 0
    if (relative_x, relative_y) == (0, 0):
        print('YOU LOSE!')
        # sys.exit(-1)
    if enemy_position != player_position:
        enemy_object.x += increment_x
        enemy_object.y += increment_y
        enemy_object.update(screen)


def create_maze():
    Black = (0, 0, 0)
    White = (255, 255, 255)
    maze = recursive_backtracker()
    side_length = maze.shape[0]
    size = maze.shape[0] * 20
    print(size)
    screen = pg.display.set_mode((size, size))
    screen.fill(White)
    count = 0
    walls = []
    for i in range(0, side_length):
        for j in range(0, side_length):
            if maze[i, j]:
                wall = Wall(i * 20, j * 20, pg.Rect(i * 20, j * 20, 20, 20))
                walls.append(wall.rect)
    return screen, walls


def movement(screen, player, walls, desired_movement):
    player.x += desired_movement[0]
    print(player.x)
    player.y += desired_movement[1]
    player.update(screen)
    if player.rect.collidelist(walls) != -1:
        player.x += -desired_movement[0]
        player.y += -desired_movement[1]
        player.update(screen)

def run_maze():
    screen, walls = create_maze()
    Inspiration = pg.image.load("Sprites/Inspiration.jpg").convert_alpha()
    player = Player(Inspiration, 2, 60, 55)
    enemy = Player(Inspiration, 1, 10, 10)
    pg.key.set_repeat(30, 30)
    running = True
    player.update(screen)
    enemy.update(screen)
    while running:
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                x_size, y_size = event.dict['size'][0], event.dict['size'][1]
                pg.transform.scale(screen, (x_size, y_size))
                print (x_size, y_size)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a: # A to move left
                    movement(screen, player, walls, (-player.speed, 0))
                if event.key == pg.K_d: # D to move right
                    movement(screen, player, walls, (player.speed, 0))
                if event.key == pg.K_s: # S to move down
                    movement(screen, player, walls, (0, player.speed))
                if event.key == pg.K_w: # W to move up
                    movement(screen, player, walls, (0, -player.speed))
                enemy_function(screen, enemy, player)
            if event.type == pg.QUIT:
                running = False
        # screen.blit(player.image, player.rect) # Makes it go nutty
        pg.display.flip()

run_maze()
