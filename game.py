import pygame as pg
import picture


class Wall:
    def __init__(self, x, y):
        self.image = pg.display.get_surface()
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 5, 5])


class Player:
    def __init__(self, screen, color, rect):
        self.screen = screen
        self.color = color
        self.rect = rect

    def draw(self):
        pg.draw.rec(self.screen.get_surface(), self.color, self.rect)


def create_maze(filename):
    image = picture.image_to_array(filename)
    height, width = image.shape
    screen = pg.display.set_mode((width, height))
    screen.fill((255, 255, 255))
    for i in range(0, width):
        for j in range(0, height):
            if image[j][i] == 0:
                print(f"i see a wall {i}, {j}")
                Wall(i, j)
    pg.display.flip()
    return screen

def run_maze():
    screen = create_maze("testmaze.png")
    player = Player(screen, (0, 0, 255), pg.rect.Rect(10, 10, 10, 10))
    pg.key.set_repeat(30, 30)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    player.rect.move(-3, 0)
                    print('Moving left')
                if event.key == pg.K_d:
                    print('Moving right')
                    player.rect.move(3, 0)
                if event.key == pg.K_s:
                    player.rect.move(0, -3)
                    print('Moving down')
                if event.key == pg.K_w:
                    player.rect.move(0, 3)
                    print('Moving up')
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()

run_maze()



