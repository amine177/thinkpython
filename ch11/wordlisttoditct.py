def dictify(file):

    dict = {}
    line = file.readline()[:-1]
    while line != "":
        dict[line] = 1
        line = file.readline()[:-1]

    return dict


if __name__ == "__main__":
    print(len(dictify(open("words.txt", "r"))))
