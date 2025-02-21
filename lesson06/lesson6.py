# Lesson 6
name = "Tony Weng"
if name:
    print(name)
else:
    print("There is literally nothing")

nameGiven = input()
if not name:
    print("Name not given")
else:
    print(f"Hello {nameGiven}!")

if "o" in nameGiven:
    print("o is in the given name")
else:
    print("o is not in the given name")

if "apple" not in ["banana", "kiwi", "fruit"]:
    print("apple is not in the given list")
else:
    print("apple is in the given list")

print("end")