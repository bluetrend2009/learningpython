# prompt user to enter lenght and breadth of a rectangle. Define is area > perimeter

lenght = input("Enter the lenght of the rectangle")
breadth = input("Enter the breadth of the rectangle")

area = int(lenght) * int(breadth)
perimeter = int(lenght) * 2 + int(breadth) * 2

if area > perimeter:
    print("The area of the rectangle is larger than its perimeter")
else:
    print("The perimeter of the rectangle is larger than its area")
