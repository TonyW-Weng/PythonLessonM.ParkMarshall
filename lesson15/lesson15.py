# Lesson 15
conditionVar = True
password = "password"

while conditionVar:
    geuss = input("Geuss the password: ")
    if geuss != password:
        print("Try again")
    else:
        print("Good job, you can leave now")
        conditionVar = False

userInput = input("What fruit are you looking for?: ")
fruits = ['Apple', 'Kiwi', 'Banana', 'Strawberry']
found = False

for fruitName in fruits:
    if fruitName == userInput:
        print("We found the fruit!")
        found = True

if not found:
    print(f"{userInput} was not found")
