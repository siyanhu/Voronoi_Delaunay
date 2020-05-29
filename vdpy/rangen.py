from random import randrange
import models.Position as Position

def ranPos(min, max, count):
    i = 0
    rans = list()
    while(i < count):
        ranx = randrange(start=min, stop=max, step=1)
        rany = randrange(start=min, stop=max, step=1)
        pos = Position.position(x=ranx, y=rany)
        rans.append(pos)
        i = i + 1
    return rans