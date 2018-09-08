import shelve


def isanagram(s1, s2):

    if (nsort(s1) == nsort(s2)):
        return True
    return False


def nsort(s):
    return ''.join(sorted(list(s)))
