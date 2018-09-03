def has_no_e(s):
    return 'e' in s


def avoids(s, f):
    for i in s:
        if i in f:
            return False
    return True


def uses_only(s, u):
    for i in s:
        if not (i in u):
            return False
    return True


def uses_all(s, u):
    for i in u:
        if not (i in s):
            return False
    return True


def is_abecedarian(s):
    if len(s) <= 1:
        return True
    if s[0] <= s[1]:
        return is_abecedarian(s[1:])
    else:
        return False


if __name__ == "__main__":
    f = open('words.txt')
    line = f.readline()[:-1]
    while (line != ""):
        if is_abecedarian(line):
            print(line)
        line = f.readline()[:-1]
