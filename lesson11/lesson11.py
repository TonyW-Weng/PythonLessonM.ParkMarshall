# Lesson 11
cordinates = input("Enter your two points: ")
cordinates = cordinates.split(' ') # splits into two different ints "10 -11" -> [10, -11]
cordinates = list(map(int, cordinates)) # map makes it iteratable and list makes a list

x, y = cordinates
if x > 0:
    if y > 0:
        print("We are in quadrant 1")
    else:
        print("We are in quadrant 4")
else:
    if y > 0:
        print("We are in quadrant 2")
    else:
        print("We are in quadrant 3")