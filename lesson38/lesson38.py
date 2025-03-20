# Lesson 38
def isPal(text):
    return text == text[::-1]

palNumber = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        currentProduct = num1*num2

        if isPal(str(currentProduct)):
            palNumber.append(currentProduct)

print(f"The largest pal of the product of given numbers is {max(palNumber)}")