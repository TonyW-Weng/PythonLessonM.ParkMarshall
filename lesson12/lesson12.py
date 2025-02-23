# Lesson 12
angleOne = int(input("Enter your first angle: "))
angleTwo = int(input("Enter your second angle: "))
angleThree = int(input("Enter your thrid angle: "))
totalAngles = angleOne + angleThree + angleTwo

if totalAngles == 180:
    if angleOne == angleThree == angleTwo:
        print("This triangle is an equilateral")
    elif angleTwo != angleTwo and angleTwo != angleThree and angleOne != angleThree:
        print("This triangle is a scalene")
    else:
        print("This triangle is a isosceles")
else:
    print("Invalid")