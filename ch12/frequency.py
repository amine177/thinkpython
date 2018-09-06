def most_frequent(s):

    histogram = {}
    for i in s:
        histogram[i] = histogram.get(i, 0) + 1

    freq = []
    for l, f in histogram.items():
        freq.append((f, l))

    freq.sort(reverse=True)

    list = []
    for l in freq:
        list.append(l[1])

    return list


if __name__ == "__main__":
    print(most_frequent("abcaadddbbbbbbbbbdd"))
