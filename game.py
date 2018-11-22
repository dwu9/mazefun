import pygame as pg
import picture


class Wall:
    def __init__(self, x, y):
        self.image = pg.display.get_surface()
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 2, 2])


class Player:
    def __init__(self, screen, rect):
        self.screen = screen
        self.color = (0, 0, 255)
        self.rect = rect
        self.surface = pg.Surface(self.rect.size)
        self.image = pg.draw.rect(self.screen, self.color, self.rect)
        # pg.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def clear(self):
        pg.draw.rect(self.screen, (255, 255, 255), self.rect)


def create_maze(filename):
    image = picture.image_to_array(filename)
    height, width = image.shape
    screen = pg.display.set_mode((width, height), pg.RESIZABLE)
    screen.fill((255, 255, 255))
    walllist= []
    walls = []
    for i in range(0, width):
        for j in range(0, height):
            if image[j][i] < 70:
                wall = Wall(i, j)
                walls.append(wall)
                walllist.append((i, j))
    pg.display.flip()
    print(walllist)
    return screen, walllist, walls


def run_maze():
    screen, walllist, walls = create_maze("testmaze1.png")
    player = Player(screen, pg.rect.Rect(15, 5, 5, 5))
    pg.key.set_repeat(30, 30)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                xsize, ysize = event.dict['size'][0], event.dict['size'][1]
                print (xsize, ysize)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    if (player.rect.left - 1, player.rect.top) in walllist:
                        pass
                    else:
                        player.clear()
                        player.rect.move_ip(-1, 0)
                        player.update()

                if event.key == pg.K_d:
                    if (player.rect.left + 6, player.rect.top) in walllist:
                        pass
                    else:
                        player.clear()
                        player.rect.move_ip(1, 0)
                        player.update()

                if event.key == pg.K_s:
                    if (player.rect.left, player.rect.top + 6) in walllist:
                        pass
                    else:
                        player.clear()
                        player.rect.move_ip(0, 1)
                        player.update()

                if event.key == pg.K_w:
                    if (player.rect.left, player.rect.top - 1) in walllist:
                        pass
                    else:
                        player.clear()
                        player.rect.move_ip(0, -1)
                        player.update()

            if event.type == pg.QUIT:
                running = False
        # screen.blit(player.image, player.rect) # Makes it go nutty
        pg.display.flip()

run_maze()



