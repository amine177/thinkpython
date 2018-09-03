def ispower(a, b):
    if a < b:
        return False
    if a == b:
        return True
    if a % b != 0:
        return False
    else:
        return ispower(a/b, b)


if __name__ == "__main__":
    print("{} = x^{} : {}".format(25, 5, ispower(25, 5)))
    print("{} = x^{} : {}".format(24, 5, ispower(24, 5)))
