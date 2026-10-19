import math

numberOfClasses = int(input("Enter the number of classes: "))
classes = []
for i in range(1,numberOfClasses + 1):
    clas = int(input(f"Enter the number of students in class{i}: "))
    classes.append(clas)

sum = 0
for i in classes:
    sum += math.ceil(i/2)

print(f"The number of desks to buy: {sum}")
