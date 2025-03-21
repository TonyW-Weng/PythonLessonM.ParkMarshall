# Lesson 40
def primeNumber(number):
    primes = []
    for i in range(1, number+1):
        Count = 0
        for j in range(1, i+1):
            if i % j == 0:
                Count += 1
        if Count == 2:
            primes.append(i)
    return primes

number = int(input("Enter your number: "))
print(f"{primeNumber(number)}")