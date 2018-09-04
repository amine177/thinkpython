def histogram(s):
    dic = {}
    for i in s:
        if not (i in dic):
            dic[i] = 1
        else:
            dic[i] += 1

    return dic


if __name__ == "__main__":
    print(histogram("sdlfksdjfpwejfas;dfjkapoweifjaofe;"))
