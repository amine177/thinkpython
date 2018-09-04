def chop(t):
    if len(t) != 0:
        if len(t) == 1:
            t.pop(0)
        else:
            t.pop(0)
            t.pop(len(t)-1)


if __name__ == "__main__":
    t = [1, 2, 3]
    chop(t)
    print(t)
    t = []
    chop(t)
    print(t)
