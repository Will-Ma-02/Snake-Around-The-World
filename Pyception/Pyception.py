import pygame, Constants, Colors, Coordinates, random
from Python import Python
from Food import Food
from Segment import Segment
pygame.init()

screen = pygame.display.set_mode([Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption("Pyception!")

python = Python(None)
food = Food(
    Coordinates.valid_coordinates_food[random.randint(0, 
    len(Coordinates.valid_coordinates_food) - 1)],
    Coordinates.valid_coordinates_food[random.randint(0, 
    len(Coordinates.valid_coordinates_food) - 1)],
    Constants.SEGMENT_SIZE
)

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
    if python.get_head_x() + Constants.SEGMENT_SIZE == food.get_x() and python.get_head_y() + Constants.SEGMENT_SIZE == food.get_y():
        if python.get_direction() == 'U':
            python.add_to_tail(Segment(python.get_head_x(), python.get_head_y() + Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
        elif python.get_direction() == 'D':
            python.add_to_tail(Segment(python.get_head_x(), python.get_head_y() - Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
        elif python.get_direction() == 'L':
            python.add_to_tail(Segment(python.get_head_x() + Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))
        elif python.get_direction() == 'R':
            python.add_to_tail(Segment(python.get_head_x() - Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))
        food.move_food()

def move():
    if python.get_direction() == None:
        return
    elif python.get_direction() == 'U':
        if python.len() == 1:
            new_y = python.get_head_y() - Constants.SEGMENT_SIZE
            python.get_head().set_y(new_y)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x(), python.get_head_y() - Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
    elif python.get_direction() == 'D':
        if python.len() == 1:
            new_y = python.get_head_y() + Constants.SEGMENT_SIZE
            python.get_head().set_y(new_y)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x(), python.get_head_y() + Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
    elif python.get_direction() == 'L':
        if python.len() == 1:
            new_x = python.get_head_x() - Constants.SEGMENT_SIZE
            python.get_head().set_x(new_x)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x() - Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))
    elif python.get_direction() == 'R':
        if python.len() == 1:
            new_x = python.get_head_x() + Constants.SEGMENT_SIZE
            python.get_head().set_x(new_x)
        else:
            python.remove_from_tail()
            python.add_to_head(Segment(python.get_head_x() + Constants.SEGMENT_SIZE, python.get_head_y(), Constants.SEGMENT_SIZE))

running = True
while running:
    timer.tick(10)
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
    pygame.display.update()
pygame.quit()
