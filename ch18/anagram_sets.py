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


def store_anagrams(dic, db):
    d = shelve.open(db, 'c')
    for i in dic.keys():
        d[i] = dic[i]


def read_anagrams(s, db):

    d = shelve.open(db)
    s = nsort(s)
    if s in d:
        return d[s]

    return None


if __name__ == "__main__":
    store_anagrams(filetoanagrams("anagram_sets.py"), "anargrams.db")
    print(read_anagrams("shelve", "anargrams.db"))
