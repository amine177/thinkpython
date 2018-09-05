def structshape(struct):

    enumerate = {}
    structstring = ""
    iterable = {list: 'list', tuple: 'tuple', str: 'string',
                dict: 'dictionnary'}
    scalar = {int: 'int', float: 'float'}
    if type(struct) in iterable:
        structstring += iterable[type(struct)] + " of  "
    for i in struct:
        if type(i) in iterable:
            structstring += "[" + structshape(i) + "], "

        else:
            if scalar[type(i)] in enumerate:
                enumerate[scalar[type(i)]] += 1
            else:
                enumerate[scalar[type(i)]] = 1

    for i in enumerate:
        structstring += str(enumerate[i]) + ' ' + i + ' '

    return structstring


if __name__ == "__main__":
    print(structshape([1, {1: 2, 2: 1}, [1, 2, [1, 2]]]))
