import turtle
import math


def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)


def polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360 / n)


def circle(t, r):
    c = 2 * math.pi * r
    polygon(t, c / r, r)


if __name__ == '__main__':
    bob = turtle.Turtle()
    square(bob, 200)
    bob.clear()
    circle(bob, 100)
    turtle.mainloop()
