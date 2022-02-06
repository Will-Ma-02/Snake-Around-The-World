import Constants, Coordinates, random
from Segment import Segment

class Python:

    _segments = []

    # Constructor
    def __init__(self, direction):
        self._segments.append(Segment(
            Coordinates.valid_coordinates_python[random.randint(0, 
            len(Coordinates.valid_coordinates_python) - 1)], 
            Coordinates.valid_coordinates_python[random.randint(0, 
            len(Coordinates.valid_coordinates_python) - 1)], 
            Constants.SEGMENT_SIZE))
        self._direction = direction

    def segments(self):
        return self._segments

    def len(self):
        return len(self._segments)

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def get_head(self):
        return self._segments[0]

    def get_head_x(self):
        return self._segments[0].get_x()

    def get_head_y(self):
        return self._segments[0].get_y()

    def add_to_head(self, segment):
        self._segments.insert(0, segment)

    def add_to_tail(self, segment):
        self._segments.append(segment)

    def remove_from_tail(self):
        del self._segments[-1]

    def is_head(self, segment):
        return segment == self._segments[0]