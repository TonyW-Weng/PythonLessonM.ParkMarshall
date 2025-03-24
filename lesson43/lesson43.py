# Lesson 43
#Q1
def removeDupe(aList):
    result = []
    for value in aList:
        if value not in result:
            result.append(value)
    return result

listOne = [1, 2, 3, 4, 4, 5, 6, 7, 7, 4, 9, 0]
print(removeDupe(listOne))

#set version
def removeDupeSet(aList):
    return list(set(aList))

print(removeDupeSet(listOne)) #also orders it
#Q2
def uniqueLetter(aList):
    resultSet = set()
    for word in aList:
        tmpSet = set(word)
        resultSet = resultSet | (tmpSet)
    return resultSet

test = ["hello", "goodbye!", "world", "tony"]
print(uniqueLetter(test))
#Q3
def iCount(aList):
    if aList:
        resultSet = aList[0]
        for exampleSet in aList[1:]:
            resultSet = resultSet & exampleSet
        return len(resultSet)
    
test = [{1,2,3,7}, {3,4,5,7}, {6,7,8,7,3}]
print(iCount(test))