from collections import Counter


def anagram(s1, s2):
    return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    print("anagram(abaa, aaba) = {}".format(anagram("baa", "aaba")))
