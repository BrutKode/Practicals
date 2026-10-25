#Swap two variables
a = int(input("Enter the value of variable 1: "))
b = int(input("Enter the value of variable 2: "))

print("Before swapping: ", a, b)

tmp = a #Set temporary variable to store state of a
a = b   #Information stored in a is lost
b = tmp

print("After swapping: ", a, b)