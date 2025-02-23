# Lesson 10
digits = input("Enter the four digits: ")

if digits[0] in {'8', '9'}:
    if digits[1] == digits[2]:
        if digits[3] in {'8', '9'}:
            print("Is a telemarketer")
        else:
            print("Is not a telemarketer")
    else:
        print("Is not a telemarketer")
else:
    print("Is not a telemarketer")
