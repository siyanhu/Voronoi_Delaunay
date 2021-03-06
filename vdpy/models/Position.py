class position(object):
    x = -1.0
    y = -1.0
    z = -1.0

    def __init__(self, x, y, z=-1):
        if x:
            self.x = x
        if y:
            self.y = y
        if z:
            self.z = z

    def display(self):
        print("Position: " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "\n")

    def compareX(self, another_instance):
        """
        return the minimum instance
        """
        if (another_instance.x < self.x):
            return another_instance
        else:
            return self

    # def position_shellsorted_temp(self, poslist):
    #     if (len(poslist) <= 1):
    #         return poslist
    #     gap = len(poslist) / 2
    #     while (gap > 0):
    #         i = gap
    #         while (i < len(poslist)):
    #             j = i
    #             while (j - gap >= 0 & poslist[j] < poslist[j - gap]):
    #                 temp = poslist[j - gap]
    #                 poslist[j - gap] = poslist[j]
    #                 poslist[j] = temp
    #                 j = j - gap
    #             i = i + 1
    #         gap = gap / 2

def position_shellsorted_x(poslist):
    if (len(poslist) <= 1):
        return poslist
    gap = int(len(poslist) / 2)
    while (gap > 0):
        i = gap
        while(i < len(poslist)):
            j = i
            pos_j = poslist[j]
            pos_jg = poslist[j - gap]
            while (j - gap >= 0) and (pos_j.x < pos_jg.x):
                poslist[j - gap] = pos_j
                poslist[j] = pos_jg
                j = j - gap
                pos_j = poslist[j]
                pos_jg = poslist[j - gap]
            i = i + 1
        gap = int(gap / 2)
    return poslist

def position_shellsorted_y(poslist):
    if (len(poslist) <= 1):
        return poslist
    gap = int(len(poslist) / 2)
    while (gap > 0):
        i = gap
        while(i < len(poslist)):
            j = i
            pos_j = poslist[j]
            pos_jg = poslist[j - gap]
            while (j - gap >= 0) and (pos_j.y < pos_jg.y):
                poslist[j - gap] = pos_j
                poslist[j] = pos_jg
                j = j - gap
                pos_j = poslist[j]
                pos_jg = poslist[j - gap]
            i = i + 1
        gap = int(gap / 2)
    return poslist