# All possible spawn coordinates for the random number generator
import Constants

valid_coordinates_python = [i for i in range(800) if i % Constants.SEGMENT_SIZE == 0]
valid_coordinates_food = [i for i in range(25, 800) if i % Constants.SEGMENT_SIZE == 0]
