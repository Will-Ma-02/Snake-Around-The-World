import Constants, math

# All possible spawn coordinates for the random number generator

VALID_COORDINATES = [i for i in range(int(math.sqrt(Constants.SCREEN_AREA)))
if i % Constants.SEGMENT_SIZE == 0]
