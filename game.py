import pygame as pg
import picture


def create_maze(filename):
    screen = pg.display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    wall = pg.Surface((5, 5))
    wall.fill((0, 0, 0))
    image = picture.image_to_array(filename)
    height, width = image.shape
    for i in range(0, width):
        for j in range(0, height):
            if image[j][i] == 0:
                print(f"i see a wall {i}, {j}")
                pg.draw.rect(screen, (0, 0, 0), [i, j, 5, 5])
    pg.display.flip()

running = True
while running:
    create_maze("testmaze.png")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False




