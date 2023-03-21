# prompt user to enter a 5 digit number
# obtain the reversed number and determine if reversed number is equal or not the the original number

num = input("Enter a 5 digit number ")

num_rev = (num[4]) + (num[3]) + (num[2]) + (num[1]) + (num[0])

print(f"{num_rev}")

if num_rev == num: 
    print("Both number are identical")
else:
    print("Both numbers are different")