import models.Position as Position


MAX_INTEGER = 100000

class triangle(object):
    def __init__(self, p1, p2, p3):
        self.p1 = Position.position(p1.x, p1.y)
        self.p2 = Position.position(p2.x, p2.y)
        self.p3 = Position.position(p3.x, p3.y)
    


def super_triangle(poslist):
    xmin = MAX_INTEGER
    ymin = MAX_INTEGER
    xmax = None
    ymax = None
    for pos in poslist:
        if pos.x < xmin:
            xmin = pos.x
        if pos.x > xmax:
            xmax = pos.x
        if pos.y < ymin:
            ymin = pos.y
        if pos.y > ymax:
            ymax = pos.y

    plg1 = Position.position(xmin, ymin)
    plg2 = Position.position(xmin, ymax)
    plg3 = Position.position(xmax, ymax)
    plg4 = Position.position(xmax, ymin)

    D = Position.position((xmax - xmin) / 2, ymax)


