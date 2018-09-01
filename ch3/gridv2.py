def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_border():
    print('+' + (' -' * 4), end=' ')


def print_plus():
    print('+')


def print_bar():
    print('|' + ' ' * 8, end=' ')


def print_pipe():
    print('|')


def print_line():
    do_twice(print_bar)
    print_pipe()


def print_head():
    do_twice(print_border)
    print_plus()


def print_grid():
    print_head()
    do_four(print_line)
    print_head()
    do_four(print_line)
    print_head()


if __name__ == '__main__':
    print_grid()
