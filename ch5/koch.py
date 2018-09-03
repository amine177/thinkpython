import turtle


def koch(t, l):
    if (l < 10):
        t.fd(l)
        return
    m = l / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


if __name__ == '__main__':
    bob = turtle.Turtle()
    for i in range(3):
        koch(bob, 500)
        bob.rt(60)
    turtle.mainloop()
