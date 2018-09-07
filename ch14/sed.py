

def replace(p, r, f1, f2):

    f1 = open(f1, 'r')
    f2 = open(f2, 'w')
    line = f1.readline()
    while line != "":
        if p in line:
            line = line.replace(p, r)
        f2.write(line)

        line = f1.readline()

    f1.close()
    f2.close()


if __name__ == "__main__":
    replace("main", "itis", "sed.py", "failed.txt")
