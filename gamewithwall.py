import pygame as pg
import picture


class wall:
    def __init__(self, x, y):
        self.image = pg.Surface((5, 5))
        self.image.fill((0, 0, 0))
        self.image.get_rect()
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 5, 5])


def create_maze(filename):
    screen = pg.display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    image = picture.image_to_array(filename)
    height, width = image.shape
    for i in range(0, width):
        for j in range(0, height):
            if image[j][i] == 0:
                print(f"i see a wall {i}, {j}")
                wall(i, j)
    pg.display.flip()

create_maze("testmaze.png")
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False




