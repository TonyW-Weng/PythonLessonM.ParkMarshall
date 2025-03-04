# Lesson 28
def checkWord(text):
    condition = True
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            condition = False
            return condition
            break
    return condition

string = input("Enter your string: ")
print(checkWord(string))