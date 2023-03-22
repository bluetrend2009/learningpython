# 1
# 2 3
# 4 5 6
# 7 8 9 10

current_num = 0

for line in range(1, 5):
    print("")
    for i in range(line):
        current_num = current_num + 1
        print(current_num, end=" ")
