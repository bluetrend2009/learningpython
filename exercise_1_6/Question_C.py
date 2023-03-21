# input any year - Leap year of not

year = int(input("What is the year? ")) #WHY NOT WORKING IF I DON T PUT INT() = because can not cacul with string
                                        # ALWAYS START WITH LEAST EXCLUSIVE CONDITION

if year % 400 == 0: 
    print("This is a leap year")

elif year % 100 == 0:
    print("This is not a leap year")

elif year % 4 == 0: 
    print("This is a leap year")

else: 
    print("This is a leap year")