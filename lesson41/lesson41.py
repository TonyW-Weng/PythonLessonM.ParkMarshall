# Lesson 41
def score(word):
    score = 0
    for letter in word:
        currentLetter = letter.upper()
        if currentLetter in "EAIONRTLSU":
            score += 1
        elif currentLetter in "DG":
            score += 2
        elif currentLetter in "BCMP":
            score += 3
        elif currentLetter in "FHVWY":
            score += 4
        elif currentLetter == "K":
            score += 5
        elif currentLetter in "JK":
            score += 8
        elif currentLetter in "QZ":
            score += 10
    return score

userWord = input("Enter your word: ")
print(score(userWord))
