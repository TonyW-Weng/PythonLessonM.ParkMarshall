# Lesson 27
def cleanString(text):
    result = ''
    for character in text:
        if character.isalpha():
            result += character.lower()
    return result

string = input("Enter your string: ")
print(cleanString(string))