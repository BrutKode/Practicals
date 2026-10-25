#Finding maximum of three numbers
a = int(input("Enter the value of first number: "))
b = int(input("Enter the value of second number: "))
c = int(input("Enter the value of third number: "))

if a>b and a>c:
    print("The greatest integer is", a)
elif b>a and b>c:
    print("The greates integer is", b)
else:
    print("The greatest integer is", c)