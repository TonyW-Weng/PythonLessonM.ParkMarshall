# Lesson 13
month = int(input())
day = int(input())

if month == 2 and day == 18:
    print("Special day")
elif month < 2:
    print("Before")
elif month > 2:
    print("After")
else:
    # month has to be 2 but not day 18
    if day < 18:
        print("Before")
    else:
        print("After")
