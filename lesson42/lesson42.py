# Lesson 42
def possibleSum(aList, target):
    for i, value in enumerate(aList):
        newTarget = target - value
        if newTarget in aList[i+1:]:
            return True
    return False

test = [1, 3, 5, 8, 12, 13, 22]
target = 23

print(possibleSum(test, target))