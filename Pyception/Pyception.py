import pygame, pygame.freetype, Constants, Colors, Coordinates, random
from Python import Python
from Food import Food
from Segment import Segment

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption("Pyception!")
font = pygame.font.Font("Font.ttf", Constants.FONT_SIZE)

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
            global running
            running = False
            return running
    if python.get_head_x() < 0 or \
        python.get_head_x() > Constants.SCREEN_WIDTH - Constants.SEGMENT_SIZE or \
        python.get_head_y() < 0 or \
        python.get_head_y() > Constants.SCREEN_HEIGHT - Constants.SEGMENT_SIZE:
        running = False
        return running

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

running = True
while running:
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
    text = font.render("Score: {}".format(score), True, Colors.WHITE)
    text_rect = text.get_rect(center = (Constants.SCREEN_WIDTH / 2, 2 * Constants.SEGMENT_SIZE))
    screen.blit(text, text_rect)
    pygame.display.update()
pygame.quit()
