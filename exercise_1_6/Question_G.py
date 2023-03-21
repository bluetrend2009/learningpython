# prompt user to enter 3 angles of a triangle. Define if triangle or not

ang_a = input("Enter the first angle") # NO NEED TO ADD INT ?
ang_b = input("Enter the second angle")
ang_c = input("Entger the third angle")

if int(ang_a) + int(ang_b) + int(ang_c) == 180: 
    print("It is a triangle")
else:
    print("This is not a triangle as the sum of its angle is superior to 180")

