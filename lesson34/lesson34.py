# Lesson 34
def splitString(text):
    aList = []
    csv = text.split(',')
    # print(csv)
    for item in csv:
        aList.append(int(item))
    return aList

from random import randrange

def randList(start, end, freq):
    if start < end and freq > 0:
        aList = []
        for _ in range(freq):
            newValue = randrange(start, end+1)
            aList.append(newValue)
        return aList
    else:
        return []

print(splitString("1,2,3,4,5,1,2,3"))
print(randList(1, 1000, 50))