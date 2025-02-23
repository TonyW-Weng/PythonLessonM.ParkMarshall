# Lesson 9
from random import choice

invalid = True

while invalid:
    playerChoice = input("Enter a choice of rock, paper, or scissors: ")
    if playerChoice in {'rock', 'paper', 'scissors'}:
        invalid = False

cpu = choice(['rock', 'paper', 'scissors'])
print(f"The player use: {playerChoice}")
print(f"The cpu use: {cpu}")
if playerChoice == cpu:
    print("tie game")
else:
    if playerChoice == 'rock':
        if cpu == 'paper':
            print("cpu wins")
        else:
            print("player wins")
    if playerChoice == 'paper':
        if cpu == 'scissors':
            print("cpu wins")
        else:
            print("player wins")
    if playerChoice == 'scissors':
        if cpu == 'rock':
            print("cpu wins")
        else:
            print("player wins")
