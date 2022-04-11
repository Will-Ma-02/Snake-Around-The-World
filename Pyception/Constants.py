# Constants for the game

# Game window width in pixels
SCREEN_WIDTH = 800

# Game window height in pixels
SCREEN_HEIGHT = 800

# Total number of pixels in the game window
SCREEN_AREA = SCREEN_WIDTH * SCREEN_HEIGHT

# Size of one unit in pixels
SEGMENT_SIZE = 25

# How fast the game runs
TICK_RATE = 15

# The sizes of the text being rendered
FONT_SIZES = {
    "SCORE" : 40,
    "TITLE" : 70,
    "TEXT" : 30
}

# The states of the game
GAME_STATES = {
    "START" : True,
    "SETTINGS" : False,
    "PLAYING" : False,
    "END" : False
}