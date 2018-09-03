def gcd(a, b):
    if b == 0 or a == b:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print("gcd(5, 2) = {}".format(gcd(5, 2)))
    print("gcd(175, 75) = {}".format(gcd(175, 75)))
