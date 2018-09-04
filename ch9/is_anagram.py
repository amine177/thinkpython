def anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    lst1 = []
    for i in s1:
        lst1.append(i)
    lst2 = []
    for i in s2:
        lst2.append(i)

    for i in lst1:
        if (i in lst2):
            lst2.remove(i)

    if len(lst2) == 0:
        return True

    return False


if __name__ == "__main__":
    print("anagram(abaa, aaba) = {}".format(anagram("baa", "aaba")))
