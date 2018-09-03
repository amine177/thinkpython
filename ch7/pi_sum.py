import math


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def pi(n):
    x = ((2 * math.sqrt(2)) / 9801) * 1103
    i = 1
    while i < n:
        x += factorial(4*i) * (1103 + 26390 * i) \
            / (factorial(i)**4 * 396**(4*i))
        i += 1
    return x


if __name__ == '__main__':
    print(1/pi(100))
