def rot(s, n):
    n = n % 26

    ret = ""
    for i in s:
        ret += chr(ord(i) + n)
    return ret


if __name__ == "__main__":
    print(rot("abc", 13))
