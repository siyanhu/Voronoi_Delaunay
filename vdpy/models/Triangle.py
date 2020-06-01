import models.Position as Position


MAX_INTEGER = 100000

class triangle(object):
    def __init__(self, p1, p2, p3):
        self.p1 = Position.position(p1.x, p1.y)
        self.p2 = Position.position(p2.x, p2.y)
        self.p3 = Position.position(p3.x, p3.y)


class vector(object):
    def __init__(self, p1, p2):
        self.p1 = Position.position(p1.x, p1.y)
        self.p2 = Position.position(p2.x, p2.y)

    def translation(self, var):
        self.p1.x = self.p1.x + var.x
        self.p2.x = self.p2.x + var.x
        self.p1.y = self.p1.y + var.y
        self.p2.y = self.p2.y + var.y

    def stretch(self, order, new_pos):
        if order == 0:
            self.p1 = new_pos
        else:
            self.p2 = new_pos



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

    o = Position.position(xmin, ymin)
    A = Position.position(xmin, ymax)
    B = Position.position(xmax, ymax)
    C = Position.position(xmax, ymin)

    D = Position.position((xmax - xmin) / 2, ymax)
    DO = vector(D, o)
    DC = vector(D, C)

    AD_length = abs(D.x - A.x)
    E = Position.position(o.x - AD_length, o.y)
    F = Position.position(C.x + AD_length, o.y)

    M_y = (D.y - o.y) * AD_length

