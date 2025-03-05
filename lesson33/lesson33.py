# Lesson 33
def mean(list):
    # Find the average
    numberList = list
    totalSum = sum(numberList)
    size = len(numberList)
    return totalSum / size

def medium(list):
    numberList = list
    size = len(numberList)
    medium = numberList[size//2]
    return medium


numberList = []
loop = int(input("Enter your numbers for how many more numbers to enter: "))
count = 0
while count < loop:
    number = int(input("Enter your number: "))
    numberList.append(number)
    count += 1

print(f"{mean(numberList)}")
print(f"{medium(numberList)}")