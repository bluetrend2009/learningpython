#If the ages of Sam, Alex, and Robin are input through the keyboard, write a
#program to determine the youngest of the three.

Sam_age = int(input("What is Same' age? "))
Alex_age = int(input("What is Alex' age? "))
Robin_age = int(input("What is Robin' age? "))

if Sam_age == Alex_age or Sam_age == Robin_age or Alex_age == Robin_age:
    print("Some of them have the same age")

if Sam_age < Alex_age and Sam_age < Robin_age:
    print("Sam is the youngest")

elif Alex_age < Sam_age and Alex_age < Robin_age:
    print("Alex is the youngest")

else:
    print("Robin is the youngest")


