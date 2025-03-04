# Lesson 26
def factorCounter (number):
    counter = 0
    for i in range (1, number+1):
        if number % i == 0:
            counter += 1
    return counter

upperLimit = int(input())
for i in range (1, upperLimit + 1):
    factorSize = factorCounter(i)

    print(f"{i} has {factorSize} number of factors")