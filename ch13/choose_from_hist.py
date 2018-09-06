import random


def chose_hist(h):

    prob_vect = []
    freq = 0
    for i in h:
        prob_vect.extend([i] * h[i])
        freq += h[i]

    return prob_vect[random.randint(0, freq-1)]


if __name__ == "__main__":
    for i in range(9):
        print(chose_hist({'a': 2, 'b': 1}))
