# Lesson 4
import math

fenceOne = len(input())
fenceTwo = len(input())
fenceThree = len(input())

totalFence = fenceOne + fenceTwo + fenceThree
paintCansOrders = totalFence / 12
paintCansOrders = math.ceil(paintCansOrders)

paintCansNeededBrought = paintCansOrders * 12
remainingPaintCans = paintCansNeededBrought - totalFence
totalCost = paintCansOrders * 14.95

print(totalFence)
print(remainingPaintCans)
print(totalCost)
print("Nice")