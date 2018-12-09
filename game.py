import pygame as pg
from pygame.time import Clock
from recursive_backtracker import recursive_backtracker
from simple_generator import simple_generator
from recursive_division import recursive_division


class Wall:
    # Function: Class for one rectangular potion of the walls of the maze
    # Arguments:
    #   x: Position of left side of wall section
    #   y: Position of top of wall section
    #   rect: Defines rectangle of the wall
    # Returns: None, draws 20 by 20 black wall at specified x, y position
    def __init__(self, x, y, rect):
        self.image = pg.display.get_surface()
        self.rect = rect
        self.x = x
        self.y = y
        pg.draw.rect(self.image, (0, 0, 0), [x, y, 20, 20])


class Player:
    # Function: Class for player and enemy, a square
    # Arguments:
    #   screen: screen to be drawn on
    #   color: color of the square Player
    #   surface: Surface of the player
    #   image: draws player with specificed color and size on specified display
    # Returns: None, draws Player on screen
    def __init__(self, screen, color, rect, speed):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.surface = pg.Surface(self.rect.size)
        self.image = pg.draw.rect(self.screen, self.color, self.rect)
        self.speed = speed

    def update(self):
        # Function: Updates the image of the player on the screen
        # Arguments: None
        # Returns: None, redraws Player
        pg.draw.rect(self.screen, self.color, self.rect)


def enemy_function(screen, enemy_object, player_object):
    # Function: Controls the enemy as well as tracks end conditions
    # Arguments:
    #   screen: screen that enemy is drawn on
    #   enemy_object: Object of class Player representing the enemy
    #   player_object: Object of class Player representing the player
    # Returns:
    #   done_flag: Tracks if player wins or loses
    #   Prints if you win or lose based on end condition

    done_flag = False
    player_rect = player_object.rect
    player_position = player_x, player_y = player_rect.x, player_rect.y
    enemy_rect = enemy_object.rect
    enemy_position = enemy_x, enemy_y = enemy_rect.x, enemy_rect.y
    # Compares the position of the enemy to the position of the player
    # Moves the enemy towards the player based on the relative x and y distance they are apart
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
    # Loses the game if player touches enemy
    if enemy_rect.colliderect(player_rect):
        results_screen(screen, "GAME OVER")
        done_flag = True
    if enemy_position != player_position:
        enemy_rect.move_ip(increment_x, increment_y)
        enemy_object.update()
    # Wins the game if the player moves out of the lower or right bounds of the screen
    if player_x > screen.get_width() or player_y > screen.get_height():
        results_screen(screen, "YOU WIN")
        done_flag = True
    return done_flag


def text_objects(text, font):
    # Function: Sets up surface and rectangle of the text that will be drawn on screen
    # Arguments:
    #   text: The text that is to be drawn on the screen
    #   font: what font the text that is drawn should be
    # Returns:
    #   textSurface: Surface of the text
    #   textSurface.get_rect(): The rectangle of the text
    # Function from link below, made text drawing simpler
    # https: // pythonprogramming.net / displaying - text - pygame - screen /
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def results_screen(screen, text_result):
    # Function: Draws the results text on the screen for the end conditions after being set up by text_objects
    # Arguments:
    #   screen: display that text will be drawn on
    #   text_result: The results text that will be shown on the screen
    # Returns: None, draws the results text in the center of the screen
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    screen.fill((255, 255, 255))  # Whites out screen first
    pg.font.init()
    # Win or lose display
    result_font = pg.font.Font('FreeSansBold.ttf', 115)
    text_surface, text_rect = text_objects(text_result, result_font)
    text_rect.center = (screen_width / 2, screen_height / 3)  # Position of the drawn text
    screen.blit(text_surface, text_rect)
    # Press enter to quit prompt
    quit_font = pg.font.Font('FreeSansBold.ttf', 60)
    quit_surface, quit_rect = text_objects('Press Enter to Quit', quit_font)
    quit_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(quit_surface, quit_rect)


