# Lesson 8
wins = input().count("W") # only works if on one line if you want, trying things out
if wins >= 5:
    print("You are in group 1")
elif wins >= 3:
    print("You are in group 2")
elif wins >= 1:
    print("You are in group 3")
else:
    print("You'reeeee Out!")

# can also be done as the following:

winCount = 0
for i in range(6): # counts from 0 to 5 which is 6 total number inputs
    currentResult = input(f"Enter the game result for game {i + 1}: ")
    if currentResult == "W":
        winCount += 1

group = 0
if winCount > 4:
    group = 1
elif winCount > 2:
    group = 2
elif winCount > 2:
    group = 3

if group == 0:
    print("You are elimated from the tourney, truly a rip moment")
else:
    print(f"You are in group {group}")