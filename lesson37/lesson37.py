# Lesson 37
def convert(text):
    newText = ''
    count = 1
    for i in range(1, len(text)):
        print(text[i])
        if text[i] == text[i - 1]:
            count += 1
        else:
            newText += text[i - 1]
            newText += str(count)
            count = 1
    newText += text[-1] + str(count)
    if len(text) >= len(newText):
        return newText
    else:
        return text

userInput = input("Enter your text: ")
print(f"The new text is: {convert(userInput)}")