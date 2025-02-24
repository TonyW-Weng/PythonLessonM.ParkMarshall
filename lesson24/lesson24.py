# Lesson 24
condition = True
longestLength = 0
longestName = ""

while condition:
    name = input("Enter a name or \" X \" to exit: ")
    if name.lower().capitalize() == 'X':
        condition = False
        break
    if len(longestName) < len(name):
        longestName = name
        longestLength = len(name)

print(f"The longest name is {longestName} with a length of {longestLength}")