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
        results_screen(screen, "GAME OVER")
        quit_prompt(screen)
    if enemy_position != player_position:
        enemy_rect.move_ip(increment_x, increment_y)
        enemy_object.update()
    if player_x > screen.get_width() or player_y > screen.get_height():
        results_screen(screen, "YOU WIN")
        quit_prompt(screen)


def text_objects(text, font):
    # https: // pythonprogramming.net / displaying - text - pygame - screen /
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def results_screen(screen, text_result):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pg.time.wait(500)
    screen.fill((255, 255, 255))
    pg.font.init()
    result_font = pg.font.Font('FreeSansBold.ttf', 115)
    text_surface, text_rect = text_objects(text_result, result_font)
    text_rect.center = (screen_width / 2, screen_height / 3)
    screen.blit(text_surface, text_rect)


def quit_prompt(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    quit_font = pg.font.Font('FreeSansBold.ttf', 60)
    text_surface, text_rect = text_objects('Press Enter to Quit', quit_font)
    text_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(text_surface, text_rect)


def choose_generator(n):
    if n == 1:
        return simple_generator()
    elif n == 2:
        return recursive_division()
    elif n == 3:
        return recursive_backtracker()


def create_maze(generator_type):
    White = (255, 255, 255)
    maze = choose_generator(generator_type)
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


def movement(screen, player, walls, desired_movement, bounce_movement):
    player.rect.move_ip(desired_movement)
    if player.rect.collidelist(walls) != -1:
        player.rect.move_ip(bounce_movement)
        player.update()
    else:
        screen.blit(background, (0, 0))
        player.update()


def run_maze(generator_type, p_speed, e_speed):
    screen, walls = create_maze(generator_type)
    global background
    background = screen.copy()
    player = Player(screen, (0, 0, 255), pg.rect.Rect(10, 46, 7, 7), p_speed)
    enemy = Player(screen, (255, 0, 0), pg.rect.Rect(350, 350, 7, 7), e_speed)
    pg.key.set_repeat(30, 30)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                x_size, y_size = event.dict['size'][0], event.dict['size'][1]
                pg.transform.scale(screen, (x_size, y_size))
                print (x_size, y_size)

            if event.type == pg.KEYDOWN:
                screen.blit(background, (0, 0))
                player.update()
                if event.key == pg.K_a or event.key == pg.K_LEFT: # A to move left
                    movement(screen, player, walls, (-player.speed, 0), (player.speed, 0))
                if event.key == pg.K_d or event.key == pg.K_RIGHT: # D to move right
                    movement(screen,     player, walls, (player.speed, 0), (-player.speed, 0))
                if event.key == pg.K_s or event.key == pg.K_DOWN: # S to move down
                    movement(screen, player, walls, (0, player.speed), (0, -player.speed))
                if event.key == pg.K_w or event.key == pg.K_UP: # W to move up
                    movement(screen, player, walls, (0, -player.speed), (0, player.speed))
                if event.key == pg.K_RETURN:
                    running = False
                enemy_function(screen, enemy, player)
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()

# run_maze(generator, playerspeed, enemyspeed)

