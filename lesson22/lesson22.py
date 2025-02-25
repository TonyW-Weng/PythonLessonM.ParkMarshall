# Lesson 22
number = int(input("Enter your limit: "))
fibZero = 0
fibOne = 1
fibN = 0

for n in range(2, number+1):
    fibN = fibOne + fibZero

    fibZero = fibOne
    fibOne = fibN
if number == 1:
    print(1)
else:
    print(f"Fibonacci({number}) is {fibN}")