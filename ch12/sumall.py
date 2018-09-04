def sumall(*arg):
    s = 0
    for i in arg:
        s += i

    return s


if __name__ == "__main__":
    print(sumall(1, 2, 3))
