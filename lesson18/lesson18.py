# Lesson 18
number = int(input("Enter your number: "))
for i in range(1, number+1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")
