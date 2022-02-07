import Colors
from configparser import ConfigParser

# All the necesary framework to manage the settings menu

config = ConfigParser()
config.read("Data/Saved_Data.ini")

ACTIVATED = [False, False, False]
BLOCKED = [False, False, False]
COLORS = [Colors.WHITE for _ in range(3)]
CHOICES = {
    "SETTING1" : ["Green", "Blue", "Rainbow"],
    "SETTING2" : ["Red", "Yellow", "Magenta"],
    "SETTING3" : ["Top", "Bottom"]
}
STRINGS = [
    "< {} >".format(config.get("Settings", "python_color")), 
    "< {} >".format(config.get("Settings", "food_color")), 
    "< {} >".format(config.get("Settings", "score_location"))
]
OPTIONS = [
    config.get("Settings", "python_color"),
    config.get("Settings", "food_color"),
    config.get("Settings", "score_location")
]
INDEXES = [0 for _ in range(3)]