# Import all necessary modules
import pygame, Constants, Colors, Coordinates, Options, random
from pygame import mixer
from configparser import ConfigParser
from Python import Python
from Food import Food
from Segment import Segment

# Initalize pygame and some dependencies
pygame.init()
mixer.init()
pygame.font.init()

# Initalize and configure game variables
screen = pygame.display.set_mode([Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT])
timer = pygame.time.Clock()
config = ConfigParser()
config.read("Data/Saved_Data.ini")
high_score = int(config.get("High_Score", "high_score"))
score = 0

# Initalize and configure font objects
score_font = pygame.font.Font("Fonts/Pixel.ttf", Constants.FONT_SIZES["SCORE"])
title_font = pygame.font.Font("Fonts/Pixel.ttf", Constants.FONT_SIZES["TITLE"])
text_font = pygame.font.Font("Fonts/Pixel.ttf", Constants.FONT_SIZES["TEXT"])

# Instantiate game objects
python = Python(None)
food = Food(
    Coordinates.VALID_COORDINATES[random.randint(1, 
    len(Coordinates.VALID_COORDINATES) - 1)],
    Coordinates.VALID_COORDINATES[random.randint(1, 
    len(Coordinates.VALID_COORDINATES) - 1)],
    Constants.SEGMENT_SIZE
)

# Initalize sound for the game
pygame.mixer.music.load("Sounds/Background.wav")
pygame.mixer.music.play(-1, 0.0)

# Set the window name
pygame.display.set_caption("Pyception!")

'''
Function: Draws the python (snake) in the game

Arguments: None
Returns: None
'''
def draw_python():

    # Initalize the python's color variable
    python_color = None

    # Color is green
    if Options.OPTIONS[0] == Options.CHOICES.get("SETTING1")[0]:
        python_color = Colors.GREEN

    # Color is blue
    elif Options.OPTIONS[0] == Options.CHOICES.get("SETTING1")[1]:
        python_color = Colors.BLUE

    # Color is rainbow
    elif Options.OPTIONS[0] == Options.CHOICES.get("SETTING1")[2]:
        python_color = tuple(random.randint(0, 255) for _ in range(3))

    # For each segment in the python, draw it on the screen
    for segment in python.segments():

        # If the segment is the head
        if python.is_head(segment):
            rect = pygame.Rect(segment.get_x(), segment.get_y(), 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE)
            pygame.draw.rect(screen, python_color, rect)

            # Draw eyes that face up if the python's direction is 'U'
            if python.get_direction() == 'U':
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)

            # Draw eyes that face down if the python's direction is 'D'
            elif python.get_direction() == 'D':
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)

            # Draw eyes that face to the left if the python's direction is 'L'
            elif python.get_direction() == 'L':
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                
            # Draw eyes that face to the left if the python's direction is 'R'
            elif python.get_direction() == 'R':
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, 
                (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)

        # If the segment is not the head
        else: 
            rect = pygame.Rect(segment.get_x(), segment.get_y(), 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE)
            pygame.draw.rect(screen, python_color, rect)

'''
Function: Draw the food in the game

Arguments: None
Returns: None
'''
def draw_food():

    # Initalize the python's color variable
    food_color = None

    # Color is red
    if Options.OPTIONS[1] == Options.CHOICES.get("SETTING2")[0]:
        food_color = Colors.RED

    # Color is yellow
    elif Options.OPTIONS[1] == Options.CHOICES.get("SETTING2")[1]:
        food_color = Colors.YELLOW

    # Color is magenta
    elif Options.OPTIONS[1] == Options.CHOICES.get("SETTING2")[2]:
        food_color = Colors.MAGENTA

    # Draw the food on the screen
    pygame.draw.circle(screen, food_color, 
    (food.get_x() - Constants.SEGMENT_SIZE / 2, 
    food.get_y() - Constants.SEGMENT_SIZE / 2), 
    Constants.SEGMENT_SIZE / 2)

