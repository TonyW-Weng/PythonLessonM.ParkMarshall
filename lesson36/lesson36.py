# Lesson 36
# finding the factors of a number and prime of a number

def factor(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def primes(number):

    return len(factor(number)) == 2
print(f"Factors of 13: {factor(13)}")
print(f"Factors of 36: {factor(36)}")
print(f"Is 13 Prime: {primes(13)}")
print(f"Is 36 Prime: {primes(36)}")