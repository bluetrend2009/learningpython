#EXERCICE H
# 5 digits number as input - print the reverse

#prompt user to input a 5 digits number
number = input("Write a 5 digit number")

#compute the reverse of the 5 digits number
rev_number = number[4] + number[3] + number[2] + number[1] + number[0]

#print result
print(f"The reverse of {number} is {rev_number}")