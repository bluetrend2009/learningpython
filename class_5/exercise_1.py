a = 0
b = 1


def cal_next_fibo():
    global a, b
    temp = b
    b = a + b
    a = temp
    print(a)
    if b <= 100:
        cal_next_fibo()


cal_next_fibo()
