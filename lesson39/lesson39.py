# Lesson 39

def commonDiv(num1, num2):
    for divide in range(min(num1, num2), 0, -1):
        if num1 % divide == 0 and num2 % divide == 0:
            return divide
        
    return 1


numberOne = int(input("Enter your first number: "))
numberTwo = int(input("Enter your second number: "))
print(f"The greatest common divider of {numberOne} and {numberTwo} are {commonDiv(numberOne, numberTwo)}")
