# Lesson 7
from random import randrange
difficultity = int(input("Enter how hard this check is: "))
playerRoll = randrange(1, 21) #Range includes the first number but exculdes the last number
if playerRoll >= difficultity:
    print(f"The player passes the check because {playerRoll} >= {difficultity}")
else:
    print(f"The player has failed the check because {playerRoll} < {difficultity}, truly a sad moment")