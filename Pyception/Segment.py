'''
Class: Segment

A coordinate pair representing the position of one of the
parts of the python.

Used in: Python, Pyception
Subclasses: None
Superclasses: Object
'''
class Segment:

    # Constructor
    def __init__(self, x, y, size):
        self._x = x
        self._y = y
        self._size = size

    # Getter for x coordinate
    def get_x(self):
        return self._x

    # Setter for x coordinate
    def set_x(self, x):
        self._x = x
    
    # Getter for y coordinate
    def get_y(self):
        return self._y

    # Setter for y coordinate
    def set_y(self, y):
        self._y = y

    # Getter for size
    def get_size(self):
        return self._size