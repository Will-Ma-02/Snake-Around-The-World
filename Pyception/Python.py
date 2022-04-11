import Constants, Coordinates, random
from Segment import Segment

'''
Class: Python

The object used to represent the snake in the game.

Used in: Pyception
Subclasses: None
Superclasses: Object
'''
class Python:

    # Array that contains all the segments
    _segments = []

    # Constructor
    def __init__(self, direction : str):
        self._segments.append(Segment(
            Coordinates.VALID_COORDINATES[random.randint(0, 
            len(Coordinates.VALID_COORDINATES) - 1)], 
            Coordinates.VALID_COORDINATES[random.randint(0, 
            len(Coordinates.VALID_COORDINATES) - 1)], 
            Constants.SEGMENT_SIZE))
        self._direction = direction

    # Returns a pointer to the segemnts array
    def segments(self) -> list[Segment]:
        return self._segments

    # Getter for a specific segment 
    def get_segment(self, index : int) -> Segment:
        return self._segments[index]

    # Retruns the length of the python
    def len(self) -> int:
        return len(self._segments)

    # Getter for the direction
    def get_direction(self) -> int:
        return self._direction

    # Setter for the direction
    def set_direction(self, direction : str) -> None:
        self._direction = direction

    # Returns a pointer to the python's head
    def get_head(self) -> Segment:
        return self._segments[0]

    # Returns the head's x coordinate
    def get_head_x(self) -> int:
        return self._segments[0].get_x()

    # Returns the head's y coordinate
    def get_head_y(self) -> int:
        return self._segments[0].get_y()

    # Inserts a new head to the segments array
    def add_to_head(self, segment : Segment) -> None:
        self._segments.insert(0, segment)

    # Appends a new segment to the end of segments
    def add_to_tail(self, segment : Segment) -> None:
        self._segments.append(segment)

    # Removes the last segment in the array
    def remove_from_tail(self) -> None:
        del self._segments[-1]

    # Checks if the argument is pointing to the head
    def is_head(self, segment : Segment) -> bool:
        return segment == self._segments[0]

    # Resets the python to its initial state
    def reset(self) -> None:
        self._segments.clear()
        self._segments.append(Segment(
            Coordinates.VALID_COORDINATES[random.randint(0, 
            len(Coordinates.VALID_COORDINATES) - 1)], 
            Coordinates.VALID_COORDINATES[random.randint(0, 
            len(Coordinates.VALID_COORDINATES) - 1)], 
            Constants.SEGMENT_SIZE))
        self._direction = None