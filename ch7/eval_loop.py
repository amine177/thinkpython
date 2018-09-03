def eval_loop():
    s = ''
    while (True):
        s = input("#")
        if (s == "done"):
            break
        eval(s)


if __name__ == '__main__':
    eval_loop()
