import pygame as pg
from recursive_backtracker import recursive_backtracker


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
    if enemy_rect.colliderect(player_rect):
        lose(screen)
    if enemy_position != player_position:
        enemy_rect.move_ip(increment_x, increment_y)
        enemy_object.update()


def text_objects(text, font):
    # https: // pythonprogramming.net / displaying - text - pygame - screen /
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def lose(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pg.time.wait(1000)
    screen.fill((255, 255, 255))
    pg.font.init()
    lose_font = pg.font.Font('FreeSansBold.ttf', 115)
    text_surface, text_rect = text_objects('GAME OVER', lose_font)
    text_rect.center = (screen_width / 2, screen_height / 3)
    screen.blit(text_surface, text_rect)


def create_maze():
    White = (255, 255, 255)
    maze = recursive_backtracker()
    side_length = maze.shape[0]
    size = maze.shape[0] * 20
    print(size)
    screen = pg.display.set_mode((size, size))
    screen.fill(White)
    walls = []
    for i in range(0, side_length):
        for j in range(0, side_length):
            if maze[i, j]:
                wall = Wall(i * 20, j * 20, pg.Rect(i * 20, j * 20, 20, 20))
                walls.append(wall.rect)
    return screen, walls


def movement(screen, player, walls, desired_movement, bounce_movement):
    screen.blit(background, (0, 0))
    player.rect.move_ip(desired_movement)
    if player.rect.collidelist(walls) != -1:
        player.rect.move_ip(bounce_movement)
        player.update()
    else:
        screen.blit(background, (0, 0))
        player.update()


def run_maze():
    screen, walls = create_maze()
    global background
    background = screen.copy()
    player = Player(screen, (0, 0, 255), pg.rect.Rect(30, 30, 7, 7), 2)
    enemy = Player(screen, (255, 0, 0), pg.rect.Rect(30, 25, 7, 7), 1)
    pg.key.set_repeat(30, 30)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                x_size, y_size = event.dict['size'][0], event.dict['size'][1]
                pg.transform.scale(screen, (x_size, y_size))
                print (x_size, y_size)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a: # A to move left
                    movement(screen, player, walls, (-player.speed, 0), (player.speed, 0))
                if event.key == pg.K_d: # D to move right
                    movement(screen, player, walls, (player.speed, 0), (-player.speed, 0))
                if event.key == pg.K_s: # S to move down
                    movement(screen, player, walls, (0, player.speed), (0, -player.speed))
                if event.key == pg.K_w: # W to move up
                    movement(screen, player, walls, (0, -player.speed), (0, player.speed))
                enemy_function(screen, enemy, player)

            if event.type == pg.QUIT:
                running = False
        pg.display.flip()

run_maze()
