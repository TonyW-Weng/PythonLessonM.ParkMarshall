# Lesson 31
'''
two ways to solve this
first way is to check if 
'''

def firstWay(textOne, textTwo):
    if len(textOne) != len(textTwo):
        return False
    else:
        textOneList = []
        for i in range (len(textOne)):
            textOneList.append(textOne[i])
        textOneList.sort()

        textTwoList = []
        for i in range (len(textTwo)):
            textTwoList.append(textTwo[i])
        textTwoList.sort()
    
        if textOneList == textTwoList:
            return True
        else:
            return False

def secondWay(textOne, textTwo):
    if len(textOne) != len(textTwo):
        return False
    else:
        listWordOne = sorted(textOne)
        listWordTwo = sorted(textTwo)
        for i, character in enumerate(listWordOne):
            if listWordTwo[i] != character:
                return False
            else:
                return True

way = input("Enter which way you want to check: ")
wordOne = input("Enter your first word: ")
wordTwo = input("Enter your second word: ")
way = way.lower()
if way == "first":
    print(f"{firstWay(wordOne, wordTwo)}")
else:
    print(f"{secondWay(wordOne, wordTwo)}")