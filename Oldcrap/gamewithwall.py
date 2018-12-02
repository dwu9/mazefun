import pygame as pg
from Oldcrap import picture


class Wall:
    def __init__(self, x, y):
        self.image = pg.display.get_surface()
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 5, 5])


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pg.Surface((10, 10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.xposition = 0
        self.yposition = 0

    def control(self, x, y):
        self.xposition += x
        self.yposition += y

    def update(self):
        self.rect.x = self.rect.x + self.xposition
        self.rect.y = self.rect.y + self.yposition


def create_maze(filename):
    screen = pg.display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    image = picture.image_to_array(filename)
    height, width = image.shape
    for i in range(0, width):
        for j in range(0, height):
            if image[j][i] == 0:
                print(f"i see a wall {i}, {j}")
                Wall(i, j)
    pg.display.flip()

create_maze("testmaze.png")
player = Player()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.control(-10, 0)
            if event.key == pg.K_RIGHT:
                player.control(10, 0)
            if event.key == pg.K_DOWN:
                player.control(0, -10)
            if event.key == pg.K_UP:
                player.control(0, 10)

        if event.type == pg.QUIT:
            running = False
    player.update()
    pg.display.flip()




