# Lesson 17
num = int(input("Enter your number: "))
totalProduct = 1
multipler = 1

while multipler <= num:
    totalProduct = totalProduct * multipler
    multipler += 1
print(f"Factorial of {num} is {totalProduct}")

secondAnswer = 1
for i in range(num, 0, -1): # it will loop from num to 0 going down by the thrid number which is -1
    secondAnswer *= i

print(f"Factorial of {num} is {secondAnswer}")

thridAnswer = 1
for j in range(1, num+1): # will start at 1 and slowly goes up to num + 1 since range doesn't exculde the last one
    thridAnswer *= j

print(f"Factorial of {num} is {thridAnswer}")