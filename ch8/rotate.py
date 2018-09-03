def rotate(s, n):
    n = n % len(s)
    return s[-n:] + s[:-n]


if __name__ == '__main__':
    print(rotate("abc", 1))
    print(rotate("abc", 3))
