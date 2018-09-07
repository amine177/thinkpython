import filetowords as analyze
from math import log
import matplotlib.pyplot as plt


def rank(file):
    hist = analyze.histogram(analyze.wordlist(file))
    shist = [(key, value) for key, value in sorted(hist.items(),
                                                   key=lambda x: x[1],
                                                   reverse=True)]

    graph = []
    for i in range(len(shist)):
        graph.append((log(i+1), log(shist[i][1])))

    plt.plot(*zip(*graph))
    plt.show()


if __name__ == "__main__":
    f = open("emma.txt")
    rank(f)
