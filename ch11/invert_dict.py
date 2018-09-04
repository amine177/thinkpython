def invert_dict(d):
    inv = {}
    for i in d:
        if not (d[i] in inv):
            try:
                inv[d[i]] = i
            except TypeError:
                raise TypeError("value can't be a key")
        else:
            if isinstance(inv[d[i]], list):
                inv[d[i]].append(i)
            else:
                inv[d[i]] = [inv[d[i]]]
                inv[d[i]].append(i)

    return inv


if __name__ == "__main__":
    d = {1: 'a', 2: 'b', 'c': 'a'}
    print(invert_dict(d))
