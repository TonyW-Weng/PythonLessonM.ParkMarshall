# Lesson 45
#Q1
def dic(aList):
    answer = {}
    for item in aList:
        if item not in answer:
            answer[item] = len(item)
    return answer

test = ["apple", "banana", "pineapple", "watermelon", "strawberry"]
print(dic(test))

#Q2
def fib(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2, num+1):
            result[i] = result[i - 1] + result[i - 2]

        return result
number = int(input("Enter your number: "))
print(fib(number))