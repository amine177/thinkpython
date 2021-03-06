import string
import choose_from_hist as rand_hist


def wordlist(file, skipHeader=True):

    line = file.readline()
    list = []
    if skipHeader:
        while not ("CHAPTER I" in line):
            line = file.readline()
        file.readline()
        file.readline()
    while line != "":
        line = line.replace('-', ' ')
        for i in line.split():
            i = i.strip(string.punctuation+string.whitespace)
            i = i.lower()
            if len(i) > 0:
                list.append(i)
        line = file.readline()
    return list


def histogram_sort(wordlist):

    histogram = {}
    for i in wordlist:
        histogram[i] = histogram.get(i, 0) + 1

    list = sorted(histogram.items(), key=lambda x:  x[1], reverse=True)
    return list


def histogram(wordlist):

    histogram = {}
    for i in wordlist:
        histogram[i] = histogram.get(i, 0) + 1

    return histogram


def toptwenty(wordlist, num=20):

    for i in range(num):
        print(wordlist[i][0])


def substruct(d1, d2):
    s1 = set(d1)
    s2 = set(d2)

    return list(s1.difference(s2))


if __name__ == "__main__":
    # print(wordlist(open("filetowords.py")))
    print(rand_hist.chose_hist(histogram(wordlist(open("emma.txt")))))
