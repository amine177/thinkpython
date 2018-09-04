

def rotate(s, n):
    n = n % len(s)
    return s[-n:] + s[:-n]


def rotate_pairs(f):
    dict = {}
    line = f.readline()[:-1]
    while line != "":
        isthere = False
        for j in range(len(line)):
            rot = rotate(line, j)
            if rot in dict:
                dict[rot].append(line)
                isthere = True
        if not isthere:
            dict[line] = [line]

        line = f.readline()[:-1]

    return dict


if __name__ == "__main__":
    d = rotate_pairs(open("words.txt"))
    for i in d.values():
        if len(i) > 1:
            print(i)
