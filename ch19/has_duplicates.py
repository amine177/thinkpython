def has_duplicates(s):
    return len(set(s)) < len(s)


if __name__ == "__main__":
    s = "abdc"
    print("has_duplicates({}) = {}".format(s, has_duplicates(s)))
