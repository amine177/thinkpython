def has_duplicates(s):
    d = {}
    for i in s:
        if i in d:
            return True
        d[i] = 1
    return False


if __name__ == "__main__":
    s = "abdc"
    print("has_duplicates({}) = {}".format(s, has_duplicates(s)))
