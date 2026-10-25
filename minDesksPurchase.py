#Minimum number of desks for school
import math
a = int(input("Enter number of desks in class 1: "))
b = int(input("Enter number of desks in class 2: "))
c = int(input("Enter number of desks in class 3: "))

#Constraints are each desk seats 2 students and all students must be seated in their respective classes
desksInA = math.ceil(a/2)
desksInB = math.ceil(b/2)
desksInC = math.ceil(c/2)

totalPurchase = desksInA + desksInB + desksInC

print(f"Total number of desks to purchase are {totalPurchase}")
