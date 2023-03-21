# find absolute number of number entered 

num = int(input("Enter negative number"))

abs_num = abs(num)

print("{num} absolute number is {abs_num}")


#not working so using a longer version:

num = float(input("Enter a number: "))

if num < 0:
    abs_value = -num
else:
    abs_value = num

print(f"The absolute value of {num} is {abs_value}")