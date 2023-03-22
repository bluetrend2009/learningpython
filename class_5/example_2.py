number = 100


def subdivide():
    global number
    number = number / 2
    print(number)
    subdivide()


subdivide()
