#Minimum number of desks for school
import math
a = 20
b = 21
c = 22

#Constraints are each desk seats 2 students and all students must be seated in their respective classes
desksInA = math.ceil(a/2)
desksInB = math.ceil(b/2)
desksInC = math.ceil(c/2)

totalPurchase = desksInA + desksInB + desksInC