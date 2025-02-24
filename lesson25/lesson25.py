# Lesson 25
number = int(input("Enter your limit: "))
copyNumber = number

largest = 0

while number % 2 == 0:
    number //= 2

    largest = max(largest, 2)

if number != 1:
    factor = 3
    while number != 1:
        if number % factor == 0:
            largest = max(largest, factor)
            number //= factor
        else:
            factor += 2

print(f"{largest} is the prime factor for {copyNumber}")