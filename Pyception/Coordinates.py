import Constants, math

# All possible spawn coordinates for the random number generator

# Constraint: Food cannot index VALID_COORDINATES[0] or else it will 
# cause it to spawn off screen

VALID_COORDINATES = [i for i in range(int(math.sqrt(Constants.SCREEN_AREA)))
if i % Constants.SEGMENT_SIZE == 0]
