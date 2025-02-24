# Lesson 21
numberInput = int(input("Enter your number: "))
number = 0
highestNumberOfFactors = 0

for i in range (1, numberInput+1):
    totalFactors = 0
    for divide in range(1, i+1):
        if i % divide == 0:
            totalFactors += 1
    if totalFactors > highestNumberOfFactors:
        highestNumberOfFactors = totalFactors
        number = i
            
print(f"The number with the highest amount of factors is: {number} with {highestNumberOfFactors} factors")