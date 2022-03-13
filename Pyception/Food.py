import Coordinates, random

'''
Class: Food

A coordinate pair representing the position of the food.

Used in: Pyception
Subclasses: None
Superclasses: Object
'''
class Food:

    # Constructor
    def __init__(self, x : int, y : int, size : int):
        self._x = x
        self._y = y
        self._size = size

    # Getter for the x coordinate
    def get_x(self) -> int:
        return self._x

    # Getter for the y coordinate
    def get_y(self) -> int:
        return self._y
    
    # Moves the food to a new location
    def move_food(self) -> None:
        self._x = Coordinates.VALID_COORDINATES[random.randint(1, \
        len(Coordinates.VALID_COORDINATES) - 1)]
        self._y = Coordinates.VALID_COORDINATES[random.randint(1, \
        len(Coordinates.VALID_COORDINATES) - 1)]