def apply(f, arg):
    f(arg)


def print_value(value):
    print(value)


if __name__ == '__main__':
    apply(print_value, 'hello')
