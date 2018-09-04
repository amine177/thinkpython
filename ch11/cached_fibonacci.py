cache = {0: 1, 1: 1}


def fibonacci(n):
    if n in cache:
        return cache[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = res
    return res


if __name__ == "__main__":
    print(fibonacci(2500))
