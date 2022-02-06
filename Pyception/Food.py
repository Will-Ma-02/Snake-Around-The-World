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
        self._x = Coordinates.valid_coordinates_food[random.randint(0, len(Coordinates.valid_coordinates_food) - 1)]
        self._y = Coordinates.valid_coordinates_food[random.randint(0, len(Coordinates.valid_coordinates_food) - 1)]