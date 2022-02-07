# Constants for the game
# Constraint: SCREEN_WIDTH and SCREEN_HEIGHT must be the same value
# Constraint: SCREEN_WIDTH and SCREEN_HEIGHT must be divisble by SEGMENT_SIZE

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_AREA = SCREEN_WIDTH * SCREEN_HEIGHT
SEGMENT_SIZE = 25
TICK_RATE = 10
FONT_SIZES = {
    "SCORE": 40,
    "TITLE": 70,
    "TEXT": 30
}
GAME_STATES = {
    "START" : True,
    "SETTINGS" : False,
    "PLAYING" : False,
    "END" : False
}