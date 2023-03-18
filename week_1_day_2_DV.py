# take input from the user with the prompt for basic salary
# this input taken as string so it is casted to float and saved to basic

basic = float(input("What is Ramesh's basic salary? "))
# dearness allowance is 40%
da = 0.4 * basic
# house rent allowance is 20%
hra = 0.2 * basic
# professional tax is 200
prof_tax = 200
# provident fund is 4300
prov_fund = 4300
# gross amount is basic + allowances - deductions
gross = basic + da + hra - prof_tax - prov_fund
# print the gross amount
print(f"Ramesh's gross salary is: {gross}")

#EXERCICE B
# distance between 2 cities is input to the program via the keyboard.
# write program to convert and print the distance in meters, miles, feet, inches and centimeter

#prompt user to enter distance
distance = float(input("What is the distance in km between Paris and New York? "))

#calculate the equivalent distance 
dm = distance * 1000
dmiles = distance * 0.62
dfeet = distance * 3280
dinch = distance * 39370
dcm = distance * 100000

#print the result for each 
print(f"The distance between Paris and New York in kilometers is {distance}")
print(f"The distance between Paris and New York in meters is {dm}")
print(f"The distance between Paris and New York in miles is {dmiles}")
print(f"The distance between Paris and New York in feet is {dfeet}")
print(f"The distance between Paris and New York in inches is {dinch}")
print(f"The distance between Paris and New York in centimeters is {dcm}")

# EXERCICE C
# marks obtained by a student in 5 different subjects are input via keyboard
# find the total marks and percentage marks obtained by the student. Max mark is 100 by subject.

# Prompt user to enter marks for each subject
subject1_marks = int(input("Enter marks for subject 1 : "))
subject2_marks = int(input("Enter marks for subject 2 : "))
subject3_marks = int(input("Enter marks for subject 3 : "))
subject4_marks = int(input("Enter marks for subject 4 : "))
subject5_marks = int(input("Enter marks for subject 5 : "))

# Calculate aggregate and percentage marks
aggregate_marks = subject1_marks + subject2_marks + subject3_marks + subject4_marks + subject5_marks
percentage_marks = (aggregate_marks / 500) * 100

# Print the results
print(f"Aggregate marks obtained by the student: {aggregate_marks} out of 500")
print(f"Percentage marks obtained by the student: {percentage_marks}%")

#EXERCICE D

# temperature in degree fahrenheit is input via keyboard
# what is the temperature in celsius degrees

# prompt the user to enter temperature in F degrees
tempF = float(input("What is the current temperature in degrees Fahrenheit? "))

# compute the equivalent in celsius degreese
tempC = tempF / 5

# print the result 
print(f"The temperature in celsius degrees is {tempC}. ")

#EXERCICE E
# length and breadth of a rectangle and radius of circle are input via keyboard
# compute the area and perimeter of rectangle and area and circumference of the circle

#prompt user to enter measurement of of two geometric figures
L_rectangle = float(input("What is the lenght of the rectangle? "))
B_rectangle = float(input("What is the breadth of the rectangle? "))
R_circle = float(input("What is the radius of the circle? "))

#compute area and perimeter for rectangle
a_rectangle = L_rectangle * B_rectangle 
p_rectangle = L_rectangle * 2 + B_rectangle *2

#compute area and perimeter for circle
a_circle = R_circle * R_circle * 3.14116
p_circle = R_circle * 3.141 * 2

# print the result 
print(f"The area of the rectangle is {a_rectangle}")
print(f"The perimeter of the rectangle is {p_rectangle}")
print(f"The area of the circle is {a_circle}")
print(f"The perimeter of the circle is {p_circle}")

#EXERCICE F
# 2 numbers are input via key board into two location C and D
# write prog to interchange contents of C and D
# ?????? don t know how to do this

#EXERCICE G
# 5 digit number input. Calculate the sum of the digits

#prompt user to input a 5 digit number
number = int(input("Write a 5 digit number"))

#compute the sum of the 5 digits included in the number
number_sum = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]) + int(number[4])

#print result
print(f"The sum of the digits in {number} is {number_sum}")

#EXERCICE H
# 5 digits number as input - print the reverse

#prompt user to input a 5 digits number
number = int(input("Write a 5 digit number"))

#compute the reverse of the 5 digits number
rev_number = int(number[4]), int(number[3]), int(number[2]), int(number[1]), int(number[0])

#print result
print(f"The reverse of {number} is {rev_number}")

#EXERCICE I
#??? don t know how to do this

#EXERCICE J
# In a town, percentage of men if 52%. Total literacy is 48%. If 35% of men are literate in total population
# find total number of illiterate men and women if total pop is 80,000

#prompt user to input total population number
total_pop = int(input("What is the total population of the town? "))

#compute men and women illiterate number
num_men = total_pop * 52 / 100
num_men_literate = num_men * 35 / 100
num_men_illiterate = num_men - num_men_literate

num_women = total_pop - num_men
num_women_literate = total_pop * 48 / 100 - num_men_literate
num_women_illiterate = num_women - num_women_literate

#print results
print(f"The number of illiterate men in the town is {num_men_illiterate}")
print(f"The number of illiterate women in the town is {num_women_illiterate}")

#EXERCICE k
#cashier has notes of 10,50 and 100. Input = amount to be withdrawn in 100. Find total number of currency note to be given.

cash_amount = int(input("Hello, how much would you like to withdraw? "))

#??? not sure how to do it - probably with an if - else

# EXERCICE L
# total selling price of 15 items and total profit is input - print cost price

#prompt user to input selling prices and total profits
total_sp = float(input("What is the selling price of the 15 items? "))
total_pr = float(input("What is the total profit earned on the 15 items? "))

#compute cost price
total_cp = total_sp - total_pr
unit_c = total_cp / 15

#print results
print(f"The unit cost of each item is {unit_c}. ")

#EXERCICE M
# 5 digit number input - print 5 digit number made with +1 at each digit

#prompt user to input 5 digit number
five_dn = int(input("Please type in a 5 digit number"))

#new number












