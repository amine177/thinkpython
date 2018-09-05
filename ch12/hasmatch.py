def hasmatch(s1, s2):
    for i, j in zip(s1, s2):
        if i == j:
            return True

    return False


if __name__ == "__main__":
    print(hasmatch('abc', 'xdc'))
