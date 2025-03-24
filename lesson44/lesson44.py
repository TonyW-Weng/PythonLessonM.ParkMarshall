# Lesson 44
def frequency(word):
    cleanWord = sorted(word.lower())
    answer = {}
    for character in cleanWord:
        if character not in answer:
            answer[character] = 1
        else:
            answer[character] += 1
    return answer

userWord = input("Enter your word: ")
print(frequency(userWord))