# Lesson 23

condition = True
Sum = 0
numberOfInput = 0
while condition:
    user = input("Enter your number or \"Exit\" to exit: ")
    if user.lower().capitalize() ==  'Exit':
        condition = False
        break
    else:
        mark = int(user)
        if 0 <= mark <= 100:
            Sum += mark
            numberOfInput += 1
        else:
            print("Invalid mark")
if numberOfInput == 0:
    print("There is literally nothing")
else:
    average = Sum / numberOfInput
    print(f"Your average is {average}")