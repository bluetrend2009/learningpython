#EXERCICE G
# 5 digit number input. Calculate the sum of the digits

#prompt user to input a 5 digit number
number = input("Write a 5 digit number")

#compute the sum of the 5 digits included in the number
number_sum = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]) + int(number[4]) # NOT SURE ABOUT THIS ONE

#print result
print(f"The sum of the digits in {number} is {number_sum}")