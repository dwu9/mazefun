
import pygame as pg
import picture
import sys


class Wall:
    def __init__(self, x, y, rect):
        self.image = pg.display.get_surface()
        self.rect = rect
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 1, 1])


class Player:
    def __init__(self, screen, color, rect, speed):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.surface = pg.Surface(self.rect.size)
        self.image = pg.draw.rect(self.screen, self.color, self.rect)
        self.speed = speed

        # pg.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def clear(self):
        pg.draw.rect(self.screen, (255, 255, 255), self.rect)

def enemy_function(enemy_object, player_object):
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
        print(relative_x)
        print(relative_y)
        print('YOU LOSE!')
        # sys.exit(-1)
    if enemy_position != player_position:
        enemy_rect.move_ip(increment_x, increment_y)
        enemy_object.update()


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
                wall = Wall(i, j, pg.Rect(i, j, 1, 1))
                walls.append(wall.rect)
                walllist.append((i, j))
    print(width)
    print(len(walls))
    return screen, walllist, walls


def run_maze():
    screen, walllist, walls = create_maze("testmaze1.png")
    player = Player(screen, (0, 0, 255), pg.rect.Rect(15, 5, 5, 5), 2)
    enemy = Player(screen, (255, 0, 0), pg.rect.Rect(10, 0, 5, 5), 1)
    pg.key.set_repeat(30, 30)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                xsize, ysize = event.dict['size'][0], event.dict['size'][1]
                pg.transform.scale(screen, (xsize, ysize))
                print (xsize, ysize)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a: # A to move left
                    player.clear()
                    player.rect.move_ip(-player.speed, 0)
                    if  player.rect.collidelist(walls) != -1:
                        #player.clear()
                        player.rect.move_ip(player.speed, 0)
                        player.update()
                        pass
                    else:
                        player.clear()
                        #player.rect.move_ip(-1, 0)
                        player.update()

                if event.key == pg.K_d: # D to move right
                    player.clear()
                    player.rect.move_ip(player.speed, 0)
                    if player.rect.collidelist(walls) != -1:
                        #player.clear()
                        player.rect.move_ip(-player.speed, 0)
                        player.update()
                    else:
                        #player.clear()
                        #player.rect.move_ip(1, 0)
                        player.update()

                if event.key == pg.K_s: # S to move down
                    player.clear()
                    player.rect.move_ip(0, player.speed)
                    if player.rect.collidelist(walls) != -1:
                        # player.clear()
                        player.rect.move_ip(0, -player.speed)
                        player.update()
                    else:
                        #player.clear()
                        # player.rect.move_ip(0, 1)
                        player.update()

                if event.key == pg.K_w: # W to move up
                    player.clear()
                    player.rect.move_ip(0, -player.speed)
                    if player.rect.collidelist(walls) != -1:
                        # player.clear()
                        player.rect.move_ip(0, player.speed)
                        player.update()
                    else:
                        # player.clear()
                        # player.rect.move_ip(0, -1)
                        player.update()
                enemy_function(enemy, player)
            if event.type == pg.QUIT:
                running = False
        # screen.blit(player.image, player.rect) # Makes it go nutty
        pg.display.flip()

run_maze()