'''
Function: Draw the score in the game

Arguments: None
Returns: None
'''
def draw_score():

    # If the score should be drawn on the top of the screen
    if Options.OPTIONS[2] == Options.CHOICES.get("SETTING3")[0]:
        text = score_font.render("Score: {}".format(score), False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 2 * Constants.SEGMENT_SIZE))
        screen.blit(text, text_rect)

    # If the score should be drawn on the bottom of the screen
    elif Options.OPTIONS[2] == Options.CHOICES.get("SETTING3")[1]:
        text = score_font.render("Score: {}".format(score), False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT - 
        2 * Constants.SEGMENT_SIZE))
        screen.blit(text, text_rect)

'''
Function: Dectect all collisions in the game

Collisions include:
The python ate food
The python hit a wall
The python ate itself

Arguments: None
Returns: a new score 
'''
def check_collisions():

    # Check if the python ate food
    if python.get_head_x() + Constants.SEGMENT_SIZE == food.get_x() and \
        python.get_head_y() + Constants.SEGMENT_SIZE == food.get_y():

        # Grow the python if it is moving up
        if python.get_direction() == 'U':
            python.add_to_tail(Segment(python.get_head_x(), python.get_head_y() + 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
        
        # Grow the python if it is moving down
        elif python.get_direction() == 'D':
            python.add_to_tail(Segment(python.get_head_x(), python.get_head_y() - 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))

        # Grow the python if it is moving left
        elif python.get_direction() == 'L':
            python.add_to_tail(Segment(python.get_head_x() + 
            Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))

        # Grow the python if it is moving right
        elif python.get_direction() == 'R':
            python.add_to_tail(Segment(python.get_head_x() - 
            Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))

        # Move food to a new location and increment score
        food.move_food()
        global score
        score += 1
        return score
    
    # Loop through all segments of the python
    for i in range(python.len() - 1, 0, -1):

        # Check if any segment collided with the head
        if python.get_head_x() == python.get_segment(i).get_x() and \
            python.get_head_y() == python.get_segment(i).get_y() and \
            python.len() > 1:

            # if the current score is higher than the high score, overwrite it
            if score > high_score:
                config.set("High_Score", "high_score", str(score))

            # Initalize game over 
            Constants.GAME_STATES["RUNNING"] = False
            Constants.GAME_STATES["END"] = True

     # Check if the head went out of bounds (hit a wall)
    if python.get_head_x() < 0 or \
        python.get_head_x() > Constants.SCREEN_WIDTH - Constants.SEGMENT_SIZE or \
        python.get_head_y() < 0 or \
        python.get_head_y() > Constants.SCREEN_HEIGHT - Constants.SEGMENT_SIZE:

        # if the current score is higher than the high score, overwrite it
        if score > high_score:
            config.set("High_Score", "high_score", str(score))

        # Initalize game over 
        Constants.GAME_STATES["RUNNING"] = False
        Constants.GAME_STATES["END"] = True

def move():
    if python.get_direction() == None:
        return
    elif python.get_direction() == 'U':
        if python.len() == 1:
            new_y = python.get_head_y() - Constants.SEGMENT_SIZE
            python.get_head().set_y(new_y)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x(), python.get_head_y() - 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
    elif python.get_direction() == 'D':
        if python.len() == 1:
            new_y = python.get_head_y() + Constants.SEGMENT_SIZE
            python.get_head().set_y(new_y)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x(), python.get_head_y() + 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
    elif python.get_direction() == 'L':
        if python.len() == 1:
            new_x = python.get_head_x() - Constants.SEGMENT_SIZE
            python.get_head().set_x(new_x)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x() - 
            Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))
    elif python.get_direction() == 'R':
        if python.len() == 1:
            new_x = python.get_head_x() + Constants.SEGMENT_SIZE
            python.get_head().set_x(new_x)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x() + 
            Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))

def reset_game():
    python.reset()
    food.move_food()
    global score
    score = 0

