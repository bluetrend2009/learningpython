num = 1


def change_the_number():
    global num
    num = 10
    return num


print(change_the_number())

print(num)
