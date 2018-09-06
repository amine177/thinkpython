import string


def wordlist(file):

    line = file.readline()
    list = []
    while line != "":
        line = line.strip(string.punctuation)
        for i in line.split():
            i = i.strip()
            if len(i) > 0:
                list.append(i)
        line = file.readline()
    return list


def histogram(wordlist):

    histogram = {}
    for i in wordlist:
        histogram[i] = histogram.get(i, 0) + 1

    list = sorted(histogram.items(), key=lambda x:  x[1], reverse=True)
    return list


def toptwenty(wordlist):

    for i in range(20):
        print(wordlist[i][0])


if __name__ == "__main__":
    # print(wordlist(open("filetowords.py")))
    toptwenty(histogram(wordlist(open("filetowords.py"))))
