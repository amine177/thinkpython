import shelve


def isanagram(s1, s2):

    if (nsort(s1) == nsort(s2)):
        return True
    return False


def nsort(s):
    return ''.join(sorted(list(s)))


def filetoanagrams(f):

    f = open(f)
    line = f.readline()
    d = {}
    for w in line.split():
        d.setdefault(nsort(w), [w]).append(w)

    return d
