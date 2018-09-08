from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
