from math import sqrt
from point import Point


class Circle:

    def __init__(self, c=Point(), r=1):
        self.c = c
        self.r = r

    def point_in_circle(self, p):
        return sqrt(p.x**2 + p.y**2) == self.r

    def rect_circle_overlap(self, r):
        # TODO
        pass
