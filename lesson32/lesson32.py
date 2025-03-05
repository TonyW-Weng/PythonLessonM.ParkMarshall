# Lesson 32

def sortedString(textOne, textTwo):
    print(textOne)
    print(textTwo)
    if  not textOne or not textTwo:
        return []
    else:
        setWordTwo = set(textTwo)
        setWordOne = set(textOne)
        result = []
        for character in setWordOne:
            if character in setWordTwo:
                result.append(character)
        return sorted(result)

wordOne = input("Enter your first string: ")
wordTwo = input("Enter your second string: ")
print(f"{sortedString(wordOne, wordTwo)}")