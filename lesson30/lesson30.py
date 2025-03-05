# Lesson 30
patternLength = int(input("Enter your pattern length: "))
pattern = '1'
for i in range(patternLength):
    print(pattern)
    if i % 2 == 0:
        pattern += '0'
    else:
        pattern += '1'
