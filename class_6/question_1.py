current_num = 1
next_num = 1

count = 0


def get_next_fibonacci():
    global current_num, next_num, count
    count = count + 1
    print(f"count {count} is {current_num}")
    prev_next_num = next_num
    next_num = current_num + prev_next_num
    current_num = prev_next_num
    if count < 25:
        get_next_fibonacci()


get_next_fibonacci()
