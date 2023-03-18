print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

print("so far this is going well")

print("Hello World!")
#print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
#print('I "said" do not touch this.')

#Exercise 2 _ Numbers and Maths

print(3 + 4) # used to compute addition
print(3 - 4) # used to compute substraction
print(4 / 5) # used to compute division
print(4 * 5) # used to compute multiplication
print(4 % 5) # used to find the remainder when one number is divided by another (Modulus)

Assignement = "Easy" #used to assign a value or a definition to a variable
print(Assignement)

#== used to check if this is a number - example:
numb1 = 5
numb2 = 10
if numb1 == numb2:
    print("numb1 and numb2 are equal.")
else:
    print("numb1 and numb2 are not equal.")


# Greater than (>) #to compare two values and check if one value is greater than the other
#example:

age = 15

if age > 20:
    print("You can drive a car")
else:
    print("You are not old enough to drive a car.")

#Less than (<) # opposite of the above
#Less than equal and greater than equal = same usecase


#Exercise 3_ code to correct

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
print(f"==========\n{end1}{end2}{end3}{end4}{end5}{end6}\n==========")

# yes we can write cars=100 instead of cars = 100 but best practice the later
# (=) is to define value of variable, (==) is to compare to value
# no variable can not be only an integer
# floating point number are numbers with decimal(s)
# yes we can round a floating point number using "round"
# we have "" when this is a sentence/word we want to print and no "" when we call a variable
# not sure about the F....n...