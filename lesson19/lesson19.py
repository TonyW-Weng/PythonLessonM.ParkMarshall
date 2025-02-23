# Lesson 19
number = int(input("Enter your number: "))
totalFactors = 0 # counts 1 and itself
for i in range(1, number+1):
    if number % i == 0:
        totalFactors += 1

if totalFactors == 2:
    print("IS a PRIME")
else:
    print("NOT a PRIME")