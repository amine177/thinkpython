

def gettime():
    time = input("Enter time:")
    return int(round(float(time)))


def printtime(time):
    days = time // 86400
    time %= 86400
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("days: {:d}, hours: {:d}, minutes: {:d}, seconds: {:d}".
          format(days, hours, minutes, seconds))


if __name__ == '__main__':
    time = gettime()
    printtime(time)
