import Coordinates, random

class Food:

    def __init__(self, x, y, size):
        self._x = x
        self._y = y
        self._size = size

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def move_food(self):
        self._x = Coordinates.VALID_COORDINATES[random.randint(1, len(Coordinates.VALID_COORDINATES) - 1)]
        self._y = Coordinates.VALID_COORDINATES[random.randint(1, len(Coordinates.VALID_COORDINATES) - 1)]