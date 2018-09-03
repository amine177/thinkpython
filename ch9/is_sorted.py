def is_sorted(t):
    i = 0
    while i < len(t) - 1:
        if (t[i] > t[i+1]):
            return False
        i += 1

    return True


if __name__ == "__main__":
    t = [1, 5, 3]
    print(is_sorted(t))
