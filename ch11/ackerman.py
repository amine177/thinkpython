cache = {}


def ack(x, y):
    if (x, y) in cache:
        return cache[x, y]
    if x < 0 or y < 0:
        print("Invalid")
        return
    if x == 0:
        return y + 1
    elif y == 0:
        return ack(x-1, 1)
    elif x > 0 and y > 0:
        cache[x, y] = ack(x-1, ack(x, y-1))
        return cache[x, y]


if __name__ == '__main__':
    print("ack(3, 4) = {:d}".format(ack(2, 4)))
