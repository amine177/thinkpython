import random


def randint(l, h):
    return round(l + random.random() * (h - l))


if __name__ == "__main__":
    for i in range(1000):
        print(randint(5, 10), end=" ")
