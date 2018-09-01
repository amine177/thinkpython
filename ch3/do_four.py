def do_twice(f, arg):
    f(arg)
    f(arg)


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


if __name__ == '__main__':
    do_four(print, "hello")
