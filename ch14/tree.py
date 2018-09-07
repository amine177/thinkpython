import os


def tree(d, space=0):
    if os.path.isfile(d):
        print((space*'-')+'>'+os.path.relpath(d))

    else:
        print('***'+d)
        for pt in os.listdir(d):
            pt = os.path.join(d, pt)
            tree(pt, space+1)


if __name__ == "__main__":
    tree("..")
