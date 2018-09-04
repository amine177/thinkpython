def reverse_lookup(dic, v):
    for k in dic:
        if dic[k] == v:
            return k

        raise LookupError("No corresponding key for value")


if __name__ == "__main__":
    dic = {'a': 1, 'c': -2}
    print(reverse_lookup(dic, 3))
