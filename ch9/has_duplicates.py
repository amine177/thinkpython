def has_duplicates(s):

    i = 0
    while i < len(s) - 1:
        if s[i] in s[i+1:]:
            return True
        i += 1

    return False


if __name__ == "__main__":
    s = "abdc"
    print("has_duplicates({}) = {}".format(s, has_duplicates(s)))
