import math

class1 = int(input("Enter the number of students in class 1: "))
class2 = int(input("Enter the number of students in class 2: "))
class3 = int(input("Enter the number of students in class 3: "))

classes = [class1, class2, class3]

sum = 0
for i in classes:
    sum += math.ceil(i/2)

print(f"The number of desks to buy: {sum}")
