from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


class Circle:

    def __init__(self, c=Point(), r=1):
        self.c = c
        self.r = r

    def point_in_circle(self, p):
        return sqrt(p.x**2 + p.y**2) == self.r

    def rect_circle_overlap(self, r):
        # TODO
        pass
