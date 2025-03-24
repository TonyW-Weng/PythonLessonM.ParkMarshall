# Lesson 47
def repeatedSum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + repeatedSum(num - 1)

number = int(input("Enter your number: "))
print(repeatedSum(number))