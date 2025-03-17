# Lesson 35
def removeDupe(list):
    testList = list
    newList = []
    for item in testList:
        if item not in newList:
            newList.append(item)

    return newList

testList = ["a", "b", "c", "d", "e", "a", "b", "c"]
print(f"{testList}")
print(f"{removeDupe(testList)}")