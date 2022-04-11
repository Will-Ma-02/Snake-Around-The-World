import Colors
from configparser import ConfigParser

# All the necesary framework to manage the settings menu

# Initalize an instance of the ConfigParser and read from config file
config = ConfigParser()
config.read("Data/Saved_Data.ini")

# List of which options are active
ACTIVATED = [False, False, False]

# List of which options are blocked by another
BLOCKED = [False, False, False]

# List of which color is used
COLORS = [Colors.WHITE for _ in range(3)]

# List of indexes stored for each setting
INDEXES = [0 for _ in range(3)]

# Dictionary of all possible choices for each setting
CHOICES = {
    "SETTING1" : ["Green", "Blue", "Rainbow"],
    "SETTING2" : ["Red", "Yellow", "Magenta"],
    "SETTING3" : ["Top", "Bottom"]
}

# List of display strings for each setting
STRINGS = [
    "< {} >".format(config.get("Settings", "python_color")), 
    "< {} >".format(config.get("Settings", "food_color")), 
    "< {} >".format(config.get("Settings", "score_location"))
]

# List of options read from the config file
OPTIONS = [
    config.get("Settings", "python_color"),
    config.get("Settings", "food_color"),
    config.get("Settings", "score_location")
]