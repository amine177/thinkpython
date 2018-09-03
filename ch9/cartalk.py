def is_consecutive_double(s):
    i = 0
    c = 0
    while i < len(s) - 1:
        if (s[i] == s[i+1]):
            c += 1
            i += 2
        else:
            c = 0
            i += 1
        if c == 3:
            return True

    return False


if __name__ == "__main__":
    f = open('words.txt')
    line = f.readline()[:-1]
    while (line != ""):
        if is_consecutive_double(line):
            print(line)
        line = f.readline()[:-1]
