import pygame as pg
from recursive_backtracker import recursive_backtracker
from simple_generator import simple_generator
from recursive_division import recursive_division


class Wall:
    def __init__(self, x, y, rect):
        self.image = pg.display.get_surface()
        self.rect = rect
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 20, 20])


class Player:
    def __init__(self, screen, color, rect, speed):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.surface = pg.Surface(self.rect.size)
        self.image = pg.draw.rect(self.screen, self.color, self.rect)
        self.speed = speed

    def update(self):
        pg.draw.rect(self.screen, self.color, self.rect)


class Game:
    def __init__(self, generator_type):
        self.screen, self.walls = self.create_maze(generator_type)
        self.close_selected = False
        self.continue_game = True

    def choose_generator(self, n):
        if n == 1:
            return simple_generator()
        elif n == 2:
            return recursive_division()
        elif n == 3:
            return recursive_backtracker()

    def create_maze(self, generator_type):
        White = (255, 255, 255)
        maze = self.choose_generator(generator_type)
        side_length = maze.shape[0]
        size = maze.shape[0] * 20
        screen = pg.display.set_mode((size, size))
        screen.fill(White)
        walls = []
        for i in range(0, side_length):
            for j in range(0, side_length):
                if maze[i, j]:
                    wall = Wall(i * 20, j * 20, pg.Rect(i * 20, j * 20, 20, 20))
                    walls.append(wall.rect)
        return screen, walls

    def running

