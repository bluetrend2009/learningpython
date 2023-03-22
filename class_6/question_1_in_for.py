current_num = 1
next_num = 1

for i in range(25):
    print(current_num)
    prev_next_num = next_num
    next_num = current_num + prev_next_num
    current_num = prev_next_num
