import turtle
from rectangle import Rectangle


def draw_rect(bf, r):
    for i in range(2):
        bf.fd(r.w)
        bf.lt(90)
        bf.fd(r.h)
        bf.lt(90)


if __name__ == "__main__":

    bf = turtle.Turtle()
    r = Rectangle(h=300, w=400)
    draw_rect(bf, r)
    turtle.mainloop()
