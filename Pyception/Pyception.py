import pygame, Constants, Colors, Coordinates, random
from Python import Python
from Food import Food
from Segment import Segment

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption("Pyception!")
score_font = pygame.font.Font("Fonts/Pixel.ttf", Constants.FONT_SIZES["SCORE"])
title_font = pygame.font.Font("Fonts/Pixel.ttf", Constants.FONT_SIZES["TITLE"])
text_font = pygame.font.Font("Fonts/Pixel.ttf", Constants.FONT_SIZES["TEXT"])

with open("Data/High_Score.txt", "r") as file1:
    lines = file1.readlines()
    high_score = int(lines[1].strip())

python = Python(None)
food = Food(
    Coordinates.VALID_COORDINATES[random.randint(1, 
    len(Coordinates.VALID_COORDINATES) - 1)],
    Coordinates.VALID_COORDINATES[random.randint(1, 
    len(Coordinates.VALID_COORDINATES) - 1)],
    Constants.SEGMENT_SIZE
)
score = 0

def draw_python():
    for segment in python.segments():
        if python.is_head(segment):
            rect = pygame.Rect(segment.get_x(), segment.get_y(), 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE)
            pygame.draw.rect(screen, Colors.GREEN, rect)
            if python.get_direction() == 'U':
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
            elif python.get_direction() == 'D':
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
            elif python.get_direction() == 'L':
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
            elif python.get_direction() == 'R':
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
                pygame.draw.circle(screen, Colors.BLACK, (segment.get_x() + 3 * Constants.SEGMENT_SIZE / 4, 
                segment.get_y() + 3 * Constants.SEGMENT_SIZE / 4), Constants.SEGMENT_SIZE / 5)
        else: 
            rect = pygame.Rect(segment.get_x(), segment.get_y(), 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE)
            pygame.draw.rect(screen, Colors.GREEN, rect)

def draw_food():
    pygame.draw.circle(screen, Colors.RED, 
    (food.get_x() - Constants.SEGMENT_SIZE / 2, 
    food.get_y() - Constants.SEGMENT_SIZE / 2), 
    Constants.SEGMENT_SIZE / 2)

def check_collisions():
    if python.get_head_x() + Constants.SEGMENT_SIZE == food.get_x() and \
        python.get_head_y() + Constants.SEGMENT_SIZE == food.get_y():
        if python.get_direction() == 'U':
            python.add_to_tail(Segment(python.get_head_x(), python.get_head_y() + 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
        elif python.get_direction() == 'D':
            python.add_to_tail(Segment(python.get_head_x(), python.get_head_y() - 
            Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
        elif python.get_direction() == 'L':
            python.add_to_tail(Segment(python.get_head_x() + 
            Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))
        elif python.get_direction() == 'R':
            python.add_to_tail(Segment(python.get_head_x() - 
            Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))
        food.move_food()
        global score
        score += 1
        return score
    for i in range(python.len() - 1, 0, -1):
        if python.get_head_x() == python.get_segment(i).get_x() and \
            python.get_head_y() == python.get_segment(i).get_y() and \
            python.len() > 1:
            global lines
            if score > high_score:
                with open("Data/High_Score.txt", "w") as file1:
                    lines[1] = str(score)
                    file1.writelines(lines)
            Constants.GAME_STATES["RUNNING"] = False
            Constants.GAME_STATES["END"] = True
    if python.get_head_x() < 0 or \
        python.get_head_x() > Constants.SCREEN_WIDTH - Constants.SEGMENT_SIZE or \
        python.get_head_y() < 0 or \
        python.get_head_y() > Constants.SCREEN_HEIGHT - Constants.SEGMENT_SIZE:
        if score > high_score:
            with open("Data/High_Score.txt", "w") as file1:
                lines[1] = str(score)
                file1.writelines(lines)
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
        with open("Data/High_Score.txt", "r") as file1:
            lines = file1.readlines()
            high_score = int(lines[1].strip())
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
        text = title_font.render("Pyception!", False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 3))
        screen.blit(text, text_rect)
        text = text_font.render("High score: {}".format(high_score), False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 2 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press Space to start", False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 3 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press Tab for settings", False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 0.65 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        pygame.display.update()
    
    elif Constants.GAME_STATES.get("SETTINGS"):
        screen.fill(Colors.BLACK)
        text = title_font.render("COMING SOON", False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 3))
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
        pygame.display.update()

    elif Constants.GAME_STATES.get("END"):
        with open("Data/High_Score.txt", "r") as file1:
            lines = file1.readlines()
            high_score = int(lines[1].strip())
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
        text = title_font.render("GAME OVER", False, Colors.RED)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 3))
        screen.blit(text, text_rect)
        text = text_font.render("Score: {}".format(score), False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 2 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("High score: {}".format(high_score), False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 0.45 * Constants.SCREEN_HEIGHT))
        screen.blit(text, text_rect)
        text = text_font.render("Press Space to play again", False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 3 * Constants.SCREEN_HEIGHT / 5))
        screen.blit(text, text_rect)
        text = text_font.render("Press S to return to start menu", False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 0.65 * Constants.SCREEN_HEIGHT))
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
        text = score_font.render("Score: {}".format(score), False, Colors.WHITE)
        text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 2 * Constants.SEGMENT_SIZE))
        screen.blit(text, text_rect)
        pygame.display.update()

file1.close()
pygame.quit()