def choose_generator(n):
    # Function: Chooses which maze generation algorithm to use
    # Arguments:
    #   n: A number from 1 to 3 that corresponds to an algorithm, from user input
    # Returns: Generator that will be used
    if n == 1:
        return simple_generator()
    elif n == 2:
        return recursive_division()
    elif n == 3:
        return recursive_backtracker()


def create_maze(generator_type):
    # Function: Draws the walls of the maze from a matrix of Trues and Falses from the generation algorithm
    # Arguments:
    #   generator_type: the algorithm used to create the maze
    # Returns:
    #   screen: screen filled with walls of maze
    #   walls: List of wall objects
    White = (255, 255, 255)
    maze = choose_generator(generator_type)
    side_length = maze.shape[0]
    size = maze.shape[0] * 20
    screen = pg.display.set_mode((size, size))
    screen.fill(White)
    walls = []
    # Checks every entry in true false matrix
    # Creates a wall object from the Wall class if the value in the matrix is True
    for i in range(0, side_length):
        for j in range(0, side_length):
            if maze[i, j]:
                wall = Wall(i * 20, j * 20, pg.Rect(i * 20, j * 20, 20, 20))
                walls.append(wall.rect)
    return screen, walls


def movement(screen, player, walls, desired_movement, bounce_movement):
    # Function: Moves player rectangle, updates the image of the rectangle, and handles wall collisions
    # Arguments:
    #   screen: screen that the player is drawn on
    #   player: Object of Player class representing the player
    #   walls: list of wall objects, used to check for collisions
    #   desired_movement: Move many pixels the player should move when a key is pressed
    #   bounce_movement: how far the player moves when they collide with a wall
    player.rect.move_ip(desired_movement)
    if player.rect.collidelist(walls) != -1:
        player.rect.move_ip(bounce_movement)
        player.update()
    else:
        screen.blit(background, (0, 0))
        player.update()


def run_maze(generator_type, p_speed, e_speed):
    # Function: The main game loop, creates screen and handles all inputs
    # Arguments:
    #   generator_type: which maze generation algorithm to used to create the maze
    #   p_speed: speed of the player
    #   e_speed: speed of the enemy
    # Returns: None, opens and runs game
    clock = Clock()
    frame_rate = 30
    screen, walls = create_maze(generator_type)
    # Stores copy of maze with no player or enemy as background
    global background
    background = screen.copy()
    # Initializes player and enemy
    player = Player(screen, (0, 0, 255), pg.rect.Rect(10, 46, 7, 7), p_speed)
    enemy = Player(screen, (255, 0, 0), pg.rect.Rect(350, 350, 7, 7), e_speed)
    pg.key.set_repeat(30, 30)
    # Sets up run conditions
    running = True
    done_flag = False
    while running:
        # Used link below to learn how to register keypresses and allow the user to exit the game
        # https: // opensource.com / article / 17 / 12 / game - python - moving - player
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                # Handles player movement
                screen.blit(background, (0, 0))
                player.update()
                if not done_flag:
                    # A or left arrow to move left
                    if (event.key == pg.K_a or event.key == pg.K_LEFT):
                        movement(screen, player, walls, (-player.speed, 0), (player.speed, 0))
                    # D or right arrow to move right
                    if (event.key == pg.K_d or event.key == pg.K_RIGHT):
                        movement(screen,     player, walls, (player.speed, 0), (-player.speed, 0))
                    # S or down arrow to move down
                    if (event.key == pg.K_s or event.key == pg.K_DOWN):
                        movement(screen, player, walls, (0, player.speed), (0, -player.speed))
                    # W or up arrow to move up
                    if (event.key == pg.K_w or event.key == pg.K_UP):
                        movement(screen, player, walls, (0, -player.speed), (0, player.speed))
                if event.key == pg.K_RETURN: # Press enter to quit game
                    running = False
                done_flag = enemy_function(screen, enemy, player) # Enemy moves, checks end game conditions
            elif event.type == pg.QUIT:
                running = False
        pg.display.flip()
        clock.tick(frame_rate)
