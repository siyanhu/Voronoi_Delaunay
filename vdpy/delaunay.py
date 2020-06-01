import math
import rangen
import models.Position as Position


input = rangen.ranPos(1,100,20)
if (len(input) < 3):
    print("Less than 3 vertices.\n")
else:
    xsorted = Position.position_shellsorted(input)