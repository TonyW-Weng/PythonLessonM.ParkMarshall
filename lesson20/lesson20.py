# Lesson 20
# A perfect number is when the sum of its divider is equal to itself
totalSum = 0

for num in range(1, 10000):
    factorSum = 0
    for divide in range(1, num):
        if num % divide == 0:
            factorSum += divide
    if factorSum == num:
        totalSum += num
        print(f"{num} is a perfect number")

print(f"The total sum of all perfect numbers below 10000 is {totalSum}")