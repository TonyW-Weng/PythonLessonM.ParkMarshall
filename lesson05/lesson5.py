# Lesson 5
start_money = float(input())
cookies_sold = input()

bigCookies = 0
smallCookies = 0

for currentCookie in cookies_sold:
    if currentCookie == 'c':
        smallCookies += 1
    elif currentCookie == 'b':
        bigCookies += 1
    else:
        print(f"{currentCookie} Not a valid sale item")

totalNumCookie = bigCookies + smallCookies
profit = (bigCookies*1.25) + (smallCookies*0.75)
endDay = start_money + profit
print(totalNumCookie)
print(profit)
print(endDay)