running = True
while running:
    if Constants.GAME_STATES.get("START"):
        high_score = int(config.get("High_Score", "high_score"))
        screen.fill(Colors.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    Constants.GAME_STATES["START"] = False
                    Constants.GAME_STATES["PLAYING"] = True
                elif event.key == pygame.K_TAB:
                    Constants.GAME_STATES["START"] = False
                    Constants.GAME_STATES["SETTINGS"] = True
                elif event.key == pygame.K_BACKSPACE:
                    running = False
        text = title_font.render("Pyception!", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 3))
        screen.blit(text, text_rect)
        text = text_font.render("High score: {}".format(high_score), False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 2 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press Space to play", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 3 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press Tab for settings", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.65 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render("Press Backspace to exit", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 7 * Constants.SCREEN_HEIGHT / 10))
        screen.blit(text, text_rect)
        text = text_font.render("Version 1.1", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.95 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        pygame.display.update()
    
    elif Constants.GAME_STATES.get("SETTINGS"):
        screen.fill(Colors.BLACK)
        text = title_font.render("Settings", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 6))
        screen.blit(text, text_rect)
        text = text_font.render("Press Space to play", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 4 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press S to return to start menu", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.85 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render("Press Backspace to exit", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 9 * Constants.SCREEN_HEIGHT / 10))
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    Constants.GAME_STATES["SETTINGS"] = False
                    Constants.GAME_STATES["PLAYING"] = True
                elif event.key == pygame.K_s:
                    Constants.GAME_STATES["SETTINGS"] = False
                    Constants.GAME_STATES["START"] = True
                elif event.key == pygame.K_BACKSPACE:
                    running = False
                elif event.key == pygame.K_1 and not Options.BLOCKED[0]:
                    if Options.ACTIVATED[0]:
                        Options.COLORS[0] = Colors.WHITE
                        Options.ACTIVATED[0] = False
                        Options.BLOCKED[1] = False
                        Options.BLOCKED[2] = False
                    else:
                        Options.COLORS[0] = Colors.MAGENTA
                        Options.ACTIVATED[0] = True
                        Options.BLOCKED[1] = True
                        Options.BLOCKED[2] = True
                elif event.key == pygame.K_2 and not Options.BLOCKED[1]:
                    if Options.ACTIVATED[1]:
                        Options.COLORS[1] = Colors.WHITE
                        Options.ACTIVATED[1] = False
                        Options.BLOCKED[0] = False
                        Options.BLOCKED[2] = False
                    else:
                        Options.COLORS[1] = Colors.MAGENTA
                        Options.ACTIVATED[1] = True
                        Options.BLOCKED[0] = True
                        Options.BLOCKED[2] = True
                elif event.key == pygame.K_3 and not Options.BLOCKED[2]:
                    if Options.ACTIVATED[2]:
                        Options.COLORS[2] = Colors.WHITE
                        Options.ACTIVATED[2] = False
                        Options.BLOCKED[0] = False
                        Options.BLOCKED[1] = False
                    else:
                        Options.COLORS[2] = Colors.MAGENTA
                        Options.ACTIVATED[2] = True
                        Options.BLOCKED[0] = True
                        Options.BLOCKED[1] = True
                elif event.key == pygame.K_RIGHT and Options.ACTIVATED[0]:
                    Options.INDEXES[0] += 1 
                    if Options.INDEXES[0] >= len(Options.CHOICES.get("SETTING1")):
                        Options.INDEXES[0] = 0
                    Options.STRINGS[0] = "< {} >" \
                    .format(Options.CHOICES.get("SETTING1")[Options.INDEXES[0]])
                    Options.OPTIONS[0] = Options.CHOICES.get("SETTING1")[Options.INDEXES[0]]
                    config.set("Settings", "python_color", Options.OPTIONS[0])
                elif event.key == pygame.K_LEFT and Options.ACTIVATED[0]:
                    Options.INDEXES[0] -= 1 
                    if Options.INDEXES[0] < 0:
                        Options.INDEXES[0] = len(Options.CHOICES.get("SETTING1")) - 1
                    Options.STRINGS[0] = "< {} >" \
                    .format(Options.CHOICES.get("SETTING1")[Options.INDEXES[0]])
                    Options.OPTIONS[0] = Options.CHOICES.get("SETTING1")[Options.INDEXES[0]]
                    config.set("Settings", "python_color", Options.OPTIONS[0])
                elif event.key == pygame.K_RIGHT and Options.ACTIVATED[1]:
                    Options.INDEXES[1] += 1 
                    if Options.INDEXES[1] >= len(Options.CHOICES.get("SETTING2")):
                        Options.INDEXES[1] = 0
                    Options.STRINGS[1] = "< {} >" \
                    .format(Options.CHOICES.get("SETTING2")[Options.INDEXES[1]])
                    Options.OPTIONS[1] = Options.CHOICES.get("SETTING2")[Options.INDEXES[1]]
                    config.set("Settings", "food_color", Options.OPTIONS[1])
                elif event.key == pygame.K_LEFT and Options.ACTIVATED[1]:
                    Options.INDEXES[1] -= 1 
                    if Options.INDEXES[1] < 0:
                        Options.INDEXES[1] = len(Options.CHOICES.get("SETTING2")) - 1
                    Options.STRINGS[1] = "< {} >" \
                    .format(Options.CHOICES.get("SETTING2")[Options.INDEXES[1]])
                    Options.OPTIONS[1] = Options.CHOICES.get("SETTING2")[Options.INDEXES[1]]
                    config.set("Settings", "food_color", Options.OPTIONS[1])
                elif event.key == pygame.K_RIGHT and Options.ACTIVATED[2]:
                    Options.INDEXES[2] += 1 
                    if Options.INDEXES[2] >= len(Options.CHOICES.get("SETTING3")):
                        Options.INDEXES[2] = 0
                    Options.STRINGS[2] = "< {} >" \
                    .format(Options.CHOICES.get("SETTING3")[Options.INDEXES[2]])
                    Options.OPTIONS[2] = Options.CHOICES.get("SETTING3")[Options.INDEXES[2]]
                    config.set("Settings", "score_location", Options.OPTIONS[2])
                elif event.key == pygame.K_LEFT and Options.ACTIVATED[2]:
                    Options.INDEXES[2] -= 1 
                    if Options.INDEXES[2] < 0:
                        Options.INDEXES[2] = len(Options.CHOICES.get("SETTING3")) - 1
                    Options.STRINGS[2] = "< {} >" \
                    .format(Options.CHOICES.get("SETTING3")[Options.INDEXES[2]])
                    Options.OPTIONS[2] = Options.CHOICES.get("SETTING3")[Options.INDEXES[2]]
                    config.set("Settings", "score_location", Options.OPTIONS[2])

        text = text_font.render("1: Python Color:", False, Options.COLORS[0])
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.35 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render(Options.STRINGS[0], False, Options.COLORS[0])
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 2 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("2: Food Color:", False, Options.COLORS[1])
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.45 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render(Options.STRINGS[1], False, Options.COLORS[1])
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2))
        screen.blit(text, text_rect)
        text = text_font.render("3: Score Location:", False, Options.COLORS[2])
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.55 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render(Options.STRINGS[2], False, Options.COLORS[2])
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 3 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)  
        pygame.display.update()

    elif Constants.GAME_STATES.get("END"):
        high_score = int(config.get("High_Score", "high_score"))
        screen.fill(Colors.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    Constants.GAME_STATES["END"] = False
                    Constants.GAME_STATES["PLAYING"] = True
                elif event.key == pygame.K_s:
                    Constants.GAME_STATES["END"] = False
                    Constants.GAME_STATES["START"] = True
                elif event.key == pygame.K_BACKSPACE:
                    running = False
        text = title_font.render("GAME OVER", False, Colors.RED)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 3))
        screen.blit(text, text_rect)
        text = text_font.render("Score: {}".format(score), False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 2 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("High score: {}".format(high_score), False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.45 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render("Press Space to play again", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 3 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press S to return to start menu", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 0.65 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render("Press Backspace to exit", False, Colors.WHITE)
        text_rect = text.get_rect(center = 
        (Constants.SCREEN_WIDTH / 2, 7 * Constants.SCREEN_HEIGHT / 10))
        screen.blit(text, text_rect)
        pygame.display.update()

    elif Constants.GAME_STATES.get("PLAYING"):
        timer.tick(Constants.TICK_RATE)
        move()
        screen.fill(Colors.BLACK)
        draw_python()
        draw_food()
        check_collisions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and python.get_direction() != 'D':
                    python.set_direction('U')
                elif event.key == pygame.K_DOWN and python.get_direction() != 'U':
                    python.set_direction('D')
                elif event.key == pygame.K_LEFT and python.get_direction() != 'R':
                    python.set_direction('L')
                elif event.key == pygame.K_RIGHT and python.get_direction() != 'L':
                    python.set_direction('R')
        draw_score()
        pygame.display.update()

with open("Data/Saved_Data.ini", "w") as data:
    config.write(data)
data.close()
pygame.quit()
