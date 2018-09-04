def middle(t):
    if len(t) <= 1:
        return []
    else:
        return t[1:-1]


if __name__ == "__main__":
    print(middle([1]))
    print(middle([1, 2, 3]))
    print(middle([1, 2, 3, 4]))
