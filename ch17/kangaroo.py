

class kangaroo:

    def __init__(self, p=None):
        if p is None:
            self.p_c = []
        else:
            self.p_c = p

    def put_in_pouch(self, o):
        self.p_c.append(o)

    def __str__(self):
        return 'kangaroo:' + str(self.p_c)


if __name__ == "__main__":
    k1 = kangaroo()
    k1.put_in_pouch(1)
    k2 = kangaroo()
    k2.put_in_pouch(2)
    print(k1)
    print(k2)